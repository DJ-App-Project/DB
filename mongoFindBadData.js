db.DJEvent.find({
    "MusicConfig.MusicPlaylist": {
      $elemMatch: {
        $or: [
          { IsUserRecommentaion: true, RecommenderID: "" },
          { IsUserRecommentaion: false, RecommenderID: { $in: ["UserID", "GuestID"] } }
        ]
      }
    }
  }).count()
  

//Še query verzija

// [
//   {
//     $unwind:
//       /**
//        * path: Path to the array field.
//        * includeArrayIndex: Optional name for index.
//        * preserveNullAndEmptyArrays: Optional
//        *   toggle to unwind null and empty values.
//        */
//       {
//         path: "$MusicConfig.MusicPlaylist"
//       }
//   },
//   {
//     $match:
//       /**
//        * query: The query in MQL.
//        */
//       {
//         $or: [
//           {
//             "MusicConfig.MusicPlaylist.IsUserRecommentaion": true,
//             "MusicConfig.MusicPlaylist.RecommenderID":
//               ""
//           },
//           {
//             "MusicConfig.MusicPlaylist.IsUserRecommentaion": false,
//             "MusicConfig.MusicPlaylist.RecommenderID":
//               {
//                 $in: ["UserID", "GuestID"]
//               }
//           }
//         ]
//       }
//   },
//   {
//     $count:
//       /**
//        * Provide the field name for the count.
//        */
//       "badMusicRecommendations"
//   }
// ]
