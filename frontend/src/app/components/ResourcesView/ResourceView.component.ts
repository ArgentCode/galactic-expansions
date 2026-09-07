import { Component, input } from '@angular/core';

@Component({
  imports: [],
  selector: 'ResourceView',
  templateUrl: './ResourceView.component.html',
})
export class ResourceView {
    metal = input.required<number>();
    crystal = input.required<number>();
    deut = input.required<number>();
}
