# Practical Journal: Full Stack Fundamentals (RPSITP0506-1)
**Student Name:** Kunal D. Mhatre  
**Roll No:** 206  
**Class:** MSc.IT - Semester I  
**College:** Ramnarain Ruia Autonomous College, Matunga  

---

## Index of Practicals

| Practical No. | Date | Topic | Framework / Language |
| :---: | :---: | :--- | :--- |
| **Practical 1** | 05/08/2026 | Price calculator | Angular (JS) |
| **Practical 2** | 12/08/2026 | Text Interpolation, Event Handling, Custom Events and 2-way data binding using Counter App | Angular (JS) |
| **Practical 3** | 19/08/2026 | Conditional and List Rendering using Timer App | Angular (JS) |
| **Practical 4** | 26/08/2026 | Routing using Timer and stopwatch App | Angular (JS) |
| **Practical 5** | 02/09/2026 | HTTP calls using REST API | React (JSX) |
| **Practical 6** | 09/09/2026 | Posting data to REST API | React (JSX) |
| **Practical 7** | 23/09/2026 | Components, conditional rendering, list rendering, text Interpolation, and form handling using the Counter App | React (JSX) |
| **Practical 8** | 30/09/2026 | HTTPs calls in react Component | React (JSX) |

---

## Practical 1: Price Calculator
- **Aim:** To develop a simple Price Calculator in Angular using JavaScript.
- **Key Concepts:** Scope variables, dynamic price calculation with quantity, discount percentage, and tax/GST percentage.
- **Files:**
  - `Practical_1_Price_Calculator/index.html`
  - `Practical_1_Price_Calculator/app.js`

### Code:
**`app.js`:**
```javascript
var app = angular.module('priceApp', []);

app.controller('PriceController', function($scope) {
    $scope.itemName = 'Notebook';
    $scope.price = 50;
    $scope.quantity = 2;
    $scope.discount = 10;
    $scope.tax = 5;

    $scope.getSubtotal = function() {
        return ($scope.price || 0) * ($scope.quantity || 0);
    };

    $scope.getDiscountAmount = function() {
        return ($scope.getSubtotal() * ($scope.discount || 0)) / 100;
    };

    $scope.getTaxAmount = function() {
        var afterDiscount = $scope.getSubtotal() - $scope.getDiscountAmount();
        return (afterDiscount * ($scope.tax || 0)) / 100;
    };

    $scope.getTotalPrice = function() {
        var afterDiscount = $scope.getSubtotal() - $scope.getDiscountAmount();
        return afterDiscount + $scope.getTaxAmount();
    };

    $scope.reset = function() {
        $scope.itemName = '';
        $scope.price = 0;
        $scope.quantity = 0;
        $scope.discount = 0;
        $scope.tax = 0;
    };
});
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

## Practical 5: HTTP calls using REST API (React)
- **Aim:** To fetch and display data from a REST API using HTTP GET requests in a React component.
- **Key Concepts:** `fetch()`, `useEffect()`, `useState()`, Promise handling, Loading and Error state management.
- **API Endpoint:** `https://jsonplaceholder.typicode.com/users`
- **Files:**
  - `Practical_5_HTTP_REST_API/App.jsx`
  - `Practical_5_HTTP_REST_API/index.html`

---

## Practical 6: Posting Data to REST API (React)
- **Aim:** To submit user data to a REST API using HTTP POST in React with a controlled form.
- **Key Concepts:** Controlled form inputs (`useState`), `fetch(url, { method: 'POST', body, headers })`, handling response status 201 Created, updating UI dynamically.
- **API Endpoint:** `https://jsonplaceholder.typicode.com/posts`
- **Files:**
  - `Practical_6_Posting_Data_REST_API/App.jsx`
  - `Practical_6_Posting_Data_REST_API/index.html`

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
