+!start(Id,P)
   <- makeArtifact(Id, "auction_env.AuctionArtifact", [], ArtId);
      .print("Auction artifact created for ",P);
      .print("ARTID =  ",ArtId);
      Id::focus(ArtId);  // place observable properties of this auction in a particular name space
      Id::start(P);
      .broadcast(achieve,focus(Id));  // ask all others to focus on this new artifact
      .send(python, achieve, focus(Id));
      .at("now + 5 seconds", {+!decide(Id)}).

+!decide(Id)
   <- Id::stop.

+NS::winner(W) : W \== no_winner
   <- ?NS::task(S);
      ?NS::best_bid(V);
      .print("Winner for ", S, " is ",W," with ", V).













// !start. // initial goal
//
// +!start
//    <- .wait(4000);
//       start("flight_ticket(paris,athens,15/12/2015)");
//       .at("now + 10 seconds", {+!decide}).
//
// +!decide
//    <- stop.
//
// +winner(W) : W \== no_winner
//    <- ?task(S);
//       ?best_bid(V);
//       .print("Winner for ", S, " is ",W," with ", V).

{ include("$jacamoJar/templates/common-cartago.asl") }
{ include("$jacamoJar/templates/common-moise.asl") }
{ include("$jacamoJar/templates/org-obedient.asl") }