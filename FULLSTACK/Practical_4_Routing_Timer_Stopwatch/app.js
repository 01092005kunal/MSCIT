// app.js - Practical 4: Routing using Timer and Stopwatch App
var app = angular.module('routingApp', ['ngRoute']);

// Configure Routing
app.config(function($routeProvider, $locationProvider) {
    $locationProvider.hashPrefix(''); // clean hash routing e.g. #/timer

    $routeProvider
        .when('/timer', {
            templateUrl: 'timer.html',
            controller: 'TimerController'
        })
        .when('/stopwatch', {
            templateUrl: 'stopwatch.html',
            controller: 'StopwatchController'
        })
        .otherwise({
            redirectTo: '/timer'
        });
});

// Timer Controller (Countdown Timer)
app.controller('TimerController', function($scope, $interval) {
    $scope.inputMinutes = 1;
    $scope.remainingSeconds = 60;
    $scope.timerRunning = false;
    var timerInterval = null;

    $scope.startTimer = function() {
        if (!$scope.timerRunning) {
            if ($scope.remainingSeconds <= 0) {
                $scope.remainingSeconds = ($scope.inputMinutes || 1) * 60;
            }
            $scope.timerRunning = true;
            timerInterval = $interval(function() {
                if ($scope.remainingSeconds > 0) {
                    $scope.remainingSeconds--;
                } else {
                    $scope.stopTimer();
                    alert('Timer Finished!');
                }
            }, 1000);
        }
    };

    $scope.stopTimer = function() {
        if ($scope.timerRunning) {
            $interval.cancel(timerInterval);
            $scope.timerRunning = false;
        }
    };

    $scope.resetTimer = function() {
        $scope.stopTimer();
        $scope.remainingSeconds = ($scope.inputMinutes || 1) * 60;
    };
});

// Stopwatch Controller (Count up)
app.controller('StopwatchController', function($scope, $interval) {
    $scope.seconds = 0;
    $scope.isRunning = false;
    var stopInterval = null;

    $scope.start = function() {
        if (!$scope.isRunning) {
            $scope.isRunning = true;
            stopInterval = $interval(function() {
                $scope.seconds++;
            }, 1000);
        }
    };

    $scope.pause = function() {
        if ($scope.isRunning) {
            $interval.cancel(stopInterval);
            $scope.isRunning = false;
        }
    };

    $scope.reset = function() {
        $scope.pause();
        $scope.seconds = 0;
    };
});
