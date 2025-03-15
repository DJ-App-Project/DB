use('DJSuggestionsDB');

db.Songs.aggregate([
    {
      $group: {
        _id: "$Genre",
        totalSongs: { $sum: 1 }
      }
    },
    { $sort: { totalSongs: -1 } },
    { $limit: 5 }
  ])
  
  