import { Component, inject, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { StatusApi } from './services/status-api';

@Component({
  imports: [RouterOutlet],
  selector: 'app-root',
  styleUrl: './app.css',
  templateUrl: './app.html',
})
export class App {
  private api = inject(StatusApi);
  protected readonly title = signal('alex');

  async getData() {
    const result = await this.api.getUser(1);
    result.subscribe((res) => console.log(res))
  }
}
