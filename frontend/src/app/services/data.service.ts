import { Injectable, inject, signal } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { firstValueFrom } from 'rxjs';

@Injectable({
  providedIn: 'root'
}
)
export class ApiService {
  private http = inject(HttpClient);
  
  // Point to localhost because the browser executes this code, not Docker
  private baseUrl = 'http://localhost:5000'; 

  // Read-only signal for your component to consume
  data = signal<any>(null);
  loading = signal<boolean>(false);
  error = signal<string | null>(null);

  /**
   * Fetches data from a Flask endpoint (e.g., /api/data)
   */
  async fetchData(playerId: number) {
    this.loading.set(true);
    this.error.set(null);

    try {
      // Define custom headers
      const headers = new HttpHeaders({
        'player': playerId
      });
      
      // firstValueFrom converts the Observable to a clean async/await Promise
      const response = await firstValueFrom(
        this.http.get<any>(`${this.baseUrl}/status`, { headers })
      );
      this.data.set(response);
    } catch (err: any) {
      this.error.set(err.message || 'Failed to fetch data');
    } finally {
      this.loading.set(false);
    }
  }
}
