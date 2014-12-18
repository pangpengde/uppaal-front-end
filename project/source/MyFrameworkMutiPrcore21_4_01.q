//This file was generated from (Academic) UPPAAL 4.1.18 (rev. 5444), November 2013

/*

*/
A[] forall(t:tid_t) not Task(t).Error

/*

*/
simulate 100 [<=20000] {cpuUsed[0],cpuUsed[1],cpuUsed[2],cpuUsed[3]}

/*

*/
Pr[<=5000] (<> forall(i:tid_t) Task(i).Error)

/*

*/
Pr[<=2000] (<> forall(i:tid_t) Task(i).Error)<=0.01

/*

*/
Pr[<=2000] (<> exists (i:tid_t) Task(i).Error)

/*

*/
E[<=200;1000](max:respt[16])

/*

*/
E[<=2000;500](max:respt[4])

/*

*/
Pr[<=200] ( <> Task(18).Running )

/*

*/
Pr[<=200] ( <> Task(20).Running )

/*

*/
Pr[<=200] ( <> Task(18).Running )>=Pr[<=200] ( <> Task(20).Running )

/*

*/
simulate 1 [<=1000] {exec[0],exec[1],exec[2],exec[3],exec[4],exec[5],exec[6],exec[7],exec[8],exec[9],exec[10],exec[11],exec[12],exec[13],exec[14],exec[15],exec[16],exec[17],exec[18],exec[19],exec[20]}
