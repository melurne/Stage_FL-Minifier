const express = require("express");
const cors = require("cors");
const MongoClient = require('mongodb').MongoClient;

var app = express();
app.use(cors());

mongourl = "mongodb://root:example@database:27017/"
dbname = "test"
let db

MongoClient.connect(mongourl, (err, client) => {
    if (err) {
        console.error(err);
        throw err
    }
    console.log("Succesfully connected to MongoDB");
    db = client.db(dbname);
});

app.get('/tests', (req, res) => {
    db.collection("testElements").find({}).toArray((err, docs) =>{
        if (err) {
            console.error(err);
            throw err
        }
        res.status(200).json(docs)
    });
});

app.get('/isAlive', (req, res) => {
	res.status(200).send("Alive")
});

app.listen(8080, () => {
	console.log("Running on localhost:8080");
});