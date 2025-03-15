use('DJSuggestionsDB');

db.User.find(
    { "UpdatedAt": { $lt: new Date(new Date().setDate(new Date().getDate() - 30)) } },
    { Name: 1, _id: 0 }
  ).sort({ "UpdatedAt": 1 }).limit(10)
  
  