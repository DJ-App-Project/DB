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
    {
      "$project": {
        "Username": 1,
        "VotesBeforeReward": {
          "$size": {
            "$filter": {
              "input": "$VotedEvents",
              "as": "event",
              "cond": { "$lt": ["$$event.CreatedAt", ISODate("2024-03-01T00:00:00Z")] }
            }
          }
        },
        "VotesAfterReward": {
          "$size": {
            "$filter": {
              "input": "$VotedEvents",
              "as": "event",
              "cond": { "$gte": ["$$event.CreatedAt", ISODate("2024-03-01T00:00:00Z")] }
            }
          }
        }
      }
    }
  ])
  