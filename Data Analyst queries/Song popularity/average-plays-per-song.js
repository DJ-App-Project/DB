use('DJSuggestionsDB');

db.DJEvent.aggregate([
    { "$unwind": "$MusicConfig.MusicPlaylist" },
    {
      "$group": {
        "_id": null,
        "AvgPlaysPerSong": { "$avg": "$MusicConfig.MusicPlaylist.Votes" }
      }
    }
  ])
  