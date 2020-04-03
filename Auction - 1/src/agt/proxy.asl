/* Initial beliefs and rules */

/* Initial goals */

/* Plans */
+!focus(A) // goal sent by the auctioneer
   <- lookupArtifact(A,ToolId);
      focus(ToolId).

+task(D)[artifact_id(AId)] : running(true)[artifact_id(AId)] & offer(X,_)
   <- bid(X)[artifact_id(AId)].

+winner(W) : .my_name(W) & offer(_,Url)
  <- .print("I Won!")
     .send(Url,tell,result(win));
     .kill_agent(W);
     .
+winner(W) : offer(_,Url) & .my_name(Me) & (W \== Me) & (W \== no_winner)
  <- .print("I Lost!")
     .send(Url,tell,result(loss));
     .kill_agent(Me);
     .

{ include("$jacamoJar/templates/common-cartago.asl") }
{ include("$jacamoJar/templates/common-moise.asl") }
{ include("$jacamoJar/templates/org-obedient.asl") }
