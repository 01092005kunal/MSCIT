import { Component, EventEmitter, Output } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-prac2-counter',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './prac2-counter.html',
  styleUrls: ['./prac2-counter.css']
})
export class Prac2CounterComponent {
  // 1. Text Interpolation
  count: number = 0;
  message: string = 'Counter initialized.';

  // 2. Two-way Data Binding
  step: number = 1;
  threshold: number = 10;
  customEventMsg: string = '';

  // 3. Custom Event Output
  @Output() thresholdReached = new EventEmitter<number>();

  checkThreshold(): void {
    if (Math.abs(this.count) >= this.threshold) {
      this.customEventMsg = `Custom Event Fired: Count reached ${this.count} (Threshold: ${this.threshold})`;
      this.thresholdReached.emit(this.count);
    } else {
      this.customEventMsg = '';
    }
  }

  // 4. Event Handlers
  increment(): void {
    this.count += (Number(this.step) || 1);
    this.message = `Incremented by ${this.step}`;
    this.checkThreshold();
  }

  decrement(): void {
    this.count -= (Number(this.step) || 1);
    this.message = `Decremented by ${this.step}`;
    this.checkThreshold();
  }

  reset(): void {
    this.count = 0;
    this.message = 'Counter reset to 0.';
    this.customEventMsg = '';
  }
}
