import { Component, ChangeDetectorRef } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.html',

})
export class App {

  time = 0;
  running = false;

  private timer: any;

  constructor(private changeDetector: ChangeDetectorRef) {}

  start() {

    if (this.running) {
      return;
    }

    this.running = true;

    this.timer = setInterval(() => {

      this.time += 10;

      this.changeDetector.detectChanges();

    }, 10);
  }

  pause() {

    this.running = false;

    clearInterval(this.timer);
    this.timer = null;

    this.changeDetector.detectChanges();
  }

  reset() {

    this.running = false;

    clearInterval(this.timer);
    this.timer = null;

    this.time = 0;

    this.changeDetector.detectChanges();
  }

  get minutes(): string {
    const minutes = Math.floor(this.time / 60000);
    return minutes.toString().padStart(2, '0');
  }

  get seconds(): string {
    const seconds = Math.floor((this.time % 60000) / 1000);
    return seconds.toString().padStart(2, '0');
  }

  get milliseconds(): string {
    const milliseconds = Math.floor((this.time % 1000) / 10);
    return milliseconds.toString().padStart(2, '0');
  }
}