import { Routes } from '@angular/router';
import { Homepage } from './pages/homepage/homepage';
import { Upgrades } from './pages/upgrades/upgrades';

export const routes: Routes = [
    {path: '', component: Homepage},
    {path: 'upgrades', component: Upgrades}
];
