const express = require("express");
const nodePickle = require("pickle");
const cors = require("cors");

const { Client } = require('pg')
const postgres = new Client();
postgres.connect().then(() => {
    console.log("Succesfully connected to postgres");
});

const redis = require('redis');
redis_client = redis.createClient({url:"redis://queue:6379"});

var app = express();
app.use(cors());
app.use(express.json())

redis_client.connect().then(()=>{
    console.log("Succesfully connected to Redis");
});

app.get('/tests', (req, res) => {
    postgres.query(
        "SELECT ba.id, tests.elem FROM tests\
        JOIN tests_batch ON tests.id = tests_batch.test\
        JOIN batch AS ba ON ba.id = tests_batch.batch\
        WHERE NOT EXISTS (\
        SELECT b.id, b.ver\
        FROM batch AS b\
        WHERE b.ver > ba.ver\
        );",
        (err, docs) => {
            if (err) {
                console.error(err);
                throw err
            }
            res.status(200).json({"tests": docs.rows.map(x => x["elem"])})
        });
});

app.post('/result', (req, res) => {
    redis_client.publish(
        "Queue", 
        JSON.stringify(req.body)
    ).then(() => {
        res.status(200).send("AK");
    });
});

app.get('/current/:id', (req, res) => {
    postgres.query(
        "SELECT users.current FROM users\
        WHERE users.extensionid = '" + req.params.id + "';",
        (err, docs) => {
            if (err) {
                console.error(err);
                throw err
            }
            res.status(200).json(docs.rows[0]["current"]["current"]);
        }
    );
});

app.get('/analytics/:id', (req, res) => {
    postgres.query(
        "SELECT diffs.stamp, diffs.additions, diffs.removed FROM diffs\
        JOIN users ON users.id = diffs.userID\
        WHERE users.extensionID = '" + req.params.id + "'\
        ORDER BY diffs.stamp;\
        ", (err, docs) => {
            if (err) {
                console.error(err);
                throw err
            }
            
            let rawData = docs.rows;
            console.log(req.params.id);
            let lastTest = rawData[0]["additions"]["+"];

            let dataPoints = {};

            dataPoints[rawData[0]["stamp"]] = {
                "state" : Object.assign([], lastTest),
                "diffs" : {"+": [], "-": []}
            }

            rawData.forEach((test, index) => {
                if (index != 0) {
                    for (rm of test["removed"]["-"]) {
                        lastTest = lastTest.filter(l => l != rm);
                    }
                    for (add of test["additions"]["+"]) {
                        lastTest.push(add);
                    }
                    dataPoints[test["stamp"]] = {
                        "state": Object.assign([], lastTest), 
                        "diffs": {"+": test["additions"]["+"], "-": test["removed"]["-"]}
                    };
                }
            });
            res.status(200).json(dataPoints);
    });
});

app.get('/isAlive', (req, res) => {
	res.status(200).send("Alive")
});

app.listen(8080, () => {
	console.log("Running on localhost:8080");
});