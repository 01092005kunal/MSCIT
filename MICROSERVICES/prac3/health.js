const express = require("express");
const axios = require("axios");

const app = express();
const port = 3000;

// Parse JSON request bodies
app.use(express.json());

// Store health data
let healthdatas = [];

// GET all health records
app.get("/healthtracker", (req, res) => {
    res.send(healthdatas);
});

// POST a new health record
app.post("/healthtracker", (req, res) => {
    const healthdata = {
        id: healthdatas.length + 1,
        title: req.body.title,
        duration: req.body.duration,
    };

    // Send data to Flask server
    axios.post("http://127.0.0.1:5000/todos", {
        task: req.body.title,
        status: "completed",
    })
    .then((response) => {
        console.log("Response from Python server:", response.data);
    })
    .catch((error) => {
        console.error("Error posting to Python server:", error.message);
    });

    // Store locally
    healthdatas.push(healthdata);

    // Send response
    res.status(201).json(healthdata);
});

// Start server
app.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
});