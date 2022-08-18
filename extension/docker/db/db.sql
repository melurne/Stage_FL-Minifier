CREATE TABLE IF NOT EXISTS tests
(
    id INT PRIMARY KEY NOT NULL,
    elem VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS batch
(
    id INT PRIMARY KEY NOT NULL,
    ver DATE
);

CREATE TABLE IF NOT EXISTS tests_batch 
(
    test INT FOREIGN KEY REFERENCES tests(id),
    batch INT FOREIGN KEY REFERENCES batch(id)
);

CREATE TABLE IF NOT EXISTS lists
(
    id INT PRIMARY KEY,
    nom VARCHAR(100),
    ver DATE
);

CREATE TABLE IF NOT EXISTS lists_tests
(
    list INT FOREIGN KEY REFERENCES lists(id),
    test INT FOREIGN KEY REFERENCES tests(id)
);

CREATE TABLE IF NOT EXISTS users
(
    id INT PRIMARY KEY NOT NULL,
    current JSON
);

CREATE TABLE IF NOT EXISTS diffs
(
    user INT FOREIGN KEY REFERENCES users(id),
    stamp TIMESTAMP,
    additions JSON,
    removed JSON
);