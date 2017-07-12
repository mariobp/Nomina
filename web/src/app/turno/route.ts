import { Routes } from '@angular/router';
import { MenuMeta } from '../app.routing';
import { ProduccionComponent, ProduccionListComponent, EditProduccionComponent } from './produccion/produccion.component';
import { ProduccionService } from './produccion/produccion.service';
import { TurnoComponent, TurnoEditComponent, TurnoListComponent } from './turno/turno.component';
import { TurnoService } from './turno/turno.service';

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
                path: 'produccion', component: ProduccionComponent, data: { miga: 'Producciónes' }, children: [
                    { path: '', component: ProduccionListComponent },
                    { path: ':id/edit', component: EditProduccionComponent, data: { miga: 'Editar' }, resolve: { item: ProduccionService } }
                ]
            }
        ]
    }

];

export const ProduccionMenuMeta: MenuMeta[] = [
    { title: 'Turnos', url: '/produccion/turno', icon: 'extension' },
    { title: 'Producción', url: '/produccion/produccion', icon: 'extension' },
];
