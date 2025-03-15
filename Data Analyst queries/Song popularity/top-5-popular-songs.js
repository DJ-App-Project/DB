use ('DJSuggestionsDB');
db.DJEvent.aggregate([
    { "$unwind": "$MusicConfig.MusicPlaylist" },
    {
      "$group": {
        "_id": "$MusicConfig.MusicPlaylist.MusicName",
        "TotalPlays": { "$sum": 1 }
      }
    },
    { "$sort": { "TotalPlays": -1 } },
    { "$limit": 5 }
  ])
  