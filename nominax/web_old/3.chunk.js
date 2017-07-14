webpackJsonp([3],{

/***/ "../../../../../src/app/usuarios/usuarios.module.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/@angular/core.es5.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_router__ = __webpack_require__("../../../router/@angular/router.es5.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__angular_common__ = __webpack_require__("../../../common/@angular/common.es5.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__angular_forms__ = __webpack_require__("../../../forms/@angular/forms.es5.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4_angular_date_value_accessor__ = __webpack_require__("../../../../angular-date-value-accessor/index.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4_angular_date_value_accessor___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_4_angular_date_value_accessor__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__lib_lib_module__ = __webpack_require__("../../../../../src/lib/lib.module.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6__route__ = __webpack_require__("../../../../../src/app/usuarios/route.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_7__asistente_asistente_service__ = __webpack_require__("../../../../../src/app/usuarios/asistente/asistente.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_8__asistente_asistente_component__ = __webpack_require__("../../../../../src/app/usuarios/asistente/asistente.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_9__admin_admin_component__ = __webpack_require__("../../../../../src/app/usuarios/admin/admin.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_10__admin_admin_service__ = __webpack_require__("../../../../../src/app/usuarios/admin/admin.service.ts");
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "UsuariosModule", function() { return UsuariosModule; });
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};











var UsuariosModule = (function () {
    function UsuariosModule() {
    }
    return UsuariosModule;
}());
UsuariosModule = __decorate([
    __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_0__angular_core__["NgModule"])({
        imports: [
            __WEBPACK_IMPORTED_MODULE_2__angular_common__["a" /* CommonModule */],
            __WEBPACK_IMPORTED_MODULE_5__lib_lib_module__["a" /* LibModule */],
            __WEBPACK_IMPORTED_MODULE_3__angular_forms__["FormsModule"],
            __WEBPACK_IMPORTED_MODULE_3__angular_forms__["ReactiveFormsModule"],
            __WEBPACK_IMPORTED_MODULE_4_angular_date_value_accessor__["DateValueAccessorModule"],
            __WEBPACK_IMPORTED_MODULE_1__angular_router__["a" /* RouterModule */].forChild(__WEBPACK_IMPORTED_MODULE_6__route__["a" /* UsuariosRoutes */])
        ],
        declarations: [
            __WEBPACK_IMPORTED_MODULE_8__asistente_asistente_component__["a" /* AsistenteComponent */],
            __WEBPACK_IMPORTED_MODULE_8__asistente_asistente_component__["b" /* AsistenteListComponent */],
            __WEBPACK_IMPORTED_MODULE_8__asistente_asistente_component__["c" /* AsistenteEditComponent */],
            __WEBPACK_IMPORTED_MODULE_9__admin_admin_component__["a" /* AdminComponent */],
            __WEBPACK_IMPORTED_MODULE_9__admin_admin_component__["b" /* EditAdminComponent */],
            __WEBPACK_IMPORTED_MODULE_9__admin_admin_component__["c" /* ListAdminComponent */]
        ],
        providers: [
            __WEBPACK_IMPORTED_MODULE_7__asistente_asistente_service__["a" /* AsistenteService */],
            __WEBPACK_IMPORTED_MODULE_10__admin_admin_service__["a" /* AdminService */]
        ]
    })
], UsuariosModule);

//# sourceMappingURL=usuarios.module.js.map

/***/ })

});
//# sourceMappingURL=3.chunk.js.map