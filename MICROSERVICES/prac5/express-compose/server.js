const express = require("express");
const mongoose = require("mongoose");

const app = express();
const PORT = 8082;

mongoose.connect("mongodb://mongodb:27017/mydatabase")
.then(() => console.log("MongoDB Connected"))
.catch(err => console.log(err));

app.get("/", (req, res) => {
    res.send("Hello from ExpressJS with MongoDB");
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});