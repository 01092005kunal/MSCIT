require("dotenv").config();

const express = require("express");
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");

const db = require("./db");
const authenticateToken = require("./middleware/auth");

const app = express();

app.use(express.json());


// REGISTER
app.post("/register", async (req, res) => {
    try {
        const { name, email, password, role } = req.body;

        if (!name || !email || !password) {
            return res.status(400).json({
                message: "Name, email and password are required"
            });
        }

        const [existingUsers] = await db.execute(
            "SELECT id FROM users WHERE email = ?",
            [email]
        );

        if (existingUsers.length > 0) {
            return res.status(409).json({
                message: "User already exists"
            });
        }

        const hashedPassword = await bcrypt.hash(password, 10);

        const [result] = await db.execute(
            "INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)",
            [
                name,
                email,
                hashedPassword,
                role || "student"
            ]
        );

        res.status(201).json({
            message: "User registered successfully",
            userId: result.insertId
        });

    } catch (error) {
        console.error(error);

        res.status(500).json({
            message: "Server error"
        });
    }
});


// LOGIN
app.post("/login", async (req, res) => {
    try {
        const { email, password } = req.body;

        const [users] = await db.execute(
            "SELECT * FROM users WHERE email = ?",
            [email]
        );

        if (users.length === 0) {
            return res.status(401).json({
                message: "Invalid email or password"
            });
        }

        const user = users[0];

        const passwordMatch = await bcrypt.compare(
            password,
            user.password
        );

        if (!passwordMatch) {
            return res.status(401).json({
                message: "Invalid email or password"
            });
        }

        const token = jwt.sign(
            {
                id: user.id,
                role: user.role
            },
            process.env.JWT_SECRET,
            {
                expiresIn: "1h"
            }
        );

        res.json({
            message: "Login successful",
            token: token
        });

    } catch (error) {
        console.error(error);

        res.status(500).json({
            message: "Server error"
        });
    }
});


// PROTECTED PROFILE
app.get("/profile", authenticateToken, async (req, res) => {
    try {
        const [users] = await db.execute(
            "SELECT id, name, email, role, created_at FROM users WHERE id = ?",
            [req.user.id]
        );

        if (users.length === 0) {
            return res.status(404).json({
                message: "User not found"
            });
        }

        res.json({
            user: users[0]
        });

    } catch (error) {
        console.error(error);

        res.status(500).json({
            message: "Server error"
        });
    }
});


// MOCK GOOGLE OAUTH
app.post("/oauth/google", async (req, res) => {
    try {
        const { googleId, name, email } = req.body;

        if (!googleId || !name || !email) {
            return res.status(400).json({
                message: "Google ID, name and email are required"
            });
        }

        const [users] = await db.execute(
            "SELECT * FROM users WHERE google_id = ? OR email = ?",
            [googleId, email]
        );

        let user;

        if (users.length === 0) {

            const [result] = await db.execute(
                `INSERT INTO users
                (name, email, password, role, google_id)
                VALUES (?, ?, ?, ?, ?)`,
                [
                    name,
                    email,
                    "",
                    "student",
                    googleId
                ]
            );

            user = {
                id: result.insertId,
                name,
                email,
                role: "student"
            };

        } else {

            user = users[0];

        }

        const token = jwt.sign(
            {
                id: user.id,
                role: user.role
            },
            process.env.JWT_SECRET,
            {
                expiresIn: "1h"
            }
        );

        res.json({
            message: "Google OAuth login successful",
            user: {
                id: user.id,
                name: user.name,
                email: user.email,
                role: user.role
            },
            token
        });

    } catch (error) {
        console.error(error);

        res.status(500).json({
            message: "Server error"
        });
    }
});


// START SERVER
const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
    console.log(`Auth service running on http://localhost:${PORT}`);
});