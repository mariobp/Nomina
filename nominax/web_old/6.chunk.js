webpackJsonp([6],{

/***/ "../../../../../src/app/incapacidad/incapacidad.module.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/@angular/core.es5.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_common__ = __webpack_require__("../../../common/@angular/common.es5.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__angular_router__ = __webpack_require__("../../../router/@angular/router.es5.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__lib_lib_module__ = __webpack_require__("../../../../../src/lib/lib.module.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__angular_forms__ = __webpack_require__("../../../forms/@angular/forms.es5.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__tipo_tipo_incapacidad_component__ = __webpack_require__("../../../../../src/app/incapacidad/tipo/tipo.incapacidad.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6__pago_pago_incapacidad_component__ = __webpack_require__("../../../../../src/app/incapacidad/pago/pago.incapacidad.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_7__tipo_tipo_incapacidad_service__ = __webpack_require__("../../../../../src/app/incapacidad/tipo/tipo.incapacidad.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_8__pago_pago_incapacidad_service__ = __webpack_require__("../../../../../src/app/incapacidad/pago/pago.incapacidad.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_9__route__ = __webpack_require__("../../../../../src/app/incapacidad/route.ts");
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "IncapacidadModule", function() { return IncapacidadModule; });
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};










var IncapacidadModule = (function () {
    function IncapacidadModule() {
    }
    return IncapacidadModule;
}());
IncapacidadModule = __decorate([
    __webpack_require__.i(__WEBPACK_IMPORTED_MODULE_0__angular_core__["NgModule"])({
        imports: [
            __WEBPACK_IMPORTED_MODULE_3__lib_lib_module__["a" /* LibModule */],
            __WEBPACK_IMPORTED_MODULE_4__angular_forms__["FormsModule"],
            __WEBPACK_IMPORTED_MODULE_1__angular_common__["a" /* CommonModule */],
            __WEBPACK_IMPORTED_MODULE_4__angular_forms__["ReactiveFormsModule"],
            __WEBPACK_IMPORTED_MODULE_2__angular_router__["a" /* RouterModule */].forChild(__WEBPACK_IMPORTED_MODULE_9__route__["a" /* IncapacidadRoutes */])
        ],
        declarations: [
            __WEBPACK_IMPORTED_MODULE_5__tipo_tipo_incapacidad_component__["a" /* TipoIncapacidadComponent */],
            __WEBPACK_IMPORTED_MODULE_5__tipo_tipo_incapacidad_component__["b" /* TipoIncapacidadListComponent */],
            __WEBPACK_IMPORTED_MODULE_5__tipo_tipo_incapacidad_component__["c" /* TipoIncapacidadEditComponent */],
            __WEBPACK_IMPORTED_MODULE_6__pago_pago_incapacidad_component__["a" /* PagoIncapacidadComponent */],
            __WEBPACK_IMPORTED_MODULE_6__pago_pago_incapacidad_component__["b" /* PagoIncapacidadEditComponent */],
            __WEBPACK_IMPORTED_MODULE_6__pago_pago_incapacidad_component__["c" /* PagoIncapacidadListComponent */]
        ],
        providers: [
            __WEBPACK_IMPORTED_MODULE_7__tipo_tipo_incapacidad_service__["a" /* TipoIncapacidadService */],
            __WEBPACK_IMPORTED_MODULE_8__pago_pago_incapacidad_service__["a" /* PagoIncapacidadService */]
        ]
    })
], IncapacidadModule);

//# sourceMappingURL=incapacidad.module.js.map

/***/ })

});
//# sourceMappingURL=6.chunk.js.map