import { Component, inject } from '@angular/core';
import { ApiService } from '../../services/data.service';

@Component({
  imports: [],
  selector: 'app-homepage',
  styleUrl: './homepage.css',
  templateUrl: './homepage.html',
})
export class Homepage {

  private apiService = inject(ApiService);

  handleClick() {
    console.log(this.apiService.fetchData());
  }
}
