# Mockup baze

Table User {
  ID           string
  Name         string
  FamilyName   string
  ImageUrl     string
  Username     string
  Email        string
  Password     string
  CreatedAt    dateTime
  UpdatedAt    dateTime
  DeletedAt    dateTime
}

Table GuestUser {
  ID           string
  Name         string
  Username     string
  Email        string
  CreatedAt    dateTime
  UpdatedAt    dateTime
  DeletedAt    dateTime
}

Table DJEvent {
  ID          string
  DJID        string // UserId Dj je user, ki je prijavljen
  QRCode      string // QRCode kaže na ta Event
  MusicConfig {
    MusicPlaylist   []Music{
      MusicName             string
      Visible               bool
      Votes                 int
      VotersIDs             []string
      IsUserRecommentaion   bool
      RecommenderID         string
    }
    EnableUserRecommendation  bool
  }
}

Table Playlist {
  ID          string
  UserID      string
  MusicList   []string
}
