import { Routes } from '@angular/router';
import { MenuMeta } from '../app.routing';
import { TurnoComponent, TurnoEditComponent, TurnoListComponent } from './turno/turno.component';
import { TurnoService } from './turno/turno.service';

export const TurnoRoutes: Routes = [
    {
        path: '', children: [
            {
                path: 'turno', component: TurnoComponent, children: [
                    { path: '', component: TurnoListComponent },
                    { path: ':id/edit', component: TurnoEditComponent, resolve: { item: TurnoService } }
                ]
            }
        ]
    }

];
