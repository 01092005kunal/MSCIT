import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-counter',
  templateUrl: './counter.html'
})
export class CounterComponent {
  @Input() countValue = 0;
  @Output() countChanged = new EventEmitter<number>();

  increment() {
    this.countValue++;
    this.countChanged.emit(this.countValue);
  }

  decrement() {
    this.countValue--;
    this.countChanged.emit(this.countValue);
  }
}