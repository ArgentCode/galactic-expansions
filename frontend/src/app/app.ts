import { Component, inject, OnInit, Signal, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NavMenu } from './components/NavMenu/NavMenu.component';
import { ResourceView } from './components/ResourcesView/ResourceView.component';
import { PlayerStatusService } from './services/player-status.service';
import { PlayerStatus } from './models/player-status.dto';

@Component({
  imports: [RouterOutlet, ResourceView, NavMenu], 
  selector: 'app-root',
  styleUrl: './app.css',
  templateUrl: './app.html',
})
export class App { 
  private statusService = inject(PlayerStatusService);

  protected playerStatus: Signal<PlayerStatus> = this.statusService.status;
}
