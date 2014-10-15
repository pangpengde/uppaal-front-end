(* Lexer and parser for MoVES using mosmllex and mosmlyac 
   Aske Brekling 13/5/2008
 *)
open Absyn;

(* Plain parsing from a string, with poor error reporting *)

fun parse str =
    let val lexbuf = Lexing.createLexerString str
        val expr   = MoVESpar.Main MoVESlex.Token lexbuf
    in
        Parsing.clearParser();
        expr
    end
    handle exn => (Parsing.clearParser(); raise exn);


(* Fancy parsing from a file; show the offending program piece on error *)

fun parseExprReport file stream lexbuf =
    let val expr = 
            MoVESpar.Main MoVESlex.Token lexbuf
            handle
               Parsing.ParseError f =>
                   let val pos1 = Lexing.getLexemeStart lexbuf
                       val pos2 = Lexing.getLexemeEnd lexbuf
                   in
                       Location.errMsg (file, stream, lexbuf) 
                                       (Location.Loc(pos1, pos2))
                                       "Syntax error."
                   end
             | MoVESlex.LexicalError(msg, pos1, pos2) =>
                   if pos1 >= 0 andalso pos2 >= 0 then
                       Location.errMsg (file, stream, lexbuf)
                                       (Location.Loc(pos1, pos2))
                                       ("Lexical error: " ^ msg)
                   else 
                       (Location.errPrompt ("Lexical error: " ^ msg ^ "\n\n");
                        raise Fail "Lexical error");
    in
        Parsing.clearParser();
        expr
    end
    handle exn => (Parsing.clearParser(); raise exn);

(* Parse a program from a string, with error reporting *)

fun parses str =
    parseExprReport "" (BasicIO.std_in) (Lexing.createLexerString str);

(* Create lexer from instream *)

fun createLexerStream (is : BasicIO.instream) =
    Lexing.createLexer (fn buff => fn n => Nonstdio.buff_input is buff 0 n)

(* Parse a program from a file, with error reporting *)

fun parsef file =
    let val is     = Nonstdio.open_in_bin file
        val expr   = parseExprReport file is (createLexerStream is)
                     handle exn => (BasicIO.close_in is; raise exn)
    in 
        BasicIO.close_in is;
        expr
    end;



