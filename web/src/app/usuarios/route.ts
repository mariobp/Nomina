import { Routes } from '@angular/router';
import { MenuMeta } from '../app.routing';
import { AsistenteComponent, AsistenteEditComponent, AsistenteListComponent } from './asistente/asistente.component';
import { AdminComponent, EditAdminComponent, ListAdminComponent } from './admin/admin.component';
import { AsistenteService } from './asistente/asistente.service';
import { AdminService } from './admin/admin.service';

export const UsuariosRoutes: Routes = [
    {
        path: '', children: [
            {
                path: 'admin', component: AdminComponent, children: [
                    { path: '', component: ListAdminComponent },
                    { path: ':id/edit', component: EditAdminComponent, resolve: { item: AdminService } }
                ]
            },
            {
                path: 'asistente', component: AsistenteComponent, children: [
                    { path: '', component: AsistenteListComponent },
                    { path: ':id/edit', component: AsistenteEditComponent, resolve: { asistente: AsistenteService } }
                ]
            },
        ]
    }

];

export const UsuariosMenuMeta: MenuMeta[] = [
    { title: 'Administrador', url: '/usuarios/admin', icon: 'account_box' },
    { title: 'Asistente', url: '/usuarios/asistente', icon: 'supervisor_account' },
];
