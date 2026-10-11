import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-prac1-price-calc',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './prac1-price-calc.html',
  styleUrls: ['./prac1-price-calc.css']
})
export class Prac1PriceCalcComponent {
  distance: number = 7;

  calculatePrice(dist: number): number {
    const d = Number(dist) || 0;
    let price = 0;

    if (d <= 0) return 0;

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
  }

  getBreakdown(): string {
    const d = Number(this.distance) || 0;
    if (d <= 0) return 'Distance must be greater than 0';

    if (d <= 5) {
      return `${d} km × ₹10 = ₹${d * 10}`;
    } else if (d <= 10) {
      return `(5 km × ₹10) + (${d - 5} km × ₹6) = ₹${(5 * 10) + (d - 5) * 6}`;
    } else {
      return `(5 km × ₹10) + (5 km × ₹6) + (${d - 10} km × ₹4) = ₹${(5 * 10) + (5 * 6) + (d - 10) * 4}`;
    }
  }

  reset(): void {
    this.distance = 0;
  }
}
