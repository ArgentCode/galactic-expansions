import { Injectable, inject, signal } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, firstValueFrom, map, tap } from 'rxjs';
import { createEmptyPlayerStatus, PlayerStatus, PlayerStatusDTO } from '../models/player-status.dto';
import { mapPlayerStatusDtoToModel } from './player-status.adapter';

@Injectable({ providedIn: 'root' })
export class PlayerStatusService {
  private http = inject(HttpClient);
  private baseUrl = 'http://localhost:5000'; 

  // The globally accessible saved state
  public status = signal<PlayerStatus>(createEmptyPlayerStatus());

  getPlayerStatus(playerId: number): Observable<PlayerStatus> {
    // Define custom headers
    const headers = new HttpHeaders({
      'player': playerId
    });

    return this.http.get<PlayerStatusDTO>(`${this.baseUrl}/status`, {headers}).pipe(
      map(dto => mapPlayerStatusDtoToModel(dto))
    );
  }
}
