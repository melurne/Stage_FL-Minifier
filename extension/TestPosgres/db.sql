DROP TABLE IF EXISTS tests CASCADE;
DROP TABLE IF EXISTS batch CASCADE;
DROP TABLE IF EXISTS tests_batch CASCADE;
DROP TABLE IF EXISTS lists CASCADE;
DROP TABLE IF EXISTS lists_tests CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS diffs CASCADE;
DROP TABLE IF EXISTS versions CASCADE;
DROP TABLE IF EXISTS tests_versions CASCADE;


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
    extensionID VARCHAR(100),
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

INSERT INTO users VALUES (1, 'extension', '{"current": []}');

INSERT INTO tests VALUES (1, '<img id="test0"/>');
INSERT INTO tests VALUES (2, '<img id="test1"/>');
INSERT INTO tests VALUES (3, '<img id="test2"/>');
INSERT INTO tests VALUES (4, '<img id="test3"/>');
INSERT INTO tests VALUES (5, '<img id="test4"/>');

INSERT INTO lists VALUES (1, 'L1', now());
INSERT INTO lists VALUES (2, 'L2', now());
INSERT INTO lists VALUES (3, 'L3', now());

INSERT INTO lists_tests VALUES (1, 1);
INSERT INTO lists_tests VALUES (1, 2);
INSERT INTO lists_tests VALUES (1, 4);
INSERT INTO lists_tests VALUES (1, 5);

INSERT INTO lists_tests VALUES (2, 1);
INSERT INTO lists_tests VALUES (2, 3);
INSERT INTO lists_tests VALUES (2, 4);

INSERT INTO lists_tests VALUES (3, 2);
INSERT INTO lists_tests VALUES (3, 3);
INSERT INTO lists_tests VALUES (3, 5);

INSERT INTO batch VALUES (1, now());

INSERT INTO tests_batch VALUES (1, 1);
INSERT INTO tests_batch VALUES (2, 1);
INSERT INTO tests_batch VALUES (3, 1);
INSERT INTO tests_batch VALUES (4, 1);
INSERT INTO tests_batch VALUES (5, 1);

-- Get test batch query

-- SELECT ba.id, tests.elem FROM tests
-- JOIN tests_batch ON tests.id = tests_batch.test
-- JOIN batch AS ba ON ba.id = tests_batch.batch
-- WHERE NOT EXISTS (
--   SELECT b.id, b.ver
--   FROM batch AS b
--   WHERE b.ver > ba.ver
-- );