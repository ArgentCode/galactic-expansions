import { Component, inject } from '@angular/core';
import { ApiService } from '../../services/data.service';
import { ResourceView } from '../../components/ResourcesView/ResourceView.component';

@Component({
  imports: [ResourceView],
  selector: 'app-homepage',
  styleUrl: './homepage.css',
  templateUrl: './homepage.html',
})
export class Homepage {

  private apiService = inject(ApiService);

  ngOnInit(): void {
    
  }

  handleClick() {
    console.log(this.apiService.fetchData(1));
  }
}
