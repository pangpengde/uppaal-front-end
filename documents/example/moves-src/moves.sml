(*
load "Int";
load "parser";
load "CommandLine";
*)

infix isin;
open parser;
exception EmptyList;

(*
type pname = string
datatype sch = FP | RM | EDF
datatype pe = P of (pname * sch)
type tname = string
type bcet = int
type wcet = int
type period = int
type offset = int
datatype task = T of (tname * bcet * wcet * period * offset)
type plat = pe list
type appl = task list
type mapping = tname -> pname
type depend = (tname * tname) list
datatype sys = S of (plat * appl * mapping * depend)
*)

fun getPName (P(n,_)) = n
fun getSch (P(_,s)) = s
fun getTName (T(n,_,_,_,_)) = n
fun getBC (T(_,b,_,_,_)) = b
fun getWC (T(_,_,w,_,_)) = w
fun getPi (T(_,_,_,p,_)) = p
fun getO (T(_,_,_,_,off)) = off

exception wrongName;
local
    fun isPName(n,p) = n=getPName p
in
    fun getP(_,[]) = raise wrongName
      | getP(n,p::rest) = if isPName(n,p) then p else getP(n,rest)
    fun getPIndex(_,_,[]) = raise wrongName
      | getPIndex(i,n,p::rest) = if isPName(n,p) then i else getPIndex(i+1,n,rest)
end

local
    fun isTName(n,t) = n=getTName t
in
    fun getT(_,[]) = raise wrongName
      | getT(n,t::rest) = if isTName(n,t) then t else getT(n,rest)
end

fun remDuplicates(lst) = List.foldr (fn(x,ys) => if (List.exists (fn y => x=y) ys) then ys else x::ys) [] lst

fun constructTList [] = []
  | constructTList(t::rest) = getTName t::constructTList(rest)

fun getPforT (_,[]) = raise mappingError
  | getPforT (t, (tn,pn)::rest) = if t=tn
				  then pn:pname
				  else getPforT(t,rest)


fun constructPList ([],_) = [] 
  | constructPList(t::app,mp) = getPforT(getTName t,mp)::constructPList(app,mp)

fun nrOfOccur p [] = 0
  | nrOfOccur p (pn::rest) = (if p=pn then 1 else 0) + nrOfOccur p rest

fun extractPs [] = []
  | extractPs(p::rest) = getPName p::extractPs(rest)

fun collectAux [] _ = []
  | collectAux (p::rest) cpl = (nrOfOccur p cpl)::(collectAux rest cpl)

fun collectNrOfOcc(plat,app,mp) = collectAux (extractPs(plat)) (constructPList(app,mp))

fun maxOfIntList [] = 0
  | maxOfIntList (l::lst) = let val m = maxOfIntList lst
			    in if l>m then l else m
			    end

fun maxTonP(plat,app,mp,dp) = let val (occList) = collectNrOfOcc(plat,app,mp)
			      in maxOfIntList occList
			      end

fun mkPSch FP = "FP"
  | mkPSch RM = "RM"
  | mkPSch EDF = "EDF"

fun mkProcSch [] = raise EmptyList
  | mkProcSch([p]) = mkPSch(getSch p)
  | mkProcSch(p::rest) = mkPSch(getSch p)^", "^(mkProcSch rest)

fun mkOnPET(_,[],_,_) = raise EmptyList
  | mkOnPET(i,[T(t,_,_,_,_)],p,mp) = if (getPforT(t,mp)=p) then [i] else []
  | mkOnPET(i,T(t,_,_,_,_)::rest,p,mp) = if getPforT(t,mp)=p then i::mkOnPET(i+1,rest,p,mp) else mkOnPET(i+1,rest,p,mp)

fun mkOnPE(_,[],_) = raise EmptyList
  | mkOnPE(ts,[p],mp) = [mkOnPET(1,ts,getPName p,mp)]
  | mkOnPE(ts,p::rest,mp) = (mkOnPET(1,ts,getPName p,mp))::(mkOnPE(ts,rest,mp))

fun mkOnPETAux(_,0) = ""
  | mkOnPETAux([],1) = "0"
  | mkOnPETAux([],i) = "0, "^mkOnPETAux([],i-1)
  | mkOnPETAux([t],1) = Int.toString(t)
  | mkOnPETAux([t],i) = Int.toString(t)^", "^mkOnPETAux([],i-1)
  | mkOnPETAux(t::rest,i) = Int.toString(t)^", "^mkOnPETAux(rest,i-1)

