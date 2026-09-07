import { Component, inject } from '@angular/core';
import { ResourceView } from '../../components/ResourcesView/ResourceView.component';
import { NavMenu } from '../../components/NavMenu/NavMenu.component';
import { PlayerStatusService } from '../../services/player-status.service';

// This should probably be renamed 'Overview'
@Component({
  imports: [ResourceView, NavMenu],
  selector: 'app-homepage',
  styleUrl: './homepage.css',
  templateUrl: './homepage.html',
})
export class Homepage {

  private statusService = inject(PlayerStatusService);

  ngOnInit(): void {}

  handleClick() {
    this.statusService.getPlayerStatus(1).subscribe({
      next: (data) => {
        console.log(data)
      },
      error: (err) => {
        console.error('Failed to load status', err);
      }
    })
  }
}
