CREATE TABLE User (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  age INT NOT NULL,
  link TEXT NOT NULL,
  gender TEXT NOT NULL
);

CREATE TABLE Activity (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id TEXT NOT NULL,
  name TEXT NOT NULL,
  day TEXT NOT NULL,
  hours TEXT NOT NULL,
  x REAL NOT NULL,
  y REAL NOT NULL,
  FOREIGN KEY(user_id) REFERENCES User(id)
);

