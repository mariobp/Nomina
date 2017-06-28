import { Routes } from '@angular/router';
import { MenuMeta } from '../app.routing';

import { PensionComponent, PensionListComponent, EditPensionComponent } from './pension/pension.component';
import { EpsComponent, EpsListComponent, EditEpsComponent } from './eps/eps.component';
import { CompensacionComponent, CompensacionListComponent, EditCompensacionComponent } from './compensacion/compensacion.component';
import { CesantiasComponent, CesantiasListComponent, EditCesantiasComponent } from './cesantias/cesantias.component';
import { CesantiasService } from './cesantias/cesantias.service';
import { CompensacionService } from './compensacion/compensacion.service';
import { EpsService } from './eps/eps.service';
import { PensionService } from './pension/pension.service';

export const ObligacionesRoutes: Routes = [
    {
        path: '', children: [
            { path: 'pension', component: PensionComponent , children:[
                { path: '', component: PensionListComponent },
                { path: ':id/edit', component: EditPensionComponent, resolve: { item: PensionService } }
            ]},
            { path: 'eps', component: EpsComponent, children: [
                { path: '', component: EpsListComponent } ,
                { path: ':id/edit', component: EditEpsComponent, resolve: { item: EpsService } }
            ]},
            { path: 'compensacion', component: CompensacionComponent, children: [
                { path: '', component: CompensacionListComponent},
                { path: ':id/edit', component: EditCompensacionComponent, resolve: { item: CompensacionService } }
            ]},
            { path: 'cesantias', component: CesantiasComponent, children:[
                { path: '', component: CesantiasListComponent},
                { path: ':id/edit', component: EditCesantiasComponent, resolve: { item: CesantiasService } }
            ] }
        ]
    }

];

export const ObligacionesMenuMeta: MenuMeta[] = [
    { title: 'Pensión', url: '/obligaciones/pension', icon: 'extension' },
    { title: 'Eps', url: '/obligaciones/eps', icon: 'extension' },
    { title: 'Caja de Compensación', url: '/obligaciones/compensacion', icon: 'extension' },
    { title: 'Cesantías', url: '/obligaciones/cesantias', icon: 'extension' },
];
