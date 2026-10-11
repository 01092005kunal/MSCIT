// app.js - Practical 1: Price Calculator
var app = angular.module('priceApp', []);

app.controller('PriceController', function($scope) {
    // Initial values
    $scope.itemName = 'Notebook';
    $scope.price = 50;
    $scope.quantity = 2;
    $scope.discount = 10; // in percentage
    $scope.tax = 5;       // in percentage

    // Calculate subtotal
    $scope.getSubtotal = function() {
        return ($scope.price || 0) * ($scope.quantity || 0);
    };

    // Calculate discount amount
    $scope.getDiscountAmount = function() {
        return ($scope.getSubtotal() * ($scope.discount || 0)) / 100;
    };

    // Calculate tax amount
    $scope.getTaxAmount = function() {
        var afterDiscount = $scope.getSubtotal() - $scope.getDiscountAmount();
        return (afterDiscount * ($scope.tax || 0)) / 100;
    };

    // Calculate total price
    $scope.getTotalPrice = function() {
        var afterDiscount = $scope.getSubtotal() - $scope.getDiscountAmount();
        return afterDiscount + $scope.getTaxAmount();
    };

    // Reset values
    $scope.reset = function() {
        $scope.itemName = '';
        $scope.price = 0;
        $scope.quantity = 0;
        $scope.discount = 0;
        $scope.tax = 0;
    };
});
