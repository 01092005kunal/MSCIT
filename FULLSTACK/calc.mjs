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
