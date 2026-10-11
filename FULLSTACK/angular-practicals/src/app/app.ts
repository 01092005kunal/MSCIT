import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Prac2CounterComponent } from './prac2-counter/prac2-counter';
import { Prac3TimerComponent } from './prac3-timer/prac3-timer';
import { Prac4RoutingComponent } from './prac4-routing/prac4-routing';
import { Prac5HttpComponent } from './prac5-http/prac5-http';
import { Prac6PostComponent } from './prac6-post/prac6-post';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule,
    Prac2CounterComponent,
    Prac3TimerComponent,
    Prac4RoutingComponent,
    Prac5HttpComponent,
    Prac6PostComponent
  ],
  templateUrl: './app.html',
  styleUrls: ['./app.css']
})
export class App {
  activePractical: number = 2;

  setPractical(p: number): void {
    this.activePractical = p;
  }
}
