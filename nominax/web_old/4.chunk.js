webpackJsonp([4],{

/***/ "../../../../../src/app/turno/turno.module.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/@angular/core.es5.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_router__ = __webpack_require__("../../../router/@angular/router.es5.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__angular_common__ = __webpack_require__("../../../common/@angular/common.es5.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__angular_forms__ = __webpack_require__("../../../forms/@angular/forms.es5.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__angular_material__ = __webpack_require__("../../../material/@angular/material.es5.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__lib_lib_module__ = __webpack_require__("../../../../../src/lib/lib.module.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6__turno_turno_component__ = __webpack_require__("../../../../../src/app/turno/turno/turno.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_7__turno_turno_service__ = __webpack_require__("../../../../../src/app/turno/turno/turno.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_8__empleados_empleado_empleado_service__ = __webpack_require__("../../../../../src/app/empleados/empleado/empleado.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_9__route__ = __webpack_require__("../../../../../src/app/turno/route.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_10__produccion_produccion_component__ = __webpack_require__("../../../../../src/app/turno/produccion/produccion.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_11__produccion_produccion_service__ = __webpack_require__("../../../../../src/app/turno/produccion/produccion.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_12__configuracion_unidadproduccion_unidadproduccion_service__ = __webpack_require__("../../../../../src/app/configuracion/unidadproduccion/unidadproduccion.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_13__configuracion_cargo_cargo_service__ = __webpack_require__("../../../../../src/app/configuracion/cargo/cargo.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_14__descuento_descuento_component__ = __webpack_require__("../../../../../src/app/turno/descuento/descuento.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_15__turno_descuento_descuento_service__ = __webpack_require__("../../../../../src/app/turno/descuento/descuento.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_16__incapacidad_incapacidad_component__ = __webpack_require__("../../../../../src/app/turno/incapacidad/incapacidad.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_17__incapacidad_incapacidad_service__ = __webpack_require__("../../../../../src/app/turno/incapacidad/incapacidad.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_18__incapacidad_tipo_tipo_incapacidad_service__ = __webpack_require__("../../../../../src/app/incapacidad/tipo/tipo.incapacidad.service.ts");
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "TurnoModule", function() { return TurnoModule; });
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};



















var TurnoModule = (function () {
    function TurnoModule() {
    }
    return TurnoModule;
}());
TurnoModule = __decorate([
    __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_0__angular_core__["NgModule"])({
        imports: [
            __WEBPACK_IMPORTED_MODULE_5__lib_lib_module__["a" /* LibModule */],
            __WEBPACK_IMPORTED_MODULE_3__angular_forms__["FormsModule"],
            __WEBPACK_IMPORTED_MODULE_2__angular_common__["a" /* CommonModule */],
            __WEBPACK_IMPORTED_MODULE_4__angular_material__["a" /* MdInputModule */],
            __WEBPACK_IMPORTED_MODULE_3__angular_forms__["ReactiveFormsModule"],
            __WEBPACK_IMPORTED_MODULE_4__angular_material__["b" /* MdAutocompleteModule */],
            __WEBPACK_IMPORTED_MODULE_1__angular_router__["a" /* RouterModule */].forChild(__WEBPACK_IMPORTED_MODULE_9__route__["a" /* TurnoRoutes */])
        ],
        declarations: [
            __WEBPACK_IMPORTED_MODULE_6__turno_turno_component__["a" /* TurnoComponent */],
            __WEBPACK_IMPORTED_MODULE_6__turno_turno_component__["b" /* TurnoEditComponent */],
            __WEBPACK_IMPORTED_MODULE_6__turno_turno_component__["c" /* TurnoListComponent */],
            __WEBPACK_IMPORTED_MODULE_10__produccion_produccion_component__["a" /* ProduccionComponent */],
            __WEBPACK_IMPORTED_MODULE_10__produccion_produccion_component__["b" /* ProduccionListComponent */],
            __WEBPACK_IMPORTED_MODULE_10__produccion_produccion_component__["c" /* EditProduccionComponent */],
            __WEBPACK_IMPORTED_MODULE_14__descuento_descuento_component__["a" /* DescuentoComponent */],
            __WEBPACK_IMPORTED_MODULE_14__descuento_descuento_component__["b" /* DescuentoListComponent */],
            __WEBPACK_IMPORTED_MODULE_14__descuento_descuento_component__["c" /* EditDescuentoComponent */],
            __WEBPACK_IMPORTED_MODULE_16__incapacidad_incapacidad_component__["a" /* IncapacidadComponent */],
            __WEBPACK_IMPORTED_MODULE_16__incapacidad_incapacidad_component__["b" /* EditIncapacidadComponent */],
            __WEBPACK_IMPORTED_MODULE_16__incapacidad_incapacidad_component__["c" /* IncapacidadListComponent */]
        ],
        providers: [
            __WEBPACK_IMPORTED_MODULE_7__turno_turno_service__["a" /* TurnoService */],
            __WEBPACK_IMPORTED_MODULE_8__empleados_empleado_empleado_service__["a" /* EmpleadoService */],
            __WEBPACK_IMPORTED_MODULE_11__produccion_produccion_service__["a" /* ProduccionService */],
            __WEBPACK_IMPORTED_MODULE_12__configuracion_unidadproduccion_unidadproduccion_service__["a" /* UnidadProduccionService */],
            __WEBPACK_IMPORTED_MODULE_13__configuracion_cargo_cargo_service__["a" /* CargoService */],
            __WEBPACK_IMPORTED_MODULE_15__turno_descuento_descuento_service__["a" /* DescuentoService */],
            __WEBPACK_IMPORTED_MODULE_17__incapacidad_incapacidad_service__["a" /* IncapacidadService */],
            __WEBPACK_IMPORTED_MODULE_18__incapacidad_tipo_tipo_incapacidad_service__["a" /* TipoIncapacidadService */]
        ]
    })
], TurnoModule);

//# sourceMappingURL=turno.module.js.map

/***/ })

});
//# sourceMappingURL=4.chunk.js.map