import os
import re
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

output_dir = os.path.join(os.getcwd(), 'practical_docs')
img_dir = os.path.join(output_dir, 'screenshots')
os.makedirs(output_dir, exist_ok=True)

KEYWORDS = {
    'import', 'from', 'export', 'default', 'class', 'function', 'return',
    'let', 'const', 'var', 'if', 'else', 'new', 'try', 'catch', 'finally',
    'async', 'await', 'implements', 'interface', 'true', 'false', 'null',
    'undefined', 'typeof', 'void', 'number', 'string', 'boolean', 'any',
    'Component', 'Output', 'EventEmitter', 'OnDestroy', 'useState', 'useEffect',
    'OnInit', 'HttpClient', 'subscribe', 'next'
}

COLOR_KEYWORD = RGBColor(0, 0, 255)      # VS Code Blue #0000FF
COLOR_STRING = RGBColor(163, 21, 21)     # VS Code Red/Brown #A31515
COLOR_COMMENT = RGBColor(0, 128, 0)      # VS Code Green #008000
COLOR_DEFAULT = RGBColor(36, 41, 47)     # Default dark text

def add_code_line(p, line):
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(1.2)
    p.paragraph_format.line_spacing = 1.05
    
    stripped = line.strip()
    if stripped.startswith('//') or stripped.startswith('<!--') or stripped.startswith('*') or stripped.startswith('/*') or stripped.endswith('-->'):
        r = p.add_run(line)
        r.font.name = 'Consolas'
        r.font.size = Pt(9.5)
        r.font.color.rgb = COLOR_COMMENT
        return

    tokens = re.split(r'("(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'|`(?:\\.|[^`\\])*`|\b[a-zA-Z_]\w*\b)', line)
    for tok in tokens:
        if not tok:
            continue
        r = p.add_run(tok)
        r.font.name = 'Consolas'
        r.font.size = Pt(9.5)
        if (tok.startswith('"') and tok.endswith('"')) or (tok.startswith("'") and tok.endswith("'")) or (tok.startswith('`') and tok.endswith('`')):
            r.font.color.rgb = COLOR_STRING
        elif tok in KEYWORDS:
            r.font.color.rgb = COLOR_KEYWORD
            r.font.bold = True
        else:
            r.font.color.rgb = COLOR_DEFAULT

def add_code_box(doc, code_str):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.autofit = False
    tbl.columns[0].width = Inches(6.5)
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.5)

    # Shading (VS Code Light #F6F8FA)
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F6F8FA"/>')
    cell._tc.get_or_add_tcPr().append(shd)

    # Borders (subtle grey #D0D7DE)
    borders = parse_xml(f'''<w:tcBorders {nsdecls("w")}>
        <w:top w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>
        <w:left w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>
        <w:bottom w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>
        <w:right w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>
    </w:tcBorders>''')
    cell._tc.get_or_add_tcPr().append(borders)

    # Padding inside cell
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="120" w:type="dxa"/><w:bottom w:w="120" w:type="dxa"/><w:left w:w="160" w:type="dxa"/><w:right w:w="160" w:type="dxa"/></w:tcMar>')
    cell._tc.get_or_add_tcPr().append(tcMar)

    lines = code_str.split('\n')
    for i, line in enumerate(lines):
        if i == 0:
            p = cell.paragraphs[0]
        else:
            p = cell.add_paragraph()
        add_code_line(p, line)

practicals = [
    {
        "num": 1,
        "title": "Practical No. 1: Price Calculator (ES Modules)",
        "aim": "To implement a Slab-based Price Calculator using JavaScript ES Modules (.mjs) demonstrating export and import statements in Node.js.",
        "code": """// slab.mjs - Defines and exports rate slab definitions
export const slabs = [
  { name: 'Slab 1', minKm: 0, maxKm: 5, rate: 10 },      // 0–5 km: ₹10/km
  { name: 'Slab 2', minKm: 5, maxKm: 10, rate: 6 },      // 5–10 km: ₹6/km
  { name: 'Slab 3', minKm: 10, maxKm: Infinity, rate: 4 } // Above 10 km: ₹4/km
];

export default slabs;

// calc.mjs - Imports slab definitions and exports price calculation logic
import { slabs } from './slab.mjs';

export function calculatePrice(distance) {
  const d = Number(distance) || 0;
  let price = 0;

  if (d <= 0) return 0;

  // Slab 1: 0–5 km -> ₹10/km
  if (d <= 5) {
    price = d * slabs[0].rate;
  }
  // Slab 2: 5–10 km -> ₹6/km
  else if (d <= 10) {
    price = (5 * slabs[0].rate) + (d - 5) * slabs[1].rate;
  }
  // Slab 3: Above 10 km -> ₹4/km
  else {
    price = (5 * slabs[0].rate) + (5 * slabs[1].rate) + (d - 10) * slabs[2].rate;
  }

  return price;
}

export function getBreakdown(distance) {
  const d = Number(distance) || 0;
  if (d <= 0) return 'Distance must be greater than 0';

  if (d <= 5) {
    return `${d} km × ₹${slabs[0].rate} = ₹${d * slabs[0].rate}`;
  } else if (d <= 10) {
    return `(5 km × ₹${slabs[0].rate}) + (${d - 5} km × ₹${slabs[1].rate}) = ₹${calculatePrice(d)}`;
  } else {
    return `(5 km × ₹${slabs[0].rate}) + (5 km × ₹${slabs[1].rate}) + (${d - 10} km × ₹${slabs[2].rate}) = ₹${calculatePrice(d)}`;
  }
}

// index.mjs - Main execution demonstrating ES Module imports
import { slabs } from './slab.mjs';
import { calculatePrice, getBreakdown } from './calc.mjs';

console.log('=========================================');
console.log(' Practical 1: Price Calculator (ESM .mjs)');
console.log('=========================================\\n');

console.log('Rate Slabs Loaded from Module (slab.mjs):');
slabs.forEach((s) => {
  const limit = s.maxKm === Infinity ? 'Above 10 km' : `${s.minKm}–${s.maxKm} km`;
  console.log(` - ${s.name}: ${limit} @ ₹${s.rate}/km`);
});

console.log('\\n--- Fare Calculations ---');
const testDistances = [3, 7, 15];

testDistances.forEach((distance) => {
  console.log(`\\nTrip Distance: ${distance} km`);
  console.log(`Breakdown: ${getBreakdown(distance)}`);
  console.log(`Total Price: ₹${calculatePrice(distance)}`);
});""",
        "output_desc": "The modular program is executed in Node.js ('node index.mjs'). The calculation logic in calc.mjs imports the rate slabs exported by slab.mjs, computes the fare based on distance brackets, and displays formatted breakdowns."
    },
    {
        "num": 2,
        "title": "Practical No. 2: Counter App",
        "aim": "To demonstrate Text Interpolation, Event Handling, Custom Events, and 2-way data binding using a Counter App in Angular.",
        "code": """// prac2-counter.ts
import { Component, EventEmitter, Output } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-prac2-counter',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './prac2-counter.html'
})
export class Prac2CounterComponent {
  // 1. Text Interpolation
  count: number = 0;
  message: string = 'Counter initialized.';

  // 2. Two-way Data Binding
  step: number = 1;
  threshold: number = 10;
  customEventMsg: string = '';

  // 3. Custom Event Output
  @Output() thresholdReached = new EventEmitter<number>();

  checkThreshold(): void {
    if (Math.abs(this.count) >= this.threshold) {
      this.customEventMsg = `Custom Event Fired: Count reached ${this.count} (Threshold: ${this.threshold})`;
      this.thresholdReached.emit(this.count);
    } else {
      this.customEventMsg = '';
    }
  }

  // 4. Event Handlers
  increment(): void {
    this.count += (Number(this.step) || 1);
    this.message = `Incremented by ${this.step}`;
    this.checkThreshold();
  }

  decrement(): void {
    this.count -= (Number(this.step) || 1);
    this.message = `Decremented by ${this.step}`;
    this.checkThreshold();
  }

  reset(): void {
    this.count = 0;
    this.message = 'Counter reset to 0.';
    this.customEventMsg = '';
  }
}

<!-- prac2-counter.html -->
<h2>Practical 2: Counter App</h2>
<p>Concepts: Text Interpolation, Event Handling, Custom Events, and 2-Way Data Binding</p>
<hr>

<!-- 1. Text Interpolation -->
<h3>Current Count: {{ count }}</h3>
<p>Status: {{ message }}</p>
<p *ngIf="customEventMsg"><b>{{ customEventMsg }}</b></p>

<!-- 2. Event Handling -->
<div>
  <button (click)="decrement()">Decrement (-{{ step }})</button>
  <button (click)="reset()">Reset</button>
  <button (click)="increment()">Increment (+{{ step }})</button>
</div>
<hr>

<!-- 3. Two-Way Data Binding -->
<h3>2-Way Data Binding Settings</h3>
<p>Step Value: <input type="number" [(ngModel)]="step"></p>
<p>Threshold Limit: <input type="number" [(ngModel)]="threshold"></p>
<p>Bound Step Value: <b>{{ step }}</b></p>
<p>Bound Threshold Limit: <b>{{ threshold }}</b></p>""",
        "output_desc": "The counter supports variable step increments and decrements via two-way data binding. When the count reaches or crosses the threshold of 10, the custom event is fired and displayed."
    },
    {
        "num": 3,
        "title": "Practical No. 3: Timer App",
        "aim": "To implement Conditional Rendering (*ngIf) and List Rendering (*ngFor) using a Timer App in Angular.",
        "code": """// prac3-timer.ts
import { Component, OnDestroy } from '@angular/core';
import { CommonModule } from '@angular/common';

interface LapItem {
  lapNumber: number;
  time: string;
}

@Component({
  selector: 'app-prac3-timer',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './prac3-timer.html'
})
export class Prac3TimerComponent implements OnDestroy {
  seconds: number = 0;
  isRunning: boolean = false;
  laps: LapItem[] = [];
  private intervalId: any = null;

  startTimer(): void {
    if (!this.isRunning) {
      this.isRunning = true;
      this.intervalId = setInterval(() => {
        this.seconds++;
      }, 1000);
    }
  }

  pauseTimer(): void {
    if (this.isRunning) {
      clearInterval(this.intervalId);
      this.isRunning = false;
    }
  }

  resetTimer(): void {
    this.pauseTimer();
    this.seconds = 0;
    this.laps = [];
  }

  recordLap(): void {
    if (this.seconds > 0) {
      this.laps.push({
        lapNumber: this.laps.length + 1,
        time: `${this.seconds} seconds`
      });
    }
  }

  ngOnDestroy(): void {
    if (this.intervalId) {
      clearInterval(this.intervalId);
    }
  }
}

<!-- prac3-timer.html -->
<h2>Practical 3: Timer App</h2>
<p>Concepts: Conditional Rendering (*ngIf) and List Rendering (*ngFor)</p>
<hr>

<h2>Time: {{ seconds }} seconds</h2>

<!-- 1. Conditional Rendering using *ngIf -->
<div>
  <p *ngIf="isRunning">Status: <b>Timer is Running...</b></p>
  <p *ngIf="!isRunning && seconds > 0">Status: <b>Timer is Paused.</b></p>
  <p *ngIf="!isRunning && seconds === 0">Status: <b>Timer is Reset (Idle).</b></p>
</div>

<!-- Controls -->
<div>
  <button (click)="startTimer()" [disabled]="isRunning">Start</button>
  <button (click)="pauseTimer()" [disabled]="!isRunning">Pause</button>
  <button (click)="recordLap()" [disabled]="!isRunning">Lap</button>
  <button (click)="resetTimer()">Reset</button>
</div>
<hr>

<!-- 2. List Rendering using *ngFor -->
<h3>Recorded Laps (List Rendering)</h3>
<p *ngIf="laps.length === 0">No laps recorded yet. Click 'Lap' while timer is running.</p>

<table border="1" cellpadding="5" *ngIf="laps.length > 0">
  <thead>
    <tr>
      <th>Lap #</th>
      <th>Recorded Time</th>
    </tr>
  </thead>
  <tbody>
    <tr *ngFor="let item of laps">
      <td>Lap {{ item.lapNumber }}</td>
      <td>{{ item.time }}</td>
    </tr>
  </tbody>
</table>""",
        "output_desc": "The timer demonstrates conditional state rendering (*ngIf for running/paused status) and dynamic list rendering (*ngFor for rendering recorded lap times in a table)."
    },
    {
        "num": 4,
        "title": "Practical No. 4: Routing using Timer and Stopwatch App",
        "aim": "To implement Routing and Single Page View Navigation between Countdown Timer and Stopwatch in Angular.",
        "code": """// prac4-routing.ts
import { Component, OnDestroy } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-prac4-routing',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './prac4-routing.html'
})
export class Prac4RoutingComponent implements OnDestroy {
  activeView: 'timer' | 'stopwatch' = 'timer';

  // Countdown Timer State
  inputMinutes: number = 1;
  remainingSeconds: number = 60;
  timerRunning: boolean = false;
  private timerInterval: any = null;

  // Stopwatch State
  stopwatchSeconds: number = 0;
  stopwatchRunning: boolean = false;
  private stopwatchInterval: any = null;

  setView(view: 'timer' | 'stopwatch'): void {
    this.activeView = view;
  }

  // Timer Methods
  startTimer(): void {
    if (!this.timerRunning) {
      if (this.remainingSeconds <= 0) {
        this.remainingSeconds = (this.inputMinutes || 1) * 60;
      }
      this.timerRunning = true;
      this.timerInterval = setInterval(() => {
        if (this.remainingSeconds > 0) {
          this.remainingSeconds--;
        } else {
          this.stopTimer();
          alert('Countdown Finished!');
        }
      }, 1000);
    }
  }

  stopTimer(): void {
    if (this.timerRunning) {
      clearInterval(this.timerInterval);
      this.timerRunning = false;
    }
  }

  resetTimer(): void {
    this.stopTimer();
    this.remainingSeconds = (this.inputMinutes || 1) * 60;
  }

  // Stopwatch Methods
  startStopwatch(): void {
    if (!this.stopwatchRunning) {
      this.stopwatchRunning = true;
      this.stopwatchInterval = setInterval(() => {
        this.stopwatchSeconds++;
      }, 1000);
    }
  }

  pauseStopwatch(): void {
    if (this.stopwatchRunning) {
      clearInterval(this.stopwatchInterval);
      this.stopwatchRunning = false;
    }
  }

  resetStopwatch(): void {
    this.pauseStopwatch();
    this.stopwatchSeconds = 0;
  }

  ngOnDestroy(): void {
    if (this.timerInterval) clearInterval(this.timerInterval);
    if (this.stopwatchInterval) clearInterval(this.stopwatchInterval);
  }
}

<!-- prac4-routing.html -->
<h2>Practical 4: Routing using Timer and Stopwatch App</h2>
<p>Concepts: Single Page Component Navigation between Countdown Timer and Stopwatch</p>
<hr>

<!-- Navigation links -->
<div>
  <b>Navigation: </b>
  <button (click)="setView('timer')" [disabled]="activeView === 'timer'">Go to Countdown Timer</button> |
  <button (click)="setView('stopwatch')" [disabled]="activeView === 'stopwatch'">Go to Stopwatch</button>
</div>
<hr>

<!-- Timer View -->
<div *ngIf="activeView === 'timer'">
  <h3>Countdown Timer View</h3>
  <p>Set duration (Minutes): <input type="number" [(ngModel)]="inputMinutes" min="1"></p>
  <h3>Remaining Time: {{ remainingSeconds }} seconds</h3>
  <div>
    <button (click)="startTimer()" [disabled]="timerRunning">Start Timer</button>
    <button (click)="stopTimer()" [disabled]="!timerRunning">Stop Timer</button>
    <button (click)="resetTimer()">Reset</button>
  </div>
</div>

<!-- Stopwatch View -->
<div *ngIf="activeView === 'stopwatch'">
  <h3>Stopwatch View</h3>
  <h3>Elapsed Time: {{ stopwatchSeconds }} seconds</h3>
  <div>
    <button (click)="startStopwatch()" [disabled]="stopwatchRunning">Start</button>
    <button (click)="pauseStopwatch()" [disabled]="!stopwatchRunning">Pause</button>
    <button (click)="resetStopwatch()">Reset</button>
  </div>
</div>""",
        "output_desc": "Demonstrates client-side view switching without page reload between a configurable Countdown Timer view and a real-time Stopwatch view."
    },
    {
        "num": 5,
        "title": "Practical No. 5: HTTP Calls using REST API (Angular)",
        "aim": "To fetch and display data from a REST API using HTTP GET calls with Angular HttpClient.",
        "code": """// prac5-http.ts
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';

interface User {
  id: number;
  name: string;
  email: string;
  phone: string;
  company: { name: string };
  address: { city: string };
}

@Component({
  selector: 'app-prac5-http',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './prac5-http.html'
})
export class Prac5HttpComponent implements OnInit {
  users: User[] = [];
  loading: boolean = false;
  error: string | null = null;

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.fetchUsers();
  }

  fetchUsers(): void {
    this.loading = true;
    this.error = null;

    this.http.get<User[]>('https://jsonplaceholder.typicode.com/users')
      .subscribe({
        next: (data) => {
          this.users = data;
          this.loading = false;
        },
        error: (err) => {
          this.error = err.message || 'Failed to fetch users';
          this.loading = false;
        }
      });
  }
}

<!-- prac5-http.html -->
<h2>Practical 5: HTTP Calls using REST API (Angular)</h2>
<p>Concepts: Consuming REST API using Angular HttpClient and Observable subscription</p>
<hr>

<button (click)="fetchUsers()">Refresh / Fetch Data</button>
<br><br>

<div *ngIf="loading">
  <p><b>Loading data from API... Please wait.</b></p>
</div>

<div *ngIf="error" style="color: red;">
  <p><b>Error: {{ error }}</b></p>
</div>

<div *ngIf="!loading && !error">
  <h3>Users List ({{ users.length }} records):</h3>
  <table border="1" cellpadding="5">
    <thead>
      <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Email</th>
        <th>Phone</th>
        <th>Company</th>
        <th>City</th>
      </tr>
    </thead>
    <tbody>
      <tr *ngFor="let user of users">
        <td>{{ user.id }}</td>
        <td>{{ user.name }}</td>
        <td>{{ user.email }}</td>
        <td>{{ user.phone }}</td>
        <td>{{ user.company.name }}</td>
        <td>{{ user.address.city }}</td>
      </tr>
    </tbody>
  </table>
</div>""",
        "output_desc": "The Angular component injects HttpClient, issues a GET request to JSONPlaceholder on initialization via ngOnInit, manages loading and error states, and renders records using *ngFor."
    },
    {
        "num": 6,
        "title": "Practical No. 6: Posting Data to REST API (Angular)",
        "aim": "To submit user data to a REST API using HTTP POST in Angular with template-driven form handling.",
        "code": """// prac6-post.ts
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

interface PostResponse {
  id: number;
  title: string;
  body: string;
  userId: number;
}

@Component({
  selector: 'app-prac6-post',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './prac6-post.html'
})
export class Prac6PostComponent {
  userId: number = 1;
  title: string = '';
  body: string = '';
  loading: boolean = false;
  statusMessage: string = '';
  responseResult: PostResponse | null = null;
  postsList: PostResponse[] = [];

  constructor(private http: HttpClient) {}

  handleSubmit(): void {
    if (!this.title.trim() || !this.body.trim()) {
      alert('Please fill all fields.');
      return;
    }

    this.loading = true;
    this.statusMessage = 'Posting data to REST API...';
    this.responseResult = null;

    const payload = {
      title: this.title,
      body: this.body,
      userId: Number(this.userId)
    };

    this.http.post<PostResponse>('https://jsonplaceholder.typicode.com/posts', payload)
      .subscribe({
        next: (res) => {
          this.loading = false;
          this.statusMessage = 'Data posted successfully! (HTTP 201 Created)';
          this.responseResult = res;
          this.postsList.unshift(res);
          this.title = '';
          this.body = '';
        },
        error: (err) => {
          this.loading = false;
          this.statusMessage = 'Error: ' + (err.message || 'Failed to post data');
        }
      });
  }
}

<!-- prac6-post.html -->
<h2>Practical 6: Posting Data to REST API (Angular)</h2>
<p>Concepts: Submitting Data using Angular HttpClient POST with Template-Driven Form</p>
<hr>

<h3>Create New Post</h3>
<form (ngSubmit)="handleSubmit()">
  <table>
    <tr>
      <td>User ID:</td>
      <td><input type="number" [(ngModel)]="userId" name="userId" min="1"></td>
    </tr>
    <tr>
      <td>Post Title:</td>
      <td><input type="text" [(ngModel)]="title" name="title" placeholder="Enter title" size="40"></td>
    </tr>
    <tr>
      <td>Post Body:</td>
      <td><textarea [(ngModel)]="body" name="body" placeholder="Enter body content" rows="4" cols="42"></textarea></td>
    </tr>
    <tr>
      <td></td>
      <td><button type="submit" [disabled]="loading">{{ loading ? 'Submitting...' : 'Post Data (Submit)' }}</button></td>
    </tr>
  </table>
</form>

<br>
<p *ngIf="statusMessage"><b>{{ statusMessage }}</b></p>

<div *ngIf="responseResult">
  <hr>
  <h3>API Response Received:</h3>
  <pre style="background: #eee; padding: 10px;">{{ responseResult | json }}</pre>
</div>

<div *ngIf="postsList.length > 0">
  <hr>
  <h3>Recently Submitted Posts:</h3>
  <table border="1" cellpadding="5">
    <thead>
      <tr>
        <th>Assigned ID</th>
        <th>Title</th>
        <th>Body</th>
        <th>User ID</th>
      </tr>
    </thead>
    <tbody>
      <tr *ngFor="let post of postsList">
        <td>{{ post.id }}</td>
        <td>{{ post.title }}</td>
        <td>{{ post.body }}</td>
        <td>{{ post.userId }}</td>
      </tr>
    </tbody>
  </table>
</div>""",
        "output_desc": "Submits form data to the REST API via Angular HttpClient POST, receives HTTP 201 Created response containing the newly assigned ID, displays response JSON using Angular's json pipe, and appends the post into the submitted items list."
    },
    {
        "num": 7,
        "title": "Practical No. 7: React Counter Application",
        "aim": "To demonstrate Components, Conditional Rendering, List Rendering, Text Interpolation, and Form Handling using the Counter App in React.",
        "code": """// Practical7_ReactCounterApp.jsx
import React, { useState } from 'react';

// Subcomponent 1: Display
function CounterDisplay({ count }) {
    return (
        <div>
            <h2>Current Count: {count}</h2>
            {count > 0 && <p>Condition: <b>Count is Positive (+)</b></p>}
            {count < 0 && <p>Condition: <b>Count is Negative (-)</b></p>}
            {count === 0 && <p>Condition: <b>Count is Zero</b></p>}
            {Math.abs(count) >= 20 && <p><b>Warning: Threshold of 20 exceeded!</b></p>}
        </div>
    );
}

// Subcomponent 2: Controls
function CounterControls({ onIncrement, onDecrement, onReset, step }) {
    return (
        <div>
            <button onClick={onDecrement}>Decrement (-{step})</button>{' '}
            <button onClick={onReset}>Reset</button>{' '}
            <button onClick={onIncrement}>Increment (+{step})</button>
        </div>
    );
}

// Subcomponent 3: Form
function ConfigForm({ step, onStepChange, onAddNote }) {
    const [note, setNote] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        if (note.trim()) {
            onAddNote(note);
            setNote('');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <h3>Form Handling (Step & Log)</h3>
            <p>
                Step Size:
                <input
                    type="number"
                    value={step}
                    onChange={(e) => onStepChange(Number(e.target.value) || 1)}
                    min="1"
                />
            </p>
            <p>
                Activity Note:
                <input
                    type="text"
                    value={note}
                    onChange={(e) => setNote(e.target.value)}
                    placeholder="e.g. Added 5"
                />{' '}
                <button type="submit">Submit Note</button>
            </p>
        </form>
    );
}

// Subcomponent 4: History list
function HistoryList({ history }) {
    return (
        <div>
            <h3>Activity History (List Rendering)</h3>
            {history.length === 0 ? (
                <p>No activity recorded yet.</p>
            ) : (
                <table border="1" cellPadding="5">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Action</th>
                            <th>Value</th>
                            <th>Note</th>
                            <th>Time</th>
                        </tr>
                    </thead>
                    <tbody>
                        {history.map((item, idx) => (
                            <tr key={item.id}>
                                <td>{idx + 1}</td>
                                <td>{item.action}</td>
                                <td>{item.value}</td>
                                <td>{item.note}</td>
                                <td>{item.time}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            )}
        </div>
    );
}

// Main Component
export default function Practical7_ReactCounterApp() {
    const [count, setCount] = useState(0);
    const [step, setStep] = useState(1);
    const [history, setHistory] = useState([]);

    const logHistory = (action, val, note) => {
        setHistory((prev) => [
            {
                id: Date.now() + Math.random(),
                action,
                value: val,
                note: note || '-',
                time: new Date().toLocaleTimeString(),
            },
            ...prev,
        ]);
    };

    const handleIncrement = () => {
        const next = count + step;
        setCount(next);
        logHistory('Increment', next, 'Added ' + step);
    };

    const handleDecrement = () => {
        const next = count - step;
        setCount(next);
        logHistory('Decrement', next, 'Subtracted ' + step);
    };

    const handleReset = () => {
        setCount(0);
        logHistory('Reset', 0, 'Reset to 0');
    };

    const handleAddNote = (note) => {
        logHistory('User Note', count, note);
    };

    return (
        <div>
            <h2>Practical 7: React Counter Application</h2>
            <p>Components, Conditional Rendering, List Rendering, Text Interpolation & Form Handling</p>
            <hr />

            <CounterDisplay count={count} />
            <br />
            <CounterControls
                onIncrement={handleIncrement}
                onDecrement={handleDecrement}
                onReset={handleReset}
                step={step}
            />
            <hr />
            <ConfigForm step={step} onStepChange={setStep} onAddNote={handleAddNote} />
            <hr />
            <HistoryList history={history} />
        </div>
    );
}""",
        "output_desc": "Combines four subcomponents with state management: display with condition check, step controls, interactive form submission, and activity history table list rendering."
    },
    {
        "num": 8,
        "title": "Practical No. 8: HTTPS Calls in React Component",
        "aim": "To implement secure HTTPS API calls using async/await, error handling, and query filters in a React Component.",
        "code": """// Practical8_HttpsCallsReact.jsx
import React, { useState, useEffect } from 'react';

export default function Practical8_HttpsCallsReact() {
    const [posts, setPosts] = useState([]);
    const [filteredPosts, setFilteredPosts] = useState([]);
    const [searchTerm, setSearchTerm] = useState('');
    const [limit, setLimit] = useState(5);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const fetchHttpsData = async (countLimit) => {
        setLoading(true);
        setError(null);

        try {
            const url = `https://jsonplaceholder.typicode.com/posts?_limit=${countLimit || limit}`;
            const response = await fetch(url);

            if (!response.ok) {
                throw new Error(`HTTPS Request failed! Status: ${response.status}`);
            }

            const data = await response.json();
            setPosts(data);
            setFilteredPosts(data);
        } catch (err) {
            setError(err.message || 'HTTPS request failed');
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchHttpsData(limit);
    }, [limit]);

    const handleSearch = (e) => {
        const query = e.target.value;
        setSearchTerm(query);

        if (!query.trim()) {
            setFilteredPosts(posts);
        } else {
            const filtered = posts.filter((post) =>
                post.title.toLowerCase().includes(query.toLowerCase())
            );
            setFilteredPosts(filtered);
        }
    };

    return (
        <div>
            <h2>Practical 8: HTTPS Calls in React Component</h2>
            <p>Secure HTTPS endpoint with async/await, error handling & live filter</p>
            <hr />

            <p>
                Fetch Records Count: 
                <select value={limit} onChange={(e) => setLimit(Number(e.target.value))}>
                    <option value="5">5 records</option>
                    <option value="10">10 records</option>
                </select>
            </p>
            <p>
                Search / Filter by Title: 
                <input
                    type="text"
                    value={searchTerm}
                    onChange={handleSearch}
                    placeholder="Filter fetched posts..."
                />
            </p>

            {loading && <p><b>[HTTPS] Connecting to secure endpoint... Please wait.</b></p>}
            {error && <p><b>[HTTPS Error]: {error}</b></p>}

            {!loading && !error && (
                <div>
                    <h3>Fetched Results ({filteredPosts.length} of {posts.length} shown)</h3>
                    <table border="1" cellPadding="5">
                        <thead>
                            <tr>
                                <th>Post ID</th>
                                <th>User ID</th>
                                <th>Title</th>
                                <th>Body</th>
                            </tr>
                        </thead>
                        <tbody>
                            {filteredPosts.map((post) => (
                                <tr key={post.id}>
                                    <td>{post.id}</td>
                                    <td>{post.userId}</td>
                                    <td><b>{post.title}</b></td>
                                    <td>{post.body}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            )}
        </div>
    );
}""",
        "output_desc": "Demonstrates an asynchronous secure HTTPS GET call with async/await, try/catch/finally error handling, dynamic limit selection, and live client-side title search filtering."
    }
]

def create_doc(p):
    doc = docx.Document()
    
    # 1 inch margins all around
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)
    
    # Heading: Practical No. X
    h1 = doc.add_paragraph()
    h1.paragraph_format.space_before = Pt(0)
    h1.paragraph_format.space_after = Pt(10)
    run_h1 = h1.add_run(p['title'])
    run_h1.font.name = 'Calibri'
    run_h1.font.size = Pt(18)
    run_h1.font.bold = True
    run_h1.font.color.rgb = RGBColor(15, 23, 42)
    
    # Aim
    p_aim = doc.add_paragraph()
    p_aim.paragraph_format.space_before = Pt(0)
    p_aim.paragraph_format.space_after = Pt(14)
    run_aim_label = p_aim.add_run("Aim: ")
    run_aim_label.font.name = 'Calibri'
    run_aim_label.font.size = Pt(12)
    run_aim_label.font.bold = True
    run_aim_label.font.color.rgb = RGBColor(15, 23, 42)
    
    run_aim_text = p_aim.add_run(p['aim'])
    run_aim_text.font.name = 'Calibri'
    run_aim_text.font.size = Pt(11)
    run_aim_text.font.color.rgb = RGBColor(51, 65, 85)
    
    # Section Heading: Main Logic Code
    h2_code = doc.add_paragraph()
    h2_code.paragraph_format.space_before = Pt(8)
    h2_code.paragraph_format.space_after = Pt(6)
    run_h2_code = h2_code.add_run("Main Logic Code:")
    run_h2_code.font.name = 'Calibri'
    run_h2_code.font.size = Pt(13)
    run_h2_code.font.bold = True
    run_h2_code.font.color.rgb = RGBColor(15, 23, 42)
    
    # VS Code-styled Code Box (Shaded card with Consolas, syntax colors, exact indentation)
    add_code_box(doc, p['code'])
    
    # Section Heading: Output
    h2_out = doc.add_paragraph()
    h2_out.paragraph_format.space_before = Pt(18)
    h2_out.paragraph_format.space_after = Pt(6)
    run_h2_out = h2_out.add_run("Output:")
    run_h2_out.font.name = 'Calibri'
    run_h2_out.font.size = Pt(13)
    run_h2_out.font.bold = True
    run_h2_out.font.color.rgb = RGBColor(15, 23, 42)
    
    p_desc = doc.add_paragraph()
    p_desc.paragraph_format.space_before = Pt(0)
    p_desc.paragraph_format.space_after = Pt(8)
    run_desc = p_desc.add_run(p['output_desc'])
    run_desc.font.name = 'Calibri'
    run_desc.font.size = Pt(11)
    run_desc.font.color.rgb = RGBColor(51, 65, 85)
    
    # Embed the high-resolution screenshot picture
    img_path = os.path.join(img_dir, f"practical_{p['num']}_output.png")
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.paragraph_format.space_before = Pt(4)
        p_img.paragraph_format.space_after = Pt(12)
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        doc.add_picture(img_path, width=Inches(6.2))
        
        # Caption below picture
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(16)
        r_cap = p_cap.add_run(f"Figure: Execution Output of Practical {p['num']}")
        r_cap.font.name = 'Calibri'
        r_cap.font.size = Pt(9.5)
        r_cap.font.italic = True
        r_cap.font.color.rgb = RGBColor(100, 116, 139)
        
    filename = f"Practical_{p['num']}.docx"
    filepath = os.path.join(output_dir, filename)
    doc.save(filepath)
    print(f"Updated: {filepath}")

for p in practicals:
    create_doc(p)

print("All practical docx files updated with VS Code formatting and embedded output pictures!")
