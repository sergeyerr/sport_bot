CREATE TABLE User (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  username TEXT NOT NULL,
  age INT NOT NULL,
  gender TEXT NOT NULL,
  city TEXT NOT NULL,
  x REAL NOT NULL,
  y REAL NOT NULL
);

CREATE TABLE Activity (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  type TEXT NOT NULL, -- (Бег, Велопрогулка..)
  distance REAL NOT NULL, -- (5km, 0.7km..)
  date DATETIME NOT NULL,
  x REAL NOT NULL,
  y REAL NOT NULL
);

CREATE TABLE Activities (
  activity_id INTEGER NOT NULL,
  user_id INTEGER NOT NULL,
  FOREIGN KEY(user_id) REFERENCES User(id),
  FOREIGN KEY(activity_id) REFERENCES Activity(id),
  PRIMARY KEY (activity_id, user_id)
);

CREATE TABLE Buddies (   -- buddy1 has buddy2 in his friends list
  buddy1 INTEGER NOT NULL,
  buddy2 INTEGER NOT NULL,
  FOREIGN KEY(buddy1) REFERENCES User(id),
  FOREIGN KEY(buddy2) REFERENCES User(id),
  PRIMARY KEY (buddy1, buddy2)
);