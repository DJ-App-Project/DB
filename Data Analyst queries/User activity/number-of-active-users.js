use('DJSuggestionsDB');


db.User.countDocuments({ "UpdatedAt": { $gte: ISODate("2024-03-01T00:00:00Z") } })
