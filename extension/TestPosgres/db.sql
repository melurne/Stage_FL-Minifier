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
    test INT REFERENCES tests(id),
    batch INT REFERENCES batch(id)
);

CREATE TABLE IF NOT EXISTS lists
(
    id INT PRIMARY KEY NOT NULL,
    nom VARCHAR(100),
    ver DATE
);

CREATE TABLE IF NOT EXISTS lists_tests
(
    list INT REFERENCES lists(id),
    test INT REFERENCES tests(id)
);

CREATE TABLE IF NOT EXISTS users
(
    id INT PRIMARY KEY NOT NULL,
    current JSON
);

CREATE TABLE IF NOT EXISTS diffs
(
    userID INT REFERENCES users(id),
    stamp TIMESTAMP NOT NULL,
    CONSTRAINT identifier PRIMARY KEY (userID, stamp),
    additions JSON,
    removed JSON
);

CREATE TABLE IF NOT EXISTS versions
(
    id INT PRIMARY KEY NOT NULL,
    list INT REFERENCES lists(id),
    ver DATE
);

CREATE TABLE IF NOT EXISTS tests_versions
(
    test INT REFERENCES tests(id),
    versions INT REFERENCES versions(id)
);


-- Get test batch query

-- SELECT tests.elem FROM tests
-- JOIN tests_batch ON tests.id = tests_batch.test
-- JOIN batch ON batch.id = tests_batch.batch
-- JOIN (
--     select max(ver) as MaxDate
--     from batch
-- ) tm on batch.ver = tm.MaxDate