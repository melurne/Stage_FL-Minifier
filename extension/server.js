const express = require("express");
const cors = require("cors");
var app = express();
app.use(cors());

const rules = {classNames: ["ad-boxes", "hey", "AdBar"]};

//const rules = {classNames: Array(200).map(i => {i = "ad-boxes"})};

app.get('/rules', (req, res) => {
	res.send(rules);
});

app.get('/scripts/:className', (req, res) => {
	console.log(req.params.className);
	//res.send("Fetched" + req.params.className);
	res.send("<img id=" + req.params.className + ">")
});

app.listen(8080, () => {
	console.log("Running on localhost:8080");
});
