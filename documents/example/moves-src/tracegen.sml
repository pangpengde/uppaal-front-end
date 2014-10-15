(*
load "Int";
load "parser";
load "CommandLine";
*)

open tparser;
exception mixedLists
exception noSuchT

fun getFirst(s,t) = s
fun getSecond(s,t) = t

fun getStates (s:sys) = map getFirst s

fun filterT [] = [] 
  | filterT((s,t)::rest) = if size(s)<4 then (s,t)::filterT rest else (if substring(s,0,3)="Con" orelse substring(s,0,3)="Syn" orelse substring(s,0,3)="Sch" then filterT rest else (if size(s) < 6 then (s,t)::filterT rest else (if substring(s,0,6)="DynPri" then filterT rest else (s,t)::filterT rest)))

fun getSt (s:sys) = map getFirst (getStates s)
fun getTSt (s:sys) = map filterT (getSt s)

fun getCont (s:sys) = map getSecond (getStates s)

fun exTM [] = 0
  | exTM((s,i)::rest) = if s="TM" then i else exTM rest

fun exTMs c = map exTM c

fun getLastSame ([a],b::rest) = [(a,b)]
  | getLastSame (a1::a2::arest,b1::b2::brest) = if a1=a2 then getLastSame(a2::arest,b2::brest) else (a1,b1)::getLastSame(a2::arest,b2::brest)
  | getLastSame _ = raise mixedLists

fun maxS(i,[]) = i  
  | maxS (i,(t,_)::rest) = if (size t>i) then maxS(size t,rest) else maxS(i,rest)

fun getMaxT (s:sys) = List.last(exTMs(getCont s))
fun getMaxS (s:sys) = maxS(0,hd(getTSt s))

fun space 0 = ""
  | space n = " "^space(n-1)

fun times(i,j) = if i=j then Int.toString(i mod 10) else 
		 (if i mod 2=0 then Int.toString(i mod 10) else " ")^times(i+1,j)

fun mkTime (s:sys) = space(getMaxS s)^" | "^times(0,getMaxT s)

fun getSforT "Done" = " "
  | getSforT "DoneU" = " "
  | getSforT "Running" = "+"
  | getSforT "RunningU" = "+"
  | getSforT "Released" = "O"
  | getSforT "Offset" = " "
  | getSforT "OffsetU" = " "
  | getSforT "Dmiss" = "X"
  | getSforT _ = "P"

fun findTforT(_,[]) = raise noSuchT 
  | findTforT(ts,(t,s)::rest) = if ts=t then (getSforT s) else findTforT(ts,rest)

fun tmln(_,_,_,[]) = ""
  | tmln(n,sym,ts,(i,st)::rest) = if n=i then findTforT(ts,st)^tmln(n+1,findTforT(ts,st),ts,rest) else sym^tmln(n+1,sym,ts,(i,st)::rest)

fun mkTimeT(ts,s:sys) = ts ^ space(getMaxS s-size ts)^ " | "^tmln(0," ",ts,getLastSame(exTMs(getCont s),getTSt s))

fun mkTimeTs([],_) = ""  
  | mkTimeTs(t::ts,s) = mkTimeT(t,s)^"\n"^mkTimeTs(ts,s)


fun getTfromS(s:sys) = map (fn(a,b)=>a) (hd(getTSt s))

fun mkTrace [] = ""
  | mkTrace (s:sys) = mkTime(s)^"\n"^mkTimeTs(getTfromS s,s)



(* function handelling arguments *)
fun main() = 
case CommandLine.arguments () of
(arg1::l) => 
  print(mkTrace(parsef arg1))
| _ => print "Usage: tracegen trace-file \n\n"

val _ = main();
