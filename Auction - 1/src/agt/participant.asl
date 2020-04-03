/* Initial beliefs and rules */
offer(X) :- .random(R) & X = (10*R)+100.

/* Initial goals */

/* Plans */
+!focus(A) // goal sent by the auctioneer
   <- lookupArtifact(A,ToolId);
      focus(ToolId).

+task(D)[artifact_id(AId)] : running(true)[artifact_id(AId)] & offer(X)
   <- bid(X)[artifact_id(AId)].

+winner(W) : .my_name(W) <- .print("I Won!").





// +task(D) : running(true) <- bid(math.random * 100 + 10).
//
// +winner(W) : .my_name(W) <- .print("I Won!").

{ include("$jacamoJar/templates/common-cartago.asl") }
{ include("$jacamoJar/templates/common-moise.asl") }
{ include("$jacamoJar/templates/org-obedient.asl") }
