"use strict";
var router_1 = require('@angular/router');
var component1_component_1 = require("./component1.component");
var component2_component_1 = require("./component2.component");
var routes = [
    { path: '', redirectTo: '/component1', pathMatch: 'full' },
    { path: 'component1', component: component1_component_1.Component1Component },
    { path: 'component2', component: component2_component_1.Component2Component }
];
exports.appRouterProviders = [
    router_1.provideRouter(routes)
];
//# sourceMappingURL=app.route.js.map