// app.js - Practical 2: Counter App
// Demonstrates Text Interpolation, Event Handling, Custom Events, and 2-way Data Binding

var app = angular.module('counterApp', []);

app.controller('CounterController', function($scope) {
    // 1. Text Interpolation variables
    $scope.count = 0;
    $scope.message = 'Counter initialized.';

    // 2. Two-way Data Binding variables (ng-model)
    $scope.step = 1;
    $scope.threshold = 10;

    // Custom event message
    $scope.customEventMsg = '';

    // 3. Listen for Custom Event
    $scope.$on('THRESHOLD_REACHED', function(event, data) {
        $scope.customEventMsg = 'Custom Event Triggered: Count reached ' + data.currentCount + ' (Threshold: ' + data.limit + ')';
    });

    // Check condition and emit Custom Event
    function checkThreshold() {
        if ($scope.count >= $scope.threshold) {
            // Emitting custom event
            $scope.$emit('THRESHOLD_REACHED', {
                currentCount: $scope.count,
                limit: $scope.threshold
            });
        } else {
            $scope.customEventMsg = '';
        }
    }

    // 4. Event Handling functions (ng-click)
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
