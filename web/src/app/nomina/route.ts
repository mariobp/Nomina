import { Routes } from '@angular/router';
import { MenuMeta } from '../app.routing';
import { NominaComponent, NominaEditComponent, NominaListComponent } from './nomina/nomina.component';
import { NominaService } from './nomina/nomina.service';

export const NominaRoutes: Routes = [
    {
        path: '', children: [
            {
                path: 'nomina', component: NominaComponent, children: [
                    { path: '', component: NominaListComponent },
                    { path: ':id/edit', component: NominaEditComponent, resolve: { item: NominaService } }
                ]
            }
        ]
    }

];
