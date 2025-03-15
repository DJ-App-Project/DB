db.DJEvent.updateMany(
    {
      "MusicConfig.MusicPlaylist": {
        $elemMatch: {
          IsUserRecommentaion: true,
          $or: [ { RecommenderID: { $exists: false } }, { RecommenderID: "" } ]
        }
      }
    },
    {
      $set: { "MusicConfig.MusicPlaylist.$[elem].RecommenderID": "DefaultRecommenderID" }
    },
    {
      arrayFilters: [
        {
          "elem.IsUserRecommentaion": true,
          $or: [ { "elem.RecommenderID": { $exists: false } }, { "elem.RecommenderID": "" } ]
        }
      ]
    }
  )

