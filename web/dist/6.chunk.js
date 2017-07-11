webpackJsonp([6],{

/***/ "../../../../../src/app/configuracion/configuracion.module.ts":
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
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6__cargo_cargo_component__ = __webpack_require__("../../../../../src/app/configuracion/cargo/cargo.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_7__tipocontrato_tipocontrato_component__ = __webpack_require__("../../../../../src/app/configuracion/tipocontrato/tipocontrato.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_8__general_general_component__ = __webpack_require__("../../../../../src/app/configuracion/general/general.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_9__cargo_cargo_service__ = __webpack_require__("../../../../../src/app/configuracion/cargo/cargo.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_10__configuracion_route__ = __webpack_require__("../../../../../src/app/configuracion/configuracion.route.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_11__tipocontrato_tipocontrato_service__ = __webpack_require__("../../../../../src/app/configuracion/tipocontrato/tipocontrato.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_12__general_general_service__ = __webpack_require__("../../../../../src/app/configuracion/general/general.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_13__tarifario_tarifario_component__ = __webpack_require__("../../../../../src/app/configuracion/tarifario/tarifario.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_14__unidadproduccion_unidadproduccion_component__ = __webpack_require__("../../../../../src/app/configuracion/unidadproduccion/unidadproduccion.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_15__unidadproduccion_unidadproduccion_service__ = __webpack_require__("../../../../../src/app/configuracion/unidadproduccion/unidadproduccion.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_16__tarifario_tarifario_service__ = __webpack_require__("../../../../../src/app/configuracion/tarifario/tarifario.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_17__banco_banco_component__ = __webpack_require__("../../../../../src/app/configuracion/banco/banco.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_18__banco_banco_service__ = __webpack_require__("../../../../../src/app/configuracion/banco/banco.service.ts");
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "ConfiguracionModule", function() { return ConfiguracionModule; });
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};



















var ConfiguracionModule = (function () {
    function ConfiguracionModule() {
    }
    return ConfiguracionModule;
}());
ConfiguracionModule = __decorate([
    __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_0__angular_core__["NgModule"])({
        imports: [
            __WEBPACK_IMPORTED_MODULE_2__angular_common__["a" /* CommonModule */],
            __WEBPACK_IMPORTED_MODULE_5__lib_lib_module__["a" /* LibModule */],
            __WEBPACK_IMPORTED_MODULE_3__angular_forms__["FormsModule"],
            __WEBPACK_IMPORTED_MODULE_3__angular_forms__["ReactiveFormsModule"],
            __WEBPACK_IMPORTED_MODULE_4_angular_date_value_accessor__["DateValueAccessorModule"],
            __WEBPACK_IMPORTED_MODULE_1__angular_router__["a" /* RouterModule */].forChild(__WEBPACK_IMPORTED_MODULE_10__configuracion_route__["a" /* ConfiguracionRoutes */])
        ],
        declarations: [
            __WEBPACK_IMPORTED_MODULE_6__cargo_cargo_component__["a" /* CargoComponent */],
            __WEBPACK_IMPORTED_MODULE_6__cargo_cargo_component__["b" /* CargoListComponent */],
            __WEBPACK_IMPORTED_MODULE_6__cargo_cargo_component__["c" /* EditCargoComponent */],
            __WEBPACK_IMPORTED_MODULE_7__tipocontrato_tipocontrato_component__["a" /* TipocontratoComponent */],
            __WEBPACK_IMPORTED_MODULE_7__tipocontrato_tipocontrato_component__["b" /* TipoContratoListComponent */],
            __WEBPACK_IMPORTED_MODULE_7__tipocontrato_tipocontrato_component__["c" /* EditTipoContratoComponent */],
            __WEBPACK_IMPORTED_MODULE_8__general_general_component__["a" /* GeneralComponent */],
            __WEBPACK_IMPORTED_MODULE_8__general_general_component__["b" /* EditGeneralComponent */],
            __WEBPACK_IMPORTED_MODULE_13__tarifario_tarifario_component__["a" /* TarifarioComponent */],
            __WEBPACK_IMPORTED_MODULE_13__tarifario_tarifario_component__["b" /* TarifarioListComponent */],
            __WEBPACK_IMPORTED_MODULE_13__tarifario_tarifario_component__["c" /* EditTarifarioComponent */],
            __WEBPACK_IMPORTED_MODULE_14__unidadproduccion_unidadproduccion_component__["a" /* UnidadproduccionComponent */],
            __WEBPACK_IMPORTED_MODULE_14__unidadproduccion_unidadproduccion_component__["b" /* UnidadProduccionListComponent */],
            __WEBPACK_IMPORTED_MODULE_14__unidadproduccion_unidadproduccion_component__["c" /* EditUnidadProduccionComponent */],
            __WEBPACK_IMPORTED_MODULE_17__banco_banco_component__["a" /* BancoComponent */],
            __WEBPACK_IMPORTED_MODULE_17__banco_banco_component__["b" /* EditBancoComponent */],
            __WEBPACK_IMPORTED_MODULE_17__banco_banco_component__["c" /* BancoListComponent */]
        ],
        providers: [
            __WEBPACK_IMPORTED_MODULE_9__cargo_cargo_service__["a" /* CargoService */],
            __WEBPACK_IMPORTED_MODULE_11__tipocontrato_tipocontrato_service__["a" /* TipoContratoService */],
            __WEBPACK_IMPORTED_MODULE_12__general_general_service__["a" /* ConfiguracionService */],
            __WEBPACK_IMPORTED_MODULE_15__unidadproduccion_unidadproduccion_service__["a" /* UnidadProduccionService */],
            __WEBPACK_IMPORTED_MODULE_16__tarifario_tarifario_service__["a" /* TarifarioService */],
            __WEBPACK_IMPORTED_MODULE_18__banco_banco_service__["a" /* BancoService */]
        ]
    })
], ConfiguracionModule);

//# sourceMappingURL=configuracion.module.js.map

/***/ })

});
//# sourceMappingURL=6.chunk.js.map