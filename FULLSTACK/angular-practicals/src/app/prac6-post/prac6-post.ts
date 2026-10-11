import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

interface PostResponse {
  id: number;
  title: string;
  body: string;
  userId: number;
}

@Component({
  selector: 'app-prac6-post',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './prac6-post.html',
  styleUrls: ['./prac6-post.css']
})
export class Prac6PostComponent {
  userId: number = 1;
  title: string = '';
  body: string = '';
  loading: boolean = false;
  statusMessage: string = '';
  responseResult: PostResponse | null = null;
  postsList: PostResponse[] = [];

  constructor(private http: HttpClient) {}

  handleSubmit(): void {
    if (!this.title.trim() || !this.body.trim()) {
      alert('Please fill all fields.');
      return;
    }

    this.loading = true;
    this.statusMessage = 'Posting data to REST API...';
    this.responseResult = null;

    const payload = {
      title: this.title,
      body: this.body,
      userId: Number(this.userId)
    };

    this.http.post<PostResponse>('https://jsonplaceholder.typicode.com/posts', payload)
      .subscribe({
        next: (res) => {
          this.loading = false;
          this.statusMessage = 'Data posted successfully! (HTTP 201 Created)';
          this.responseResult = res;
          this.postsList.unshift(res);
          this.title = '';
          this.body = '';
        },
        error: (err) => {
          this.loading = false;
          this.statusMessage = 'Error: ' + (err.message || 'Failed to post data');
        }
      });
  }
}
