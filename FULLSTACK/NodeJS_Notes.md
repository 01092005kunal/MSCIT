# Node.js Notes

## What is Node.js?

Node.js is an **open-source, cross-platform JavaScript runtime
environment** that allows JavaScript to run **outside the web browser**,
mainly on the server.


Before Node.js: - JavaScript ran only in browsers.

With Node.js: - JavaScript can create servers, APIs, command-line tools,
and real-time applications.


## Why Run-time Environment is used ?

A runtme environment is a platfrom where the code which is already in a compiled form it re compiles and translets it in "Binary"
for the cpu .. so it bassically it an  interpreter , which takes the code and convert it into a binary form 
"So called Translater"



## How Node.js Works

1.  You write JavaScript code.
2.  Node.js executes it using Google's **V8 JavaScript Engine**.
3.  It interacts with the operating system to read files, connect to
    databases, and handle network requests.

## Features

-   Asynchronous & Non-blocking
-   Event-driven
-   Fast (V8 Engine)
-   Cross-platform
-   Single-threaded with Event Loop

## Architecture

``` text
Client
   |
   v
Node.js Server
   |
Event Loop
   |
 +- File System
 +- Database
 +- Network
 +- Other Services
```

## Uses

-   REST APIs
-   Web servers
-   Chat applications
-   Real-time applications
-   Online games
-   Streaming services
-   IoT applications
-   Command-line tools

## Advantages

-   Fast performance
-   JavaScript for frontend and backend
-   Handles many users efficiently
-   Large npm ecosystem
-   Easy to learn

## Disadvantages

-   Not ideal for CPU-intensive tasks
-   Single-threaded
-   Callback complexity (reduced with async/await)

## npm

Initialize:

``` bash
npm init -y
```

Install Express:

``` bash
npm install express
```

Install Axios:

``` bash
npm install axios
```

## Example

``` javascript
const http = require("http");

const server = http.createServer((req, res) => {
    res.write("Hello, Node.js!");
    res.end();
});

server.listen(3000, () => {
    console.log("Server running on port 3000");
});
```

Visit:

    http://localhost:3000

## Interview Questions

**What is Node.js?** A JavaScript runtime environment for server-side
applications.

**What is npm?** Node Package Manager used to install and manage
packages.

**What is Express.js?** A web framework built on Node.js for creating
servers and APIs.

**Is Node.js a programming language?** No. It is a runtime environment.

**Why is Node.js fast?** Because it uses the V8 engine and a
non-blocking event-driven architecture.

## JavaScript vs Node.js

  JavaScript              Node.js
  ----------------------- ---------------------------------
  Programming language    Runtime environment
  Runs in browser         Runs outside browser
  Frontend                Mainly backend
  Manipulates web pages   Builds servers, APIs, CLI tools
  Uses browser APIs       Uses Node APIs
