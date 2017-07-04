import { Routes } from '@angular/router';
import { MenuMeta } from '../app.routing';
import { EmpleadoComponent, EmpleadoEditComponent, EmpleadoListComponent } from './empleado/empleado.component';
import { EmpleadoService } from './empleado/empleado.service';

export const EmpleadoRoutes: Routes = [
    {
        path: '', children: [
            {
                path: 'empleados', component: EmpleadoComponent, children: [
                    { path: '', component: EmpleadoListComponent },
                    { path: ':id/edit', component: EmpleadoEditComponent, resolve: { item: EmpleadoService } }
                ]
            }
        ]
    }

];
