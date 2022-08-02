const express = require("express");
const nodePickle = require("pickle");
const cors = require("cors");
const MongoClient = require('mongodb').MongoClient;

const redis = require('redis');
redis_client = redis.createClient({url:"redis://queue:6379"});

var app = express();
app.use(cors());
app.use(express.json())

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

redis_client.connect().then(()=>{
    console.log("Succesfully connected to Redis");
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

app.post('/result', (req, res) => {
    // console.log(req.body)
    // nodePickle.dumps(req.body, data => {
        // pickle.loads(data, function(original) {
        //     console.log("original:", original);
        // });
        redis_client.publish(
            "Queue", 
            JSON.stringify(req.body)
        ).then(() => {
            res.status(200).send("AK");
        });
    // });
});




app.get('/isAlive', (req, res) => {
	res.status(200).send("Alive")
});

app.listen(8080, () => {
	console.log("Running on localhost:8080");
});