# Practical Journal: Full Stack Fundamentals (RPSITP0506-1)
**Student Name:** Kunal D. Mhatre  
**Roll No:** 206  
**Class:** MSc.IT - Semester I  
**College:** Ramnarain Ruia Autonomous College, Matunga  

---

## Index of Practicals

| Practical No. | Date | Topic | Framework / Language |
| :---: | :---: | :--- | :--- |
| **Practical 1** | 05/08/2026 | Price calculator | Node.js (ES Modules / MJS) |
| **Practical 2** | 12/08/2026 | Text Interpolation, Event Handling, Custom Events and 2-way data binding using Counter App | Angular (TS) |
| **Practical 3** | 19/08/2026 | Conditional and List Rendering using Timer App | Angular (TS) |
| **Practical 4** | 26/08/2026 | Routing using Timer and stopwatch App | Angular (TS) |
| **Practical 5** | 02/09/2026 | HTTP calls using REST API | React (JSX) |
| **Practical 6** | 09/09/2026 | Posting data to REST API | React (JSX) |
| **Practical 7** | 23/09/2026 | Components, conditional rendering, list rendering, text Interpolation, and form handling using the Counter App | React (JSX) |
| **Practical 8** | 30/09/2026 | HTTPs calls in react Component | React (JSX) |

---

## Practical 1: Price Calculator (ES Modules)
- **Aim:** To implement a Slab-based Price Calculator using JavaScript ES Modules (`.mjs`) demonstrating `export` and `import` statements in Node.js.
- **Key Concepts:** ES Module system, named and default exports (`export const`, `export default`), module imports (`import { ... } from './...'`), tiered rate slabs (0–5 km: ₹10/km, 5–10 km: ₹6/km, >10 km: ₹4/km).
- **Files:**
  - `slab.mjs`
  - `calc.mjs`
  - `index.mjs`

### Code:

**`slab.mjs`:**
```javascript
// slab.mjs - Defines and exports rate slab definitions
export const slabs = [
    { name: "Slab 1", minKm: 0, maxKm: 5, rate: 10 },      // 0–5 km: ₹10/km
    { name: "Slab 2", minKm: 5, maxKm: 10, rate: 6 },      // 5–10 km: ₹6/km
    { name: "Slab 3", minKm: 10, maxKm: Infinity, rate: 4 } // Above 10 km: ₹4/km
];

export default slabs;
```

**`calc.mjs`:**
```javascript
// calc.mjs - Imports slab definitions and exports price calculation logic
import { slabs } from './slab.mjs';

export function calculatePrice(distance) {
    const d = Number(distance) || 0;
    let price = 0;

    if (d <= 0) return 0;

    // Slab 1: 0–5 km → ₹10/km
    if (d <= 5) {
        price = d * slabs[0].rate;
    }
    // Slab 2: 5–10 km → ₹6/km
    else if (d <= 10) {
        price = (5 * slabs[0].rate) + (d - 5) * slabs[1].rate;
    }
    // Slab 3: Above 10 km → ₹4/km
    else {
        price = (5 * slabs[0].rate) + (5 * slabs[1].rate) + (d - 10) * slabs[2].rate;
    }

    return price;
}

export function getBreakdown(distance) {
    const d = Number(distance) || 0;
    if (d <= 0) return "Distance must be greater than 0";

    if (d <= 5) {
        return `${d} km × ₹${slabs[0].rate} = ₹${d * slabs[0].rate}`;
    } else if (d <= 10) {
        return `(5 km × ₹${slabs[0].rate}) + (${d - 5} km × ₹${slabs[1].rate}) = ₹${calculatePrice(d)}`;
    } else {
        return `(5 km × ₹${slabs[0].rate}) + (5 km × ₹${slabs[1].rate}) + (${d - 10} km × ₹${slabs[2].rate}) = ₹${calculatePrice(d)}`;
    }
}
```

**`index.mjs`:**
```javascript
// index.mjs - Main execution demonstrating ES Module imports
import { slabs } from './slab.mjs';
import { calculatePrice, getBreakdown } from './calc.mjs';

console.log("=========================================");
console.log(" Practical 1: Price Calculator (ESM .mjs)");
console.log("=========================================\n");

console.log("Rate Slabs Loaded from Module (slab.mjs):");
slabs.forEach((s) => {
    const limit = s.maxKm === Infinity ? "Above 10 km" : `${s.minKm}–${s.maxKm} km`;
    console.log(` - ${s.name}: ${limit} @ ₹${s.rate}/km`);
});

console.log("\n--- Fare Calculations ---");
const testDistances = [3, 7, 15];

testDistances.forEach((distance) => {
    console.log(`\nTrip Distance: ${distance} km`);
    console.log(`Breakdown: ${getBreakdown(distance)}`);
    console.log(`Total Price: ₹${calculatePrice(distance)}`);
});
```

### Execution & Output:
```bash
node index.mjs
```
```
=========================================
 Practical 1: Price Calculator (ESM .mjs)
=========================================

Rate Slabs Loaded from Module (slab.mjs):
 - Slab 1: 0–5 km @ ₹10/km
 - Slab 2: 5–10 km @ ₹6/km
 - Slab 3: Above 10 km @ ₹4/km

--- Fare Calculations ---

Trip Distance: 3 km
Breakdown: 3 km × ₹10 = ₹30
Total Price: ₹30

Trip Distance: 7 km
Breakdown: (5 km × ₹10) + (2 km × ₹6) = ₹62
Total Price: ₹62

Trip Distance: 15 km
Breakdown: (5 km × ₹10) + (5 km × ₹6) + (5 km × ₹4) = ₹100
Total Price: ₹100
```

---

