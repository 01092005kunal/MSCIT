import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';

interface User {
  id: number;
  name: string;
  email: string;
  phone: string;
  company: { name: string };
  address: { city: string };
}

@Component({
  selector: 'app-prac5-http',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './prac5-http.html',
  styleUrls: ['./prac5-http.css']
})
export class Prac5HttpComponent implements OnInit {
  users: User[] = [];
  loading: boolean = false;
  error: string | null = null;

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.fetchUsers();
  }

  fetchUsers(): void {
    this.loading = true;
    this.error = null;

    this.http.get<User[]>('https://jsonplaceholder.typicode.com/users')
      .subscribe({
        next: (data) => {
          this.users = data;
          this.loading = false;
        },
        error: (err) => {
          this.error = err.message || 'Failed to fetch users';
          this.loading = false;
        }
      });
  }
}
