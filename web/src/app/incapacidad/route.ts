import { Routes } from '@angular/router';
import { MenuMeta } from '../app.routing';
import { TipoIncapacidadComponent, TipoIncapacidadListComponent, TipoIncapacidadEditComponent } from './tipo/tipo.incapacidad.component';
import { TipoIncapacidadService } from './tipo/tipo.incapacidad.service';
import { PagoIncapacidadComponent, PagoIncapacidadListComponent, PagoIncapacidadEditComponent } from './pago/pago.incapacidad.component';
import { PagoIncapacidadService } from './pago/pago.incapacidad.service';

export const IncapacidadRoutes: Routes = [
    {
        path: '', children: [
            {
                path: 'tipo', component: TipoIncapacidadComponent, data: { miga: 'Tipo de incapacidad' }, children: [
                    { path: '', component: TipoIncapacidadListComponent },
                    {
                        path: ':id/edit', component: TipoIncapacidadEditComponent,
                        data: { miga: 'Editar' }, resolve: { item: TipoIncapacidadService }
                    }
                ]
            },
            {
                path: 'pago', component: PagoIncapacidadComponent, data: { miga: 'Pago de incapacidad' }, children: [
                    { path: '', component: PagoIncapacidadListComponent },
                    {
                        path: ':id/edit', component: PagoIncapacidadEditComponent,
                        data: { miga: 'Editar' }, resolve: { item: PagoIncapacidadService }
                    }
                ]
            }
        ]
    }

];

export const IncapacidadMenuMeta: MenuMeta[] = [
    { title: 'Tipo', url: '/incapacidad/tipo', icon: 'extension' },
    { title: 'Pago', url: '/incapacidad/pago', icon: 'extension' }
];