## Practical 2: Counter App
- **Aim:** To demonstrate Text Interpolation, Event Handling, Custom Events, and 2-way data binding using a Counter App in Angular.
- **Key Concepts:**
  - **Text Interpolation:** `{{ count }}`
  - **Event Handling:** `ng-click="increment()"`
  - **2-Way Data Binding:** `ng-model="step"`
  - **Custom Events:** `$emit('THRESHOLD_REACHED')` and `$on('THRESHOLD_REACHED')`
- **Files:**
  - `Practical_2_Counter_App/index.html`
  - `Practical_2_Counter_App/app.js`

### Code:
**`app.js`:**
```javascript
var app = angular.module('counterApp', []);

app.controller('CounterController', function($scope) {
    $scope.count = 0;
    $scope.message = 'Counter initialized.';
    $scope.step = 1;
    $scope.threshold = 10;
    $scope.customEventMsg = '';

    // Listen for custom event
    $scope.$on('THRESHOLD_REACHED', function(event, data) {
        $scope.customEventMsg = 'Custom Event: Count reached ' + data.currentCount;
    });

    function checkThreshold() {
        if ($scope.count >= $scope.threshold) {
            $scope.$emit('THRESHOLD_REACHED', {
                currentCount: $scope.count,
                limit: $scope.threshold
            });
        } else {
            $scope.customEventMsg = '';
        }
    }

    $scope.increment = function() {
        $scope.count += Number($scope.step);
        $scope.message = 'Incremented by ' + $scope.step;
        checkThreshold();
    };

    $scope.decrement = function() {
        $scope.count -= Number($scope.step);
        $scope.message = 'Decremented by ' + $scope.step;
        checkThreshold();
    };

    $scope.reset = function() {
        $scope.count = 0;
        $scope.message = 'Counter reset to 0.';
        $scope.customEventMsg = '';
    };
});
```

---

## Practical 3: Conditional and List Rendering using Timer App
- **Aim:** To implement Conditional Rendering (`ng-if`) and List Rendering (`ng-repeat`) using a Timer App in Angular.
- **Key Concepts:**
  - `ng-if`: Displaying state messages (Running, Paused, Idle, or Empty Laps).
  - `ng-repeat`: Rendering array of lap items in an HTML table.
  - `$interval`: Timer execution and cleanup.
- **Files:**
  - `Practical_3_Timer_App/index.html`
  - `Practical_3_Timer_App/app.js`

---

## Practical 4: Routing using Timer and Stopwatch App
- **Aim:** To implement client-side routing between a Timer component and a Stopwatch component in Angular using `ngRoute`.
- **Key Concepts:** `$routeProvider.when('/timer', ...)`, `$routeProvider.when('/stopwatch', ...)`, `<div ng-view></div>`.
- **Files:**
  - `Practical_4_Routing_Timer_Stopwatch/index.html`
  - `Practical_4_Routing_Timer_Stopwatch/app.js`

---

## Practical 5: HTTP calls using REST API (Angular)
- **Aim:** To fetch and display data from a REST API using HTTP GET requests with Angular `HttpClient`.
- **Key Concepts:** `HttpClient`, `provideHttpClient()`, Observable subscription (`.subscribe()`), `*ngIf` loading/error states, `*ngFor` table rendering.
- **API Endpoint:** `https://jsonplaceholder.typicode.com/users`
- **Files:**
  - `angular-practicals/src/app/prac5-http/prac5-http.ts`
  - `angular-practicals/src/app/prac5-http/prac5-http.html`

---

## Practical 6: Posting Data to REST API (Angular)
- **Aim:** To submit user data to a REST API using HTTP POST in Angular with a template-driven form.
- **Key Concepts:** Template-driven forms (`[(ngModel)]`), `HttpClient.post()`, handling response status 201 Created, `json` pipe, dynamic list updating.
- **API Endpoint:** `https://jsonplaceholder.typicode.com/posts`
- **Files:**
  - `angular-practicals/src/app/prac6-post/prac6-post.ts`
  - `angular-practicals/src/app/prac6-post/prac6-post.html`

---

## Practical 7: Components, Conditional Rendering, List Rendering, Text Interpolation & Form Handling (React)
- **Aim:** To demonstrate React modular components, conditional rendering, list rendering, text interpolation, and form handling in a Counter application.
- **Key Concepts:**
  - **Child Components:** `CounterDisplay`, `CounterControls`, `ConfigForm`, `HistoryList`.
  - **Conditional Rendering:** Positive/Negative/Warning condition checks.
  - **List Rendering:** `.map()` over history log.
  - **Form Handling:** `onChange`, `onSubmit`, `preventDefault()`.
  - **Text Interpolation:** `{count}`, `{step}` in JSX.
- **Files:**
  - `Practical_7_React_Counter_App/App.jsx`
  - `Practical_7_React_Counter_App/index.html`

---

## Practical 8: HTTPS Calls in React Component (React)
- **Aim:** To implement secure HTTPS API calls using `async/await`, error handling, and query filters in a React component.
- **Key Concepts:** Secure `https://` protocol, `async/await` syntax, `try...catch...finally`, query parameter filtering, live title search.
- **API Endpoint:** `https://jsonplaceholder.typicode.com/posts?_limit=...`
- **Files:**
  - `Practical_8_HTTPS_Calls_React/App.jsx`
  - `Practical_8_HTTPS_Calls_React/index.html`

---

## How to Run:
1. Simply double-click any `index.html` file in any of the practical folders, or open `FULLSTACK/index.html` in Chrome/Edge to view the full index table!
2. All libraries (AngularJS, ngRoute, React 18, Babel) are loaded via standard CDNs without requiring compilation or node build steps.
