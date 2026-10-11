import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Prac1PriceCalcComponent } from './prac1-price-calc/prac1-price-calc';
import { Prac2CounterComponent } from './prac2-counter/prac2-counter';
import { Prac3TimerComponent } from './prac3-timer/prac3-timer';
import { Prac4RoutingComponent } from './prac4-routing/prac4-routing';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule,
    Prac1PriceCalcComponent,
    Prac2CounterComponent,
    Prac3TimerComponent,
    Prac4RoutingComponent
  ],
  templateUrl: './app.html',
  styleUrls: ['./app.css']
})
export class App {
  activePractical: number = 1;

  setPractical(p: number): void {
    this.activePractical = p;
  }
}
