function calculatePrice(distance) {
    let price = 0;

    // Slab 1: 0–5 km → ₹10/km
    if (distance <= 5) {
        price = distance * 10;
    }

    // Slab 2: 5–10 km → ₹6/km
    else if (distance <= 10) {
        price = (5 * 10) + (distance - 5) * 6;
    }

    // Slab 3: Above 10 km → ₹4/km
    else {
        price = (5 * 10) + (5 * 6) + (distance - 10) * 4;
    }

    return price;
}

const tripDistance = 7;

const totalPrice = calculatePrice(tripDistance);

console.log("Trip Distance:", tripDistance, "km");
console.log("Total Price: ₹" + totalPrice);
