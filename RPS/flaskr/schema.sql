DROP TABLE IF EXISTS games;

CREATE TABLE games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    computer CHARACTER(1),
    user CHARACTER(1),
    result CHARACTER(1),
    played_on DATE
);