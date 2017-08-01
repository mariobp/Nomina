import { Routes } from '@angular/router';
import { MenuMeta } from '../app.routing';
import { ProduccionComponent, ProduccionListComponent, EditProduccionComponent } from './produccion/produccion.component';
import { ProduccionService } from './produccion/produccion.service';
import { TurnoComponent, TurnoEditComponent, TurnoListComponent } from './turno/turno.component';
import { TurnoService } from './turno/turno.service';
import { DescuentoComponent, DescuentoListComponent, EditDescuentoComponent } from './descuento/descuento.component';
import { DescuentoService } from '../turno/descuento/descuento.service';
import { IncapacidadComponent, EditIncapacidadComponent, IncapacidadListComponent } from '../turno/incapacidad/incapacidad.component';
import { IncapacidadService } from '../turno/incapacidad/incapacidad.service';

export const TurnoRoutes: Routes = [
    {
        path: '', children: [
            {
                path: 'turno', component: TurnoComponent, data: { miga: 'Turnos' }, children: [
                    { path: '', component: TurnoListComponent },
                    { path: ':id/edit', component: TurnoEditComponent, data: { miga: 'Editar' }, resolve: { item: TurnoService } }
                ]
            },
            {
                path: 'produccion', component: ProduccionComponent, data: { miga: 'Producciones' }, children: [
                    { path: '', component: ProduccionListComponent },
                    { path: ':id/edit', component: EditProduccionComponent, data: { miga: 'Editar' }, resolve: { item: ProduccionService } }
                ]
            },
            {
                path: 'descuento', component: DescuentoComponent, data: { miga: 'Descuentos de producción' }, children: [
                    { path: '', component: DescuentoListComponent },
                    { path: ':id/edit', component: EditDescuentoComponent, data: { miga: 'Editar' }, resolve: { item: DescuentoService } }
                ]
            },
            {
                path: 'incapacidad', component: IncapacidadComponent, data: { miga: 'Incapacidad' }, children: [
                    { path: '', component: IncapacidadListComponent },
                    { path: ':id/edit', component: EditIncapacidadComponent, data: { miga: 'Editar' }, resolve: { item: IncapacidadService } }
                ]
            }
        ]
    }

];

export const ProduccionMenuMeta: MenuMeta[] = [
    { title: 'Turnos', url: '/operacion/turno', icon: 'extension' },
    { title: 'Producción', url: '/operacion/produccion', icon: 'extension' },
    { title: 'Descuentos de producción', url: '/operacion/descuento', icon: 'extension' },
    { title: 'Incapacidad', url: '/operacion/incapacidad', icon: 'extension' },

];
