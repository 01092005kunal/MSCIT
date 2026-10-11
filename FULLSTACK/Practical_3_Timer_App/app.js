// app.js - Practical 3: Timer App
// Demonstrates Conditional Rendering (ng-if/ng-show) and List Rendering (ng-repeat)

var app = angular.module('timerApp', []);

app.controller('TimerController', function($scope, $interval) {
    $scope.seconds = 0;
    $scope.isRunning = false;
    $scope.laps = [];
    var timerPromise = null;

    // Start Timer
    $scope.startTimer = function() {
        if (!$scope.isRunning) {
            $scope.isRunning = true;
            timerPromise = $interval(function() {
                $scope.seconds++;
            }, 1000);
        }
    };

    // Pause/Stop Timer
    $scope.pauseTimer = function() {
        if ($scope.isRunning) {
            $interval.cancel(timerPromise);
            $scope.isRunning = false;
        }
    };

    // Reset Timer
    $scope.resetTimer = function() {
        $scope.pauseTimer();
        $scope.seconds = 0;
        $scope.laps = [];
    };

    // Record Lap (for List Rendering)
    $scope.recordLap = function() {
        if ($scope.seconds > 0) {
            $scope.laps.push({
                lapNumber: $scope.laps.length + 1,
                time: $scope.seconds + ' seconds'
            });
        }
    };

    // Clean up timer on scope destroy
    $scope.$on('$destroy', function() {
        if (timerPromise) {
            $interval.cancel(timerPromise);
        }
    });
});
