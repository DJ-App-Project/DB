db.DJEvent.updateMany(
    {
      "MusicConfig.MusicPlaylist": {
        $elemMatch: {
          IsUserRecommentaion: false,
          RecommenderID: { $nin: ["", null] }
        }
      }
    },
    {
      $set: { "MusicConfig.MusicPlaylist.$[elem].RecommenderID": "" }
    },
    {
      arrayFilters: [
        {
          "elem.IsUserRecommentaion": false,
          "elem.RecommenderID": { $nin: ["", null] }
        }
      ]
    }
  )
  