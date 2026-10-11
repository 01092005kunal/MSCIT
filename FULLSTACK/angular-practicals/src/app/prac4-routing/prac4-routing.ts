import { Component, OnDestroy } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-prac4-routing',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './prac4-routing.html',
  styleUrls: ['./prac4-routing.css']
})
export class Prac4RoutingComponent implements OnDestroy {
  activeView: 'timer' | 'stopwatch' = 'timer';

  // Countdown Timer State
  inputMinutes: number = 1;
  remainingSeconds: number = 60;
  timerRunning: boolean = false;
  private timerInterval: any = null;

  // Stopwatch State
  stopwatchSeconds: number = 0;
  stopwatchRunning: boolean = false;
  private stopwatchInterval: any = null;

  setView(view: 'timer' | 'stopwatch'): void {
    this.activeView = view;
  }

  // Timer Methods
  startTimer(): void {
    if (!this.timerRunning) {
      if (this.remainingSeconds <= 0) {
        this.remainingSeconds = (this.inputMinutes || 1) * 60;
      }
      this.timerRunning = true;
      this.timerInterval = setInterval(() => {
        if (this.remainingSeconds > 0) {
          this.remainingSeconds--;
        } else {
          this.stopTimer();
          alert('Countdown Finished!');
        }
      }, 1000);
    }
  }

  stopTimer(): void {
    if (this.timerRunning) {
      clearInterval(this.timerInterval);
      this.timerRunning = false;
    }
  }

  resetTimer(): void {
    this.stopTimer();
    this.remainingSeconds = (this.inputMinutes || 1) * 60;
  }

  // Stopwatch Methods
  startStopwatch(): void {
    if (!this.stopwatchRunning) {
      this.stopwatchRunning = true;
      this.stopwatchInterval = setInterval(() => {
        this.stopwatchSeconds++;
      }, 1000);
    }
  }

  pauseStopwatch(): void {
    if (this.stopwatchRunning) {
      clearInterval(this.stopwatchInterval);
      this.stopwatchRunning = false;
    }
  }

  resetStopwatch(): void {
    this.pauseStopwatch();
    this.stopwatchSeconds = 0;
  }

  ngOnDestroy(): void {
    if (this.timerInterval) clearInterval(this.timerInterval);
    if (this.stopwatchInterval) clearInterval(this.stopwatchInterval);
  }
}
