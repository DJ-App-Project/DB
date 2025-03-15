
use("djSuggestions");

const songsData = db.songs.find().toArray(); 


use("DJSuggestionsDB");

if (songsData.length > 0) {
    db.songs.insertMany(songsData); 
    print("✅ Songs collection moved successfully!");
}


use("djSuggestions");
db.songs.drop(); 

print("✅ Old songs collection removed!");
