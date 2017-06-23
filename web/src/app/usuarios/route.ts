import { Routes } from '@angular/router';
import { MenuMeta } from '../app.routing';
import { AsistenteComponent, AsistenteEditComponent, AsistenteListComponent } from './asistente/asistente.component';
<<<<<<< HEAD
import { AdminComponent } from './admin/admin.component';
import { AsistenteService } from './asistente/asistente.service';
=======
import { AdminComponent, EditAdminComponent, ListAdminComponent } from './admin/admin.component';
import { AsistenteService } from './asistente/asistente.service';
import { AdminService } from './admin/admin.service';
>>>>>>> a75b9556452a39ceaafc3ff96c271708205b741f

export const UsuariosRoutes: Routes = [
    {
        path: '', children: [
<<<<<<< HEAD
            { path: 'admin', component: AdminComponent },
            { path: 'asistente', component: AsistenteComponent, children: [
                { path: '', component: AsistenteListComponent},
                { path: ':id/edit', component: AsistenteEditComponent, resolve: { asistente: AsistenteService }}
            ]},
=======
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
>>>>>>> a75b9556452a39ceaafc3ff96c271708205b741f
        ]
    }

];

export const UsuariosMenuMeta: MenuMeta[] = [
    { title: 'Administrador', url: '/usuarios/admin', icon: 'account_box' },
    { title: 'Asistente', url: '/usuarios/asistente', icon: 'supervisor_account' },
];
