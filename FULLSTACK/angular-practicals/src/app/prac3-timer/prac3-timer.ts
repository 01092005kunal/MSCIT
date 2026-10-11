import { Component, OnDestroy } from '@angular/core';
import { CommonModule } from '@angular/common';

interface LapItem {
  lapNumber: number;
  time: string;
}

@Component({
  selector: 'app-prac3-timer',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './prac3-timer.html',
  styleUrls: ['./prac3-timer.css']
})
export class Prac3TimerComponent implements OnDestroy {
  seconds: number = 0;
  isRunning: boolean = false;
  laps: LapItem[] = [];
  private intervalId: any = null;

  startTimer(): void {
    if (!this.isRunning) {
      this.isRunning = true;
      this.intervalId = setInterval(() => {
        this.seconds++;
      }, 1000);
    }
  }

  pauseTimer(): void {
    if (this.isRunning) {
      clearInterval(this.intervalId);
      this.isRunning = false;
    }
  }

  resetTimer(): void {
    this.pauseTimer();
    this.seconds = 0;
    this.laps = [];
  }

  recordLap(): void {
    if (this.seconds > 0) {
      this.laps.push({
        lapNumber: this.laps.length + 1,
        time: `${this.seconds} seconds`
      });
    }
  }

  ngOnDestroy(): void {
    if (this.intervalId) {
      clearInterval(this.intervalId);
    }
  }
}
