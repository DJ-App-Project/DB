use('DJSuggestionsDB');

db.GuestUser.aggregate([
    {
      "$lookup": {
        "from": "DJEvent",
        "localField": "ID",
        "foreignField": "MusicConfig.MusicPlaylist.VotersIDs",
        "as": "VotedEvents"
      }
    },
    { "$sort": { "TotalVotesAfterReward": -1 } },
    { "$limit": 5 }
  ])
  