fun mkOnPETextAux([],_) = raise EmptyList
  | mkOnPETextAux([tlst],nr) = "{"^mkOnPETAux(tlst,nr)^"}"
  | mkOnPETextAux(tlst::rest,nr) = "{"^mkOnPETAux(tlst,nr)^"},"^mkOnPETextAux(rest,nr)

fun mkOnPEText(plat,app,mp,dp) = "{"^mkOnPETextAux(mkOnPE(app,plat,mp),maxTonP(plat,app,mp,dp))^"};\n"

fun mkFPris(_,[]) = raise EmptyList
  | mkFPris(i,[t]) = Int.toString(i)
  | mkFPris(i,t::rest) = Int.toString(i)^", "^mkFPris(i+1,rest)

fun appStrLst [] = ""
  | appStrLst [a] = a
  | appStrLst (h::t) = h^", "^appStrLst t 

fun mkX fnx tskl = appStrLst (map Int.toString (map fnx tskl))

val mkPi2 = mkX getPi

val mkO2 = mkX getO

fun mkPi [] = raise EmptyList
  | mkPi([t]) = Int.toString(getPi t)
  | mkPi(t::rest) = Int.toString(getPi t)^", "^mkPi(rest)

fun mkO [] = raise EmptyList
  | mkO([t]) = Int.toString(getO t)
  | mkO(t::rest) = Int.toString(getO t)^", "^mkO(rest)

fun _ isin [] = false
  | a isin (b::rest) = if a=b then true else a isin rest

fun mkDep(_,[],_) = raise EmptyList
  | mkDep(t,[tn],dp) = (if ((getTName tn,t) isin dp) then Int.toString(1) else Int.toString(0))
  | mkDep(t,tn::rest,dp) = (if ((getTName tn,t) isin dp) then Int.toString(1) else Int.toString(0)) ^ ", " ^ mkDep(t,rest,dp)

fun mkDepRel([],_,_) = ""
  | mkDepRel([t],ot,dp) = "{"^mkDep(getTName t,ot,dp)^"}"
  | mkDepRel(t::rest,ot,dp) = "{"^mkDep(getTName t,ot,dp)^"},"^mkDepRel(rest,ot,dp)

fun mkDepend(app,dp) = "{"^mkDepRel(app,app,dp)^"};\n"

