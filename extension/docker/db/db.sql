DROP TABLE IF EXISTS tests CASCADE;
DROP TABLE IF EXISTS batch CASCADE;
DROP TABLE IF EXISTS tests_batch CASCADE;
DROP TABLE IF EXISTS lists CASCADE;
DROP TABLE IF EXISTS lists_tests CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS diffs CASCADE;
DROP TABLE IF EXISTS listoflists CASCADE;
DROP TABLE IF EXISTS listoflists_lists CASCADE;

CREATE TABLE tests
(
    id SERIAL PRIMARY KEY NOT NULL,
    elem VARCHAR(100)
);

CREATE TABLE batch
(
    id SERIAL PRIMARY KEY NOT NULL,
    ver DATE
);

CREATE TABLE tests_batch 
(
    test SERIAL REFERENCES tests(id),
    batch SERIAL REFERENCES batch(id)
);

CREATE TABLE lists
(
    id SERIAL PRIMARY KEY NOT NULL,
    nom VARCHAR(100),
    ver DATE
);

CREATE TABLE listoflists 
(
    id SERIAL PRIMARY KEY NOT NULL
);

CREATE TABLE listoflists_lists
(
    id SERIAL NOT NULL,
    list SERIAL REFERENCES lists(id),
    CONSTRAINT lol_id PRIMARY KEY (id, list)
);

CREATE TABLE lists_tests
(
    list SERIAL REFERENCES lists(id),
    test SERIAL REFERENCES tests(id)
);

CREATE TABLE users
(
    id SERIAL PRIMARY KEY NOT NULL,
    extensionID VARCHAR(100),
    current SERIAL REFERENCES listoflists(id)
);

CREATE TABLE diffs
(
    userID SERIAL REFERENCES users(id),
    stamp VARCHAR(100) NOT NULL,
    CONSTRAINT identifier PRIMARY KEY (userID, stamp),
    additions SERIAL REFERENCES listoflists(id),
    removed SERIAL REFERENCES listoflists(id)
);

INSERT INTO listoflists DEFAULT VALUES;
INSERT INTO users(extensionID, current) VALUES ('extension', currval('listoflists_id_seq'));

INSERT INTO tests(elem) VALUES ('<img id="test0"/>');
INSERT INTO tests(elem) VALUES ('<img id="test1"/>');
INSERT INTO tests(elem) VALUES ('<img id="test2"/>');
INSERT INTO tests(elem) VALUES ('<img id="test3"/>');
INSERT INTO tests(elem) VALUES ('<img id="test4"/>');

INSERT INTO lists(nom, ver) VALUES ('L1', now());
INSERT INTO lists(nom, ver) VALUES ('L2', now());
INSERT INTO lists(nom, ver) VALUES ('L3', now());

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

INSERT INTO batch(ver) VALUES (now());

INSERT INTO tests_batch VALUES (1, 1);
INSERT INTO tests_batch VALUES (2, 1);
INSERT INTO tests_batch VALUES (3, 1);
INSERT INTO tests_batch VALUES (4, 1);
INSERT INTO tests_batch VALUES (5, 1);