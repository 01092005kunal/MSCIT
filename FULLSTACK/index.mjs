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
