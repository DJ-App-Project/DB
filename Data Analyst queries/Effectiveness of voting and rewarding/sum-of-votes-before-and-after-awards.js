use('DJSuggestionsDB');

db.DJEvent.aggregate([
    { "$unwind": "$MusicConfig.MusicPlaylist" },
    {
      "$group": {
        "_id": null,
        totalVotesBefore: {
          "$sum": {
            "$cond": [{ "$lt": ["$MusicConfig.MusicPlaylist.Votes", 10] }, 1, 0]
          }
        },
        totalVotesAfter: {
          "$sum": {
            "$cond": [{ "$gte": ["$MusicConfig.MusicPlaylist.Votes", 10] }, 1, 0]
          }
        }
      }
    }
  ])
  