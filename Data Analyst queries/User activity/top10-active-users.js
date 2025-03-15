use('DJSuggestionsDB');

db.User.aggregate([
    {
      $lookup: {
        from: "DJEvent",
        localField: "ID",
        foreignField: "DJID",
        as: "UserEvents"
      }
    },
    {
      $project: {
        "_id": 0,
        "Username": 1
      }
    },
    { "$sort": { "TotalEvents": -1 } },
    { "$limit": 10 }
  ])
  