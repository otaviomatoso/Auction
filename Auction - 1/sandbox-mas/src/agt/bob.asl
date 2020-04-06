/* Initial beliefs and rules */

/* Initial goals */

/* Plans */
+!start(Id,P)
   <- .print("Agent started").

{ include("$jacamoJar/templates/common-cartago.asl") }
{ include("$jacamoJar/templates/common-moise.asl") }
{ include("$jacamoJar/templates/org-obedient.asl") }
