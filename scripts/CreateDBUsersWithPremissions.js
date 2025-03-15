
use("admin")

db.getSiblingDB("DJSuggestionsDB").createUser(
  {
    user: "DavidNovak",
    pwd: 'Novak2025',
    roles: [{ role: "readWrite", db: "DJSuggestionsDB" }],
  }
)
db.getSiblingDB("DJSuggestionsDB").createUser(
  {
    user: "JureKozar",
    pwd: 'Kozar2025',
    roles: [{ role: "readWrite", db: "DJSuggestionsDB" }],
  }
)
db.getSiblingDB("DJSuggestionsDB").createUser(
  {
    user: "MatejKlemencic",
    pwd: 'Klemencic2025',
    roles: [{ role: "readWrite", db: "DJSuggestionsDB" }],
  }
)
db.getSiblingDB("DJSuggestionsDB").createUser(
  {
    user: "JulianBreznik",
    pwd: 'Breznik2025',
    roles: [{ role: "readWrite", db: "DJSuggestionsDB" }],
  }
)
