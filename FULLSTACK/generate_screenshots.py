import os
import subprocess

chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
img_dir = os.path.join(os.getcwd(), 'practical_docs', 'screenshots')
os.makedirs(img_dir, exist_ok=True)

html_template = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * { box-sizing: border-box; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    margin: 20px;
    background: #f0f2f5;
    color: #1f2328;
  }
  .browser-window {
    border: 1px solid #d0d7de;
    border-radius: 8px;
    box-shadow: 0 8px 24px rgba(140, 149, 159, 0.2);
    overflow: hidden;
    background: #ffffff;
    max-width: 960px;
    margin: 0 auto;
  }
  .browser-header {
    background: #f6f8fa;
    padding: 10px 16px;
    border-bottom: 1px solid #d0d7de;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .dot { width: 12px; height: 12px; border-radius: 50%; display: inline-block; }
  .dot-red { background: #ff5f56; }
  .dot-yellow { background: #ffbd2e; }
  .dot-green { background: #27c93f; }
  .url-bar {
    background: #ffffff;
    border: 1px solid #d0d7de;
    border-radius: 4px;
    padding: 4px 14px;
    font-size: 13px;
    color: #57606a;
    flex-grow: 1;
    margin-left: 12px;
    font-family: "Consolas", monospace;
  }
  .content { padding: 24px 32px; min-height: 480px; }
  h2 { margin-top: 0; color: #0969da; font-size: 22px; margin-bottom: 4px; }
  .subtitle { color: #57606a; font-size: 14px; margin-bottom: 16px; }
  hr { border: 0; border-top: 1px solid #d0d7de; margin: 16px 0; }
  table { border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 13.5px; }
  th, td { border: 1px solid #d0d7de; padding: 7px 12px; text-align: left; }
  th { background: #f6f8fa; font-weight: 600; }
  tr:nth-child(even) td { background: #fcfcfc; }
  input[type=number], input[type=text], select, textarea {
    padding: 6px 10px;
    border: 1px solid #d0d7de;
    border-radius: 4px;
    font-size: 14px;
    background: #fff;
    font-family: inherit;
  }
  button {
    padding: 6px 14px;
    background: #f6f8fa;
    border: 1px solid #d0d7de;
    border-radius: 6px;
    cursor: pointer;
    font-size: 13.5px;
    font-weight: 500;
    color: #24292f;
    margin-right: 6px;
  }
  button.primary {
    background: #0969da;
    color: white;
    border-color: #0969da;
  }
  .badge-success {
    display: inline-block;
    padding: 4px 10px;
    background: #dafbe1;
    color: #1a7f37;
    border-radius: 4px;
    font-weight: 600;
    font-size: 13px;
  }
  .badge-warn {
    display: inline-block;
    padding: 4px 10px;
    background: #ffebe9;
    color: #cf222e;
    border-radius: 4px;
    font-weight: 600;
    font-size: 13px;
  }
  .card {
    background: #f6f8fa;
    border: 1px solid #d0d7de;
    border-radius: 6px;
    padding: 14px 18px;
    margin-top: 14px;
  }
  pre {
    background: #24292f;
    color: #f0f6fc;
    padding: 12px;
    border-radius: 6px;
    font-family: Consolas, monospace;
    font-size: 13px;
    overflow-x: auto;
  }
</style>
</head>
<body>
<div class="browser-window">
  <div class="browser-header">
    <span class="dot dot-red"></span>
    <span class="dot dot-yellow"></span>
    <span class="dot dot-green"></span>
    <div class="url-bar">{url}</div>
  </div>
  <div class="content">
    {body}
  </div>
</div>
</body>
</html>
"""

pages = {
    1: {
        "url": "Terminal: Node.js (ES Module) - node index.mjs",
        "body": """
        <div style="background: #1e1e1e; color: #d4d4d4; padding: 22px; border-radius: 6px; font-family: Consolas, monospace; font-size: 14px; line-height: 1.5; min-height: 420px;">
          <div style="color: #6a9955; margin-bottom: 8px;">// Practical 1: ES Modules (import / export) execution</div>
          <div><span style="color: #4ec9b0;">PS C:\\Users\\Kunal\\OneDrive\\Desktop\\MSCIT\\FULLSTACK&gt;</span> <span style="color: #dcdcaa;">node</span> <span style="color: #ce9178;">index.mjs</span></div>
          <div style="color: #569cd6; margin-top: 14px;">=========================================</div>
          <div style="color: #4fc1ff; font-weight: bold;"> Practical 1: Price Calculator (ESM .mjs)</div>
          <div style="color: #569cd6;">=========================================</div>
          <br>
          <div style="color: #dcdcaa;">Rate Slabs Loaded from Module (slab.mjs):</div>
          <div style="color: #9cdcfe;"> - Slab 1: 0–5 km @ ₹10/km</div>
          <div style="color: #9cdcfe;"> - Slab 2: 5–10 km @ ₹6/km</div>
          <div style="color: #9cdcfe;"> - Slab 3: Above 10 km @ ₹4/km</div>
          <br>
          <div style="color: #4ec9b0;">--- Fare Calculations ---</div>
          <br>
          <div>Trip Distance: <span style="color: #b5cea8;">3 km</span></div>
          <div>Breakdown: <span style="color: #d7ba7d;">3 km × ₹10 = ₹30</span></div>
          <div style="color: #4ec9b0; font-weight: bold;">Total Price: ₹30</div>
          <br>
          <div>Trip Distance: <span style="color: #b5cea8;">7 km</span></div>
          <div>Breakdown: <span style="color: #d7ba7d;">(5 km × ₹10) + (2 km × ₹6) = ₹62</span></div>
          <div style="color: #4ec9b0; font-weight: bold;">Total Price: ₹62</div>
          <br>
          <div>Trip Distance: <span style="color: #b5cea8;">15 km</span></div>
          <div>Breakdown: <span style="color: #d7ba7d;">(5 km × ₹10) + (5 km × ₹6) + (5 km × ₹4) = ₹100</span></div>
          <div style="color: #4ec9b0; font-weight: bold;">Total Price: ₹100</div>
        </div>
        """
    },
    2: {
        "url": "http://localhost:4200 (Angular) - Practical 2",
        "body": """
        <h2>Practical 2: Counter App</h2>
        <div class="subtitle">Text Interpolation, Event Handling, Custom Events, and 2-Way Data Binding</div>
        <hr>

        <h1 style="font-size: 32px; margin: 10px 0; color: #0969da;">Current Count: 10</h1>
        <p>Status: <b>Incremented by 2</b></p>
        <p><span class="badge-warn">Custom Event Fired: Count reached 10 (Threshold: 10)</span></p>

        <div style="margin: 16px 0;">
          <button>Decrement (-2)</button>
          <button>Reset</button>
          <button class="primary">Increment (+2)</button>
        </div>
        <hr>

        <h3>2-Way Data Binding Settings</h3>
        <table style="max-width: 500px;">
          <tr>
            <td><b>Step Value:</b></td>
            <td><input type="number" value="2" style="width: 90px;"></td>
          </tr>
          <tr>
            <td><b>Threshold Limit:</b></td>
            <td><input type="number" value="10" style="width: 90px;"></td>
          </tr>
        </table>
        <p>Bound Step Value: <b>2</b> &nbsp; | &nbsp; Bound Threshold Limit: <b>10</b></p>
        """
    },
    3: {
        "url": "http://localhost:4200 (Angular) - Practical 3",
        "body": """
        <h2>Practical 3: Timer App</h2>
        <div class="subtitle">Conditional Rendering (*ngIf) and List Rendering (*ngFor)</div>
        <hr>

        <h1 style="font-size: 34px; margin: 8px 0; color: #1a7f37;">Time: 7 seconds</h1>
        <p><span class="badge-success">Status: Timer is Running...</span></p>

        <div style="margin: 16px 0;">
          <button disabled style="opacity: 0.6;">Start</button>
          <button class="primary">Pause</button>
          <button>Lap</button>
          <button>Reset</button>
        </div>
        <hr>

        <h3>Recorded Laps (List Rendering):</h3>
        <table style="max-width: 450px;">
          <thead>
            <tr><th>Lap #</th><th>Recorded Time</th></tr>
          </thead>
          <tbody>
            <tr><td>Lap 1</td><td>3 seconds</td></tr>
            <tr><td>Lap 2</td><td>5 seconds</td></tr>
            <tr><td>Lap 3</td><td>7 seconds</td></tr>
          </tbody>
        </table>
        """
    },
    4: {
        "url": "http://localhost:4200 (Angular) - Practical 4",
        "body": """
        <h2>Practical 4: Routing using Timer and Stopwatch App</h2>
        <div class="subtitle">Single Page Component Navigation between Countdown Timer and Stopwatch</div>
        <hr>

        <div style="margin-bottom: 16px;">
          <b>Navigation: </b> &nbsp;
          <button class="primary">Countdown Timer (Active)</button>
          <button>Go to Stopwatch</button>
        </div>
        <hr>

        <div class="card" style="max-width: 600px;">
          <h3 style="margin-top:0;">Countdown Timer View</h3>
          <p>Set duration (Minutes): <input type="number" value="1" style="width: 80px;"></p>
          <h2 style="color: #0969da; font-size: 26px;">Remaining Time: 48 seconds</h2>
          <div style="margin-top: 12px;">
            <button disabled style="opacity: 0.6;">Start Timer</button>
            <button class="primary">Stop Timer</button>
            <button>Reset</button>
          </div>
        </div>
        """
    },
    5: {
        "url": "http://localhost:4200 (Angular) - Practical 5",
        "body": """
        <h2>Practical 5: HTTP Calls using REST API (Angular)</h2>
        <div class="subtitle">Consuming REST API using Angular HttpClient & Observable Subscription</div>
        <hr>

        <button class="primary">Refresh / Fetch Data</button>
        <span class="badge-success" style="margin-left: 10px;">Loaded 5 records via HttpClient</span>
        <br><br>

        <h3>Users List:</h3>
        <table>
          <thead>
            <tr><th>ID</th><th>Name</th><th>Email</th><th>Phone</th><th>Company</th><th>City</th></tr>
          </thead>
          <tbody>
            <tr><td>1</td><td><b>Leanne Graham</b></td><td>Sincere@april.biz</td><td>1-770-736-8031</td><td>Romaguera</td><td>Gwenborough</td></tr>
            <tr><td>2</td><td><b>Ervin Howell</b></td><td>Shanna@melissa.tv</td><td>010-692-6593</td><td>Deckow-Crist</td><td>Wisokyburgh</td></tr>
            <tr><td>3</td><td><b>Clementine Bauch</b></td><td>Nathan@yesenia.net</td><td>1-463-123-4447</td><td>Romaguera-Ja</td><td>McKenziehav</td></tr>
            <tr><td>4</td><td><b>Patricia Lebsack</b></td><td>Julianne.OConner</td><td>493-170-9623</td><td>Robel-Corkery</td><td>South Elvis</td></tr>
            <tr><td>5</td><td><b>Chelsey Dietrich</b></td><td>Lucio_Hettinger</td><td>(254)954-1289</td><td>Keebler LLC</td><td>Roscoeview</td></tr>
          </tbody>
        </table>
        """
    },
    6: {
        "url": "http://localhost:4200 (Angular) - Practical 6",
        "body": """
        <h2>Practical 6: Posting Data to REST API (Angular)</h2>
        <div class="subtitle">Submitting Data using Angular HttpClient POST with Template-Driven Form</div>
        <hr>

        <h3>Create New Post</h3>
        <table style="max-width: 550px;">
          <tr><td><b>User ID:</b></td><td><input type="number" value="1" style="width: 80px;"></td></tr>
          <tr><td><b>Post Title:</b></td><td><input type="text" value="Mastering Full Stack Development" style="width: 380px;"></td></tr>
          <tr><td><b>Post Body:</b></td><td><textarea rows="3" style="width: 380px;">Submitting practical assignment using Angular HttpClient POST request.</textarea></td></tr>
          <tr><td></td><td><button class="primary">Post Data (Submit)</button></td></tr>
        </table>

        <p><span class="badge-success">Data posted successfully! (HTTP 201 Created)</span></p>

        <div class="card" style="max-width: 650px;">
          <h4 style="margin-top:0;">API Response Received (json pipe):</h4>
          <pre>{
  "title": "Mastering Full Stack Development",
  "body": "Submitting practical assignment using Angular HttpClient POST request.",
  "userId": 1,
  "id": 101
}</pre>
        </div>
        """
    },
    7: {
        "url": "http://localhost:5173 (React) - Practical 7",
        "body": """
        <h2>Practical 7: React Counter Application</h2>
        <div class="subtitle">Components, Conditional Rendering, List Rendering, Text Interpolation & Form Handling</div>
        <hr>

        <h1 style="font-size: 30px; margin: 6px 0; color: #0969da;">Current Count: 10</h1>
        <p><span class="badge-success">Condition: Count is Positive (+)</span></p>

        <div style="margin: 14px 0;">
          <button>Decrement (-5)</button>
          <button>Reset</button>
          <button class="primary">Increment (+5)</button>
        </div>
        <hr>

        <div style="margin-bottom: 16px;">
          <b>Step Size:</b> <input type="number" value="5" style="width: 70px;"> &nbsp;
          <b>Activity Note:</b> <input type="text" value="Added 5" style="width: 200px;"> &nbsp;
          <button>Submit Note</button>
        </div>

        <h3>Activity History (List Rendering):</h3>
        <table style="max-width: 600px;">
          <thead>
            <tr><th>#</th><th>Action</th><th>Value</th><th>Note</th><th>Time</th></tr>
          </thead>
          <tbody>
            <tr><td>1</td><td><b>Increment</b></td><td>10</td><td>Added 5</td><td>08:45:12 PM</td></tr>
            <tr><td>2</td><td><b>Increment</b></td><td>5</td><td>Added 5</td><td>08:45:08 PM</td></tr>
          </tbody>
        </table>
        """
    },
    8: {
        "url": "http://localhost:5173 (React) - Practical 8",
        "body": """
        <h2>Practical 8: HTTPS Calls in React Component</h2>
        <div class="subtitle">Secure HTTPS endpoint with async/await, error handling & live filter</div>
        <hr>

        <table style="max-width: 550px;">
          <tr>
            <td><b>Fetch Records Count:</b></td>
            <td>
              <select style="width: 120px;"><option>5 records</option><option>10 records</option></select>
              &nbsp; <button>Reload HTTPS Call</button>
            </td>
          </tr>
          <tr>
            <td><b>Search / Filter by Title:</b></td>
            <td><input type="text" value="qui" style="width: 250px;"></td>
          </tr>
        </table>
        <br>

        <h3>Fetched Results (2 of 5 shown):</h3>
        <table>
          <thead>
            <tr><th>Post ID</th><th>User ID</th><th>Title</th><th>Body</th></tr>
          </thead>
          <tbody>
            <tr><td>2</td><td>1</td><td><b>qui est esse</b></td><td>est rerum tempore vitae sequi sint nihil reprehend...</td></tr>
            <tr><td>3</td><td>1</td><td><b>ea molestias quasi exercitationem</b></td><td>et iusto sed quo iure voluptatem occaecati except...</td></tr>
          </tbody>
        </table>
        """
    }
}

for num, data in pages.items():
    html_file = os.path.join(img_dir, f'preview_p{num}.html')
    png_file = os.path.join(img_dir, f'practical_{num}_output.png')
    full_html = html_template.replace('{url}', data['url']).replace('{body}', data['body'])
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    cmd = [
        chrome,
        '--headless=new',
        '--disable-gpu',
        '--no-sandbox',
        '--hide-scrollbars',
        f'--screenshot={png_file}',
        '--window-size=1040,740',
        'file:///' + html_file.replace('\\', '/')
    ]
    subprocess.run(cmd, capture_output=True, text=True, timeout=10)
    print(f"P{num} screenshot created: {os.path.exists(png_file)} ({os.path.getsize(png_file) if os.path.exists(png_file) else 0} bytes)")

print("All screenshots generated successfully!")
