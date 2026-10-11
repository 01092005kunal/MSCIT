// app.js - Practical 1: Price Calculator (Slab-based distance pricing)
var app = angular.module('priceApp', []);

app.controller('PriceController', function($scope) {
    // Initial distance value
    $scope.distance = 7;

    // Slab-based price calculation
    $scope.calculatePrice = function(distance) {
        var d = Number(distance) || 0;
        var price = 0;

        if (d <= 0) {
            return 0;
        }

        // Slab 1: 0–5 km → ₹10/km
        if (d <= 5) {
            price = d * 10;
        }
        // Slab 2: 5–10 km → ₹6/km
        else if (d <= 10) {
            price = (5 * 10) + (d - 5) * 6;
        }
        // Slab 3: Above 10 km → ₹4/km
        else {
            price = (5 * 10) + (5 * 6) + (d - 10) * 4;
        }

        return price;
    };

    // Helper to explain the slab breakdown
    $scope.getBreakdown = function() {
        var d = Number($scope.distance) || 0;
        if (d <= 0) return 'Distance must be greater than 0';

        if (d <= 5) {
            return d + ' km × ₹10 = ₹' + (d * 10);
        } else if (d <= 10) {
            return '(5 km × ₹10) + (' + (d - 5) + ' km × ₹6) = ₹' + ((5 * 10) + (d - 5) * 6);
        } else {
            return '(5 km × ₹10) + (5 km × ₹6) + (' + (d - 10) + ' km × ₹4) = ₹' + ((5 * 10) + (5 * 6) + (d - 10) * 4);
        }
    };

    // Reset distance
    $scope.reset = function() {
        $scope.distance = 0;
    };
});
