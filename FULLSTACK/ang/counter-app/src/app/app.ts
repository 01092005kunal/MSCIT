import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CounterComponent } from './counter/counter';

@Component({
  selector: 'app-root',
  imports: [CounterComponent],
  templateUrl: './app.html'
  
})
export class App {
  initalvalue = 0;
  currentCountValue = 0;

  onInit(event: any) {
    this.initalvalue = parseInt(event.target.value) || 0;
  }

  createCounter() {
    this.currentCountValue = this.initalvalue;
    console.log('Counter created with value:', this.currentCountValue);
  }
}