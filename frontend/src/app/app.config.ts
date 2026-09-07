import { ApplicationConfig, inject, provideAppInitializer, provideBrowserGlobalErrorListeners } from '@angular/core';
import { provideRouter } from '@angular/router';
import { routes } from './app.routes';
import { provideHttpClient } from '@angular/common/http';
import { firstValueFrom, tap } from 'rxjs';
import { PlayerStatusService } from './services/player-status.service';

// export const appConfig: ApplicationConfig = {
//   providers: [
//     provideBrowserGlobalErrorListeners(),
//     provideRouter(routes)
//   ]
// };


export const appConfig: ApplicationConfig = {
  providers: [
    provideBrowserGlobalErrorListeners(),
    provideRouter(routes),
    // 1. Ensure the HTTP client is provided so your service can make API calls
    provideHttpClient(), 
    
    // 2. Add the app initializer to fetch data on startup
    provideAppInitializer(() => {
      const playerService = inject(PlayerStatusService);
      
      // Choose the initial player ID you want to load on startup
      const initialPlayerId = 1; 

      return firstValueFrom(
        playerService.getPlayerStatus(initialPlayerId).pipe(
          // Intercept the stream to instantly save the mapped data into your service's signal
          tap(data => playerService.status.set(data))
        )
      );
    })
  ]
};