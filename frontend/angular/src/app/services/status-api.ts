import { HttpClient, HttpHeaders } from '@angular/common/http';
import { inject, Service } from '@angular/core';
import { Observable } from 'rxjs';
import { StatusModel } from '../models/status.interface';

@Service()
export class StatusApi {
    private http = inject(HttpClient); // Modern injection syntax (or use constructor)
    private apiUrl = '/api/status';

    // Returns an Observable array of Users
    public getUser(playerId: number): Observable<StatusModel> {
        const headers = new HttpHeaders()
            .set('Content-Type', 'application/json')
            .set('player', playerId.toString());
        return this.http.get<StatusModel>(this.apiUrl, { headers });
    }
}
