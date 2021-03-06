import { Routes } from '@angular/router';
import { MenuMeta } from '../app.routing';
import { NominaComponent, NominaListComponent } from './nomina/nomina.component';
import { DescuentoComponent, DescuentoListComponent, DescuentoEditComponent } from './descuento/descuento.component';
import { CorteComponent, CorteListComponent, CorteEditComponent } from './corte/corte.component';
import { NominaService } from './nomina/nomina.service';
import { CorteService } from './corte/corte.service';
import { DescuentoService } from './descuento/descuento.service';


export const NominaRoutes: Routes = [
    {
        path: '', children: [
            {
                path: 'nomina', component: CorteComponent, children: [
                    { path: '', component: CorteListComponent },
                    {
                        path: ':id/edit', component: CorteEditComponent, resolve: { item: CorteService }, children: [
                            { path: '', component: NominaListComponent },
                            {
                                path: '', component: DescuentoComponent, outlet: 'descuento', children: [
                                    { path: '', component: DescuentoListComponent },
                                    { path: ':id/edit', component: DescuentoEditComponent, resolve: { item: DescuentoService } }
                                ]
                            }
                        ]
                    },

                ]
            }
        ]
    }

];