exception MixedLists;
local
  (* findSmallestD: (int * _ * _)list -> int
   * Gives the smallest relative deadline in the list 
   *)
  fun findSmallestD [] = raise EmptyList
    | findSmallestD [(d,_,_)] = d
    | findSmallestD((d,_,_)::xs) = 
    let val sm = findSmallestD xs 
    in 
      if d<sm 
      then d 
      else sm 
    end

  local
    (* timeStep: (int * int * int * 'a) -> (int * int * 'a) 
     * Makes a time step for a single element in the list        
     *)
    fun timeStep(dead,step,per,e) = (((dead-step-1) mod per)+1,per,e)
  in
    (* timeStepList: (int * int * 'a)list -> (int * int * 'a)list
     * Makes a time step for the whole list with the smallest element
     *)
    fun timeStepList ds = map (fn (x,y,e) => timeStep(x,findSmallestD ds,y,e)) ds
  end
  local
    (* findAndRemoveSmallest: (int * int * 'a)list -> (int * int list)
     * Gives the element in the list with the smallest relative deadline as well as the 
     * list without that element 
     *)
    fun findAndRemoveSmallest [] = raise EmptyList
      | findAndRemoveSmallest [e] = (e,[])
      | findAndRemoveSmallest(x::xs) = 
      let val (sm,rest) = findAndRemoveSmallest xs 
          val (d1,_,_) = x
          val (d2,_,_) = sm
      in 
        if d1>d2 
        then (sm,x::rest) 
        else (x,xs) 
      end
    (* sortUList: (int * int * 'a)list -> (int * int * 'a) list
     * Sorts the list according to relative deadlines
     *)
    fun sortUList xs = 
      let val (sm,rest) = findAndRemoveSmallest xs 
      in 
        if rest = [] 
        then [sm] 
        else sm::sortUList rest 
      end
    (* getExt: (_, _, 'a) -> 'a
     * Gets the third element in a 3-tuple
     *) 
    fun getExt(_,_,ext) = ext
  in
    (* mkPrio: (int * int * 'a)list -> 'a list
     * Makes priorities for a given time step in the external representation ('a)
     *)
    fun mkPrio xs = map getExt (sortUList xs)
  end
  in
  local
    (* mkUListsAux: ((int * int * 'a)list * (int * int * 'a)list * int list * 'a list list) 
     *                                                         -> (int list * ''a list list)
     * Auxilary function for 'mkULists' collecting time step sizes in 'As' and a list of 
     * priorities in 'prios'
     *)
    fun mkUListsAux(ds, ods, As, prios) = 
      if ds=ods 
      then (As, prios) 
      else mkUListsAux(timeStepList ds, ods, findSmallestD ds::As, mkPrio ds::prios)
  in
    (* mkULists: (int * int * 'a)list -> (int list * 'a list list)
     * Function for creating urgency lists. It takes a list of elements (d,p,e) where 
     * d is the relative deadline, p is the period and e is the external representation 
     * for a given task 
     *)
    fun mkULists ds = 
      let val (ts,ps) = mkUListsAux(timeStepList ds, ds, [findSmallestD ds], [mkPrio ds])
      in  (rev ts, rev ps)
      end
  end
end

local
  (* optULists: (int list * 'a list list) -> (int list * 'a list list)
   * Function making optimized urgency lists, removing repeated elements
   * from the priority list by adding their durrations
   *)
  fun optULists([t], [p]) = ([t],[p])
    | optULists(t::ts, p::ps) = 
        let val (t1s, p1s) = optULists(ts,ps) 
        in 
          if hd p1s = p 
	  then ((t+hd t1s)::tl t1s, p1s) 
	  else (t::t1s, p::p1s)
        end
    | optULists _ = raise MixedLists
  (* sumList: (int * int list) -> int list
   * Function for adding a number to the head of an int list and adding 
   * the result of the addition to the rest of the elements in the list 
   * recursively
   *)
  fun sumList (_,[]) = []
    | sumList (n,x::xs) = x+n::sumList(x+n,xs)
in
  (* sumOptULists: (int * (int list * 'a list list)) -> (int list * 'a list list)
   * Function making the optimized urgency list and possibly adding a maximal offset
   * to the time steps
   *)
  fun sumOptULists(MO,(ts,ps),opt) =
    if(opt="O") then
      let val (ots,ops) = optULists(ts,ps)
      in (sumList(MO,ots), ops)
      end
    else
      (sumList(MO,ts),ps)
end

(* FSMO: (int * int * int * 'a)list -> int
 * Function for finding the smallest element in
 * offsets or relative deadlines
 *)
fun FSMO [] = raise EmptyList
  | FSMO [(d,off,_,_)] = if off=0 then d else off
  | FSMO((d,off,_,_)::rest) =
      let val sm = FSMO rest
      in 
	if off=0 
	then (if d<sm then d else sm) 
	else (if off<sm then off else sm)
      end

(* offStep: (int * int * int * 'a * int) -> (int * int * int * 'a)
 * Function taking a step during offset for a single element in
 * a (distance,offset,period,ext) list
 *)
fun offStep(d,off,per,ext,step) =
      if off > 0
      then 
        if off-step = 0 
        then (per, 0, per, ext)
        else (d,off-step, per, ext)
      else (((d-step-1)mod per)+ 1, off, per, ext)

(* offStep: (int * int * int * 'a)list -> (int * int * int * 'a)list
 * Function taking a step during offset for a
 * (distance,offset,period,ext) list
 *)
fun offStepList lst = map (fn(d,off,p,e) => offStep(d,off,p,e,FSMO(lst))) lst

(* offZeros: (int * int * int * 'a)list -> bool
 * Function checking if all offsets are zero
 *)
fun offZeros [] = true
  | offZeros((_,off,_,_)::rest) = off=0 andalso offZeros rest

(* findAndRemoveSmallest: (int * int * int * 'a)list -> (int * int * int list)
 * Gives the element in the list with the smallest relative deadline or offset
 * as well as the list without that element 
 *)
fun findAndRemoveSmallestOff [] = raise EmptyList
  | findAndRemoveSmallestOff [e] = (e,[])
  | findAndRemoveSmallestOff(x::xs) = 
  let val (sm,rest) = findAndRemoveSmallestOff xs 
      val (d1,o1,_,_) = x
      val (d2,o2,_,_) = sm
  in 
    if o1=0 andalso o2=0  
    then 
      if d1>d2 
      then (sm,x::rest)
      else (x,xs)
    else
      if o1=0 andalso o2>0
      then (x,xs)
      else
        if o1>0 andalso o2=0
	then (sm,x::rest)
	else
	  if o1>o2
	  then (sm,x::rest)
	  else (x,xs)
  end
(* sortUListOff: (int * int * int * 'a)list -> (int * int * int * 'a) list
 * Sorts the list according to relative deadlines and offsets
 *)
fun sortUListOff xs = 
  let val (sm,rest) = findAndRemoveSmallestOff xs 
  in 
    if rest = [] 
    then [sm] 
    else sm::sortUListOff rest 
  end

(* getExtOff: (_, _, 'a) -> 'a
 * Gets the fourth element in a 4-tuple
 *) 
fun getExtOff(_,_,_,ext) = ext

(* mkPrioOff: (int * int * int * 'a)list -> 'a list 
 * Makes priorities for a given time step during the offset in 
 * the external representation ('a)
 *)
fun mkPrioOff xs = map getExtOff (sortUListOff xs)

(* mkOffUListsAux ((int * int * int * 'a)list * int list * 'a list list) ->
 *   (int list * 'a list list)
 * 
 * Auxilary function for 'mkOffULists' collecting time step sizes in 'As' 
 * and a list of priorities in 'prios' during offset

 *)
fun mkOffUListsAux(lst,As,prios) =
      if offZeros lst
      then (rev As,rev prios,lst)
      else mkOffUListsAux(offStepList lst, FSMO lst::As, mkPrioOff lst::prios)

(* mkOffULists: (int * int * 'a)list -> (int list * 'a list list)
 * Function for creating offset urgency lists. It takes a list of 
 * elements (o,p,e) where 
 * o is the offset, p is the period and e is the external representation 
 * for a given task 
 *)
fun mkOffULists opeList = mkOffUListsAux(map (fn(off,p,e) => ((if off>0 then off else p),off,p,e)) opeList,[],[])

(* mkP: (int * int * int * 'a) -> (int * int * 'a)
 * Function for making an element for the periodic list from and element
 * of the offset list
 *)
fun mkP (d,_,p,e) = (d,p,e)

(* mkPList: (int * int * int * 'a)list -> (int * int * 'a)list
 * Function for making the periodic list from the offset list
 *)
fun mkPList lst = map mkP lst

local
  (* wh: ('a * int * 'a list) -> int
   * Function finding a placement of an element in a list
   *)
  fun wh (i,_,[]) = raise Empty
    | wh (i,n,x::xs) = if i=x then n else wh(i,n+1,xs)
  (* whList: int list -> int list -> int list
   * Function finding the placements of a list of elements
   *)
  fun whList [] lst = []
    | whList (g::gs) lst = wh(g,1,lst)::whList gs lst
  (* trans: int list -> int list list
   * Function translating a list of priorities to their global ids
   *)
  fun trans gl pr = map (whList gl) pr
  (* gl: 'a list -> 'a -> int
   * Function finding the placement of a global id in a priority list
   *)
  fun gl gls s = wh(s,1,gls)
in
  (* transPList: 'a list list * 'a list -> int list list
   * Function translating a list of priorities in the external
   * representation to a list of global ids
   *)
  fun transPList(pris,gls) = trans (map (gl gls) gls) (map (map (gl gls)) pris)
end

(* mkBothULists: (int * int * 'a)list -> 
 *   (int list * int list list) * (int list * int list list)
 * Function for making the offset urgency list and the periodic
 * urgency list from a list of 3-tuple elements (o,p,e), where o 
 * is the offset, p is the period and e is the external 
 * representation for each task
 *)
fun mkBothULists opeList gls opt =
  let val (ots,ops,lst) = mkOffULists opeList
      val (optts, optps) = sumOptULists(0,(ots,ops),opt)
      val lalie = if(List.length optts>0) then List.last optts else 0
      val plst = mkPList lst
      val uplst = mkULists(plst)
      val (perts,perps) = sumOptULists(lalie, uplst, opt)
      val tpolist = transPList(optps,gls)
      val tpper = transPList(perps,gls)
  in ((optts,tpolist),(perts,tpper))
  end

fun intStringList [] = raise EmptyList
  | intStringList [h] = Int.toString(h)
  | intStringList (h::t) = Int.toString(h)^","^intStringList t

local
  fun strRepT [] = ""
    | strRepT [t] = Int.toString t
    | strRepT(t::ts) = Int.toString t ^ "," ^ strRepT ts
  fun strRepP [] = ""
    | strRepP [p] = strRepT p
    | strRepP(p::ps) = strRepT p ^ "},{" ^ strRepP ps
in
  fun strRep ((ots,ops),(pts,pps)) = let val mostep = if(length ots>0) then List.nth(ots,((length ots)-1)) else 0
					 val offsteps = if(length ots>0) then strRepT ots else "0"
					 val offprios = if(length ots>0) then strRepP ops else intStringList(hd pps)
				     in
					 "int[1,MN] pri[MN] = {"^intStringList(if(length ops>0) then hd ops else hd pps)^"}; //EDF scheduling priorities\n\nconst int NRSteps="^Int.toString(length pts)^", NROffSteps="^(if(length ots>0) then Int.toString(length ots) else "1")^", MAXOffStep="^Int.toString(mostep)^", MAXStep="^Int.toString(List.nth(pts,(length(pts)-1)))^";\n\nconst int[0,MAXOffStep] OffSteps[NROffSteps] = {" ^ offsteps ^ "};\nconst int[1,MN] OffPrios[NROffSteps][MN] = {{" ^ offprios ^ "}};\n\nconst int[0,MAXStep] Steps[NRSteps] = {" ^ strRepT pts ^ "};\nconst int[1,MN] Prios[NRSteps][MN] = {{" ^ strRepP pps ^ "}};\n\n"
				     end
end

fun mkGlList [] = []
  | mkGlList(t::ts) = getTName t::mkGlList((ts)) 

fun mkOList([]) = []
  | mkOList(t::ts) = (getO t, getPi t, getTName t)::mkOList((ts))

fun mkDynPri(app,opt) =
  let val glist = mkGlList app
      val olist = mkOList app
      val blists = mkBothULists olist glist opt
  in
      strRep blists
  end

fun mxExe ([],m) = m
  | mxExe (t::rest,m) = if getWC t>m then mxExe(rest,getWC t) else mxExe(rest,m)

fun mxPi ([],m) = m
  | mxPi (t::rest,m) = if getPi t>m then mxPi (rest,getPi t) else mxPi (rest,m)

fun mkDeclText((plat,app,mp,dp),opt) = "const int M = "^Int.toString(length plat)^";\nconst int N = "^Int.toString(maxTonP(plat,app,mp,dp))^";\nconst int MN = "^Int.toString(length app)^";\n\nconst int[FP,EDF] processorScheduling[M] = {"^(mkProcSch plat)^"};\nconst int[0,MN] onPE[M][N] = "^mkOnPEText(plat,app,mp,dp)^"const int fpris[MN] = {"^mkFPris(1,app)^"};\nconst int pi[MN] = {"^mkPi app^"};\nconst int offset[MN] = {"^mkO app^"};\n\nconst bool origdep[MN][MN] = "^mkDepend(app,dp)^"\nbool depend[MN][MN] = "^mkDepend(app,dp)^"\n"^mkDynPri(app,opt)^"const int MaxExe="^Int.toString(mxExe(app,0))^";\nconst int MaxPi="^Int.toString(mxPi(app,0))^";\n\n"

fun extractTs [] = []
  | extractTs(t::rest) = getTName t::extractTs(rest)

fun mkSysDeclP(_,[]) = ""
  | mkSysDeclP(i,p::rest) = "Con"^Int.toString(i)^" = Control("^Int.toString(i)^");\nSyn"^Int.toString(i)^" = Synchronizer("^Int.toString(i)^");\nSch"^Int.toString(i)^" = Scheduler("^Int.toString(i)^");\n\n"^mkSysDeclP(i+1,rest)

fun mkSysDeclPInit(plat) = mkSysDeclP(1,plat)


fun mkSysDeclA(_,[],_,_) = "\n"
  | mkSysDeclA(i,t::rest,(mp:mapping),plat) = getTName(t)^" = Task("^Int.toString(getPIndex(1,(getPforT(getTName t,mp)),plat))^", "^Int.toString(i)^", "^Int.toString(getBC t)^", "^Int.toString(getWC t)^");\n"^mkSysDeclA(i+1,rest,mp,plat)

fun mkSysDeclAInit(app,mp,plat) = mkSysDeclA(1,app,mp,plat)

fun mkSysDeclEndA(_,[]) = ""
  | mkSysDeclEndA(i,t::rest) = getTName(t)^", "^mkSysDeclEndA(i+1,rest)

fun mkSysDeclEndP(_,[]) = ""
  | mkSysDeclEndP(i,p::rest) = "Con"^Int.toString(i)^", "^"Syn"^Int.toString(i)^", "^"Sch"^Int.toString(i)^", "^mkSysDeclEndP(i+1,rest)

fun mkSysDeclEnd(app,plat) = "system "^ mkSysDeclEndA(1,app) ^ mkSysDeclEndP(1,plat) ^ "DynPri;\n"

fun mkFullSysDecl(plat,app,mp,dp) = mkSysDeclPInit(plat) ^ mkSysDeclAInit(app,mp,plat) ^ mkSysDeclEnd(app,plat)

fun collectPre(is) = let val line = TextIO.inputLine is
		     in if(line="//System-Dependent Decl\n") then "" else line ^"\n"^collectPre is
		     end

fun collectRealMid(is) = let val line = TextIO.inputLine is
			 in if(line="//System-Dependent Inst\n") then "" else line ^collectRealMid is
			 end

fun collectMid(is) = let val line = TextIO.inputLine is
		     in if(line="//System-Independent Decl\n") then collectRealMid(is) else collectMid(is)
		     end

fun collectRealEnd(is) = let val line = TextIO.inputLine is
			 in if(TextIO.endOfStream is) then line else line ^collectRealEnd is
			 end

fun collectEnd(is) = let val line = TextIO.inputLine is
		     in if(line="//System-Independent Inst\n") then collectRealEnd(is) else collectEnd(is)
		     end

fun readModel(filename) = let val is = TextIO.openIn filename
			      val pre = collectPre(is)
			      val middle = collectMid(is)
			      val ending = collectEnd(is)
			  in (pre,middle,ending)
			  end

fun collectFullModel(filename, S sys, opt) = let val (pre,middle,ending) = readModel filename
				     in pre ^ "//System-Dependent Decl\n" ^ mkDeclText(sys,opt) ^ "//System-Independent Decl\n" ^ middle ^ "//System-Dependent Inst\n" ^ mkFullSysDecl sys ^ "//System-Independent Inst\n" ^ ending
				     end

fun mkFullModel(infile,sys,outfile,opt) = let val os = TextIO.openOut outfile
				      in 
					  (TextIO.output(os,collectFullModel(infile,sys,opt)) ; TextIO.flushOut os)
				      end

fun getBusName(B(n,_,_)) = n

fun getBusSpeed(B(_,_,s)) = s

fun transBustoP(B(n,a,s)) = P(n,FP)

fun tMtoPplat(pes,bus) = transBustoP bus::pes

fun findCet (_,_,[]) = raise mappingError 
| findCet(t,p,(tn,pn,bc,wc)::rest) = if t=tn andalso p=pn 
				       then (bc,wc) 
				       else findCet(t,p,rest)

fun findet (_,[],_) = raise noSuchT
  | findet(n,(t,p)::rest,chr) = if n=t 
				then findCet(t,p,chr)
				else findet(n,rest,chr)

fun tMtoPtask (MT(n,p,off),m,chrs) = let val (bc,wc) = findet(n,m,chrs)
				     in T(n,bc,wc,p,off)
				     end

fun findMT(_,[]) = raise noSuchT 
  | findMT(tn,MT(n,p,off)::rest) = if tn=n then MT(n,p,off) else findMT(tn,rest)

fun getPerforT(tn,mapp) = let val MT(_,p,_) = findMT(tn,mapp)
			  in p
			  end

fun getOffforT(tn,mapp) = let val MT(_,_,off) = findMT(tn,mapp)
			  in off
			  end

fun tMdep (_,[],_,_) = []
  | tMdep (mapp,(t1,t2,d)::rest,m,(x,b)) = if d=0 orelse getPforT(t1,m)=getPforT(t2,m) then (tMdep(mapp,rest,m,(x,b))) else T(t1^"_"^t2,d div (getBusSpeed b),d div (getBusSpeed b),getPerforT(t1,mapp),getOffforT(t1,mapp))::tMdep(mapp,rest,m,(x,b))

fun tMmap ([],_,_) = [] 
  | tMmap ((t1,t2,d)::rest,m,(x,b)) = if d=0 orelse getPforT(t1,m)=getPforT(t2,m) then tMmap(rest,m,(x,b)) else (t1^"_"^t2,getBusName b)::tMmap(rest,m,(x,b))

fun tMtoPapp ([],_,_) = []
  | tMtoPapp (t::rest,m,chrs) = (tMtoPtask(t,m,chrs)::tMtoPapp(rest,m,chrs))

fun tMtoPdep ([],_)  = []
  | tMtoPdep ((t1,t2,d)::rest,m) = if d=0 orelse getPforT(t1,m)=getPforT(t2,m) then (t1,t2)::tMtoPdep(rest,m) else (t1,t1^"_"^t2)::(t1^"_"^t2,t2)::tMtoPdep(rest,m)

fun transMtoS(M(mpl,(mapp,mdep),m,chrs,prop)) = let val p = tMtoPplat mpl
						    val a = tMtoPapp(mapp,m,chrs)@tMdep(mapp,mdep,m,mpl)
						    val d = tMtoPdep (mdep,m)
						    val ms = m @ tMmap(mdep,m,mpl)
						in (S(p,a,ms,d),prop)
						end
						
fun mkModelFromFile(infile,systemfile,outfile,opt) = let val os = TextIO.openOut outfile
							 val (psys,_) = transMtoS(parsef systemfile)
							 val cfm = collectFullModel(infile,psys,opt)
				      in 
					  (TextIO.output(os,cfm) ; TextIO.flushOut os)
				      end

fun mkQuery(queryfile,systemfile) = let val os = TextIO.openOut queryfile
					val (_,prop) = transMtoS(parsef systemfile)
			 in 
				case prop of
				    Schedule => (TextIO.output(os,"A[]!missedDeadline"); TextIO.flushOut os)
				  | Trace => (TextIO.output(os,"E<>missedDeadline"); TextIO.flushOut os)
			 end

fun printFullModel(infile,sys,opt) = print (collectFullModel(infile,sys,opt));


(*
val P1 = P("p1",RM)
val P2 = P("p2",EDF)
val plat = [P1,P2]
val T1 = T("t1",2,2,4,0)
val T2 = T("t2",2,2,6,0)
val T3 = T("t3",2,2,6,0)
val T4 = T("t4",2,3,6,4)
val app = [T1,T2,T3,T4]
val M = fn "t1" => "p1"
	     | "t2" => "p1"
	     | "t3" => "p2"
	     | "t4" => "p2"
	     | _ => ""

val D = [("t2","t3")]

val sys = S(plat,app,M,D);
*)

(*
val _ = printFullModel("testTemplate.xml",sys,"U")
*)

(*
mkModelFromFile("testTemplate.xml","testSystemSmallNoOffset.mvs","sysSmallNoOffset.xml","U");
mkModelFromFile("testTemplateSW.xml","testSystemSmallNoOffset.mvs","sysSmallNoOffsetSW.xml","U");

mkModelFromFile("testTemplate.xml","testSystemSmall.mvs","sysSmall.xml","U");
mkModelFromFile("testTemplateSW.xml","testSystemSmall.mvs","sysSmallSW.xml","U");
*)

(* function handeling arguments *)
fun main() = 
case CommandLine.arguments () of
(arg1::arg2::arg3::l) => 
  let val pre = if ((size(arg3)>4) andalso substring(arg3,size(arg3)-4,4)=".xml") then substring(arg3,0,size(arg3)-4) else arg3
  in 
  (mkModelFromFile(arg2,arg1,pre^".xml","U"); mkQuery(pre^".q",arg1))
  end
| _ => print "Usage: modelgen input_system system_template output_filename) \n\n"

val _ = main();


