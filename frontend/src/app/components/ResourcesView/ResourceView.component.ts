import { Component, input } from '@angular/core';
import { PlayerStatus } from '../../models/player-status.dto';

@Component({
  imports: [],
  selector: 'ResourceView',
  styleUrl: './ResourceView.component.css',
  templateUrl: './ResourceView.component.html',
})
export class ResourceView {
    playerStatus = input.required<PlayerStatus>()
}
