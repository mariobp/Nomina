import { Routes } from '@angular/router';
import { MenuMeta } from '../app.routing';
import { CargoComponent, CargoListComponent, EditCargoComponent } from './cargo/cargo.component';
import { GeneralComponent, EditGeneralComponent } from './general/general.component';
import { TipocontratoComponent, TipoContratoListComponent, EditTipoContratoComponent } from './tipocontrato/tipocontrato.component';
import { TarifarioComponent } from './tarifario/tarifario.component';
import { CargoService } from './cargo/cargo.service';
import { TipoContratoService } from './tipocontrato/tipocontrato.service';
import { UnidadproduccionComponent, EditUnidadProduccionComponent, UnidadProduccionListComponent} from './unidadproduccion/unidadproduccion.component';
import { UnidadProduccionService } from './unidadproduccion/unidadproduccion.service';

export const ConfiguracionRoutes: Routes = [
    {
        path: '', children: [
            {
                path: 'cargos', component: CargoComponent, children: [
                    { path: '', component: CargoListComponent },
                    { path: ':id/edit', component: EditCargoComponent, resolve: { item: CargoService } }
                ]
            },
            {
                path: 'general', component: GeneralComponent, children: [
                    { path: '', component: EditGeneralComponent }
                ]
            },
            {
                path: 'tipo/contrato', component: TipocontratoComponent, children: [
                    { path: '', component: TipoContratoListComponent },
                    { path: ':id/edit', component: EditTipoContratoComponent, resolve: { item: TipoContratoService } }
                ]
            },
            {
                path: 'unidad/produccion', component: UnidadproduccionComponent, children: [
                    { path: '', component: UnidadProduccionListComponent },
                    { path: ':id/edit', component: EditUnidadProduccionComponent, resolve: { item: UnidadProduccionService } }
                ]
            },
            {
                path: 'tarifario', component: TarifarioComponent
            }
        ]
    }
]

export const ConfiguracionMenuMeta: MenuMeta[] = [
    { title: 'Cargos', url: '/configuracion/cargos', icon: 'extension' },
    { title: 'Tipos de Contrato', url: '/configuracion/tipo/contrato', icon: 'extension' },
    { title: 'Configuración General', url: '/configuracion/general', icon: 'extension' },
    { title: 'Unidad de producción', url: '/configuracion/unidad/produccion', icon: 'extension' },
    { title: 'Tarifario', url: '/configuracion/tarifario', icon: 'extension' }
]
