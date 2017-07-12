import { Routes } from '@angular/router';
import { MenuMeta } from '../app.routing';
import { ContratoListComponent, EditContratoComponent } from './contrato/contrato.component';
import { EmpleadoComponent, EmpleadoEditComponent, EmpleadoListComponent } from './empleado/empleado.component';
import { EmpleadoService } from './empleado/empleado.service';
import { ContratoService } from './contrato/contrato.service';
export const EmpleadoRoutes: Routes = [
    {
        path: '', children: [
            {
                path: 'empleados', component: EmpleadoComponent, data: { miga: 'Empleados' }, children: [
                    { path: '', component: EmpleadoListComponent },
                    {
                        path: ':id/edit', component: EmpleadoEditComponent, data: { miga: 'Editar' }, resolve: { item: EmpleadoService }, children: [
                            { path: '', component: ContratoListComponent },
                            { path: ':id/edit', component: EditContratoComponent, resolve: { item: ContratoService } }
                        ]
                    }
                ]
            }
        ]
    }

];
