/** @odoo-module **/
odoo.define('custom_website.Dynamic', function (require) {
    const PublicWidget = require('web.public.widget');
    const rpc = require('web.rpc');


    PublicWidget.registry.custom_website = PublicWidget.Widget.extend({
        selector: '.custom_website',
        start: function () {
            rpc.query({
                route: '/dynamic',
                params: {
                    result : vals
                },
            }).then(function (result) {
                console.log(result)
                // this.$('#total_sold').text(result);
            });
        },
    });
    return PublicWidget.registry.custom_website;
    
 });