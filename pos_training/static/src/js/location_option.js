odoo.define("pos_order.LocationList", function (require) {
    "use strict";
    const ProductScreen = require("point_of_sale.ProductScreen");
    const PosComponent = require('point_of_sale.PosComponent');
    const { useListener } = require("@web/core/utils/hooks");
    const Registries = require("point_of_sale.Registries");

    class LocationOption extends PosComponent{

        setup(){
            super.setup();
            useListener('click', this.onClick);
            this.all_order = this.env.pos.get_order();
            this.locations_from_config = this.env.pos.locations.filter((method) => this.env.pos.config.selected_location.includes(method.id));

        }
        get pre_select_loc(){
            if (this.all_order.selected_location){
                return this.all_order.selected_location.id
            }
            return false
        }
        get selected_loc(){
            let loc = this.all_order.get_location()
            return loc ? loc.location : false
        }
        async onClick() {
            const selectedList = this.locations_from_config.map(locationoption => ({
                id: locationoption.id,
                label: locationoption.location,
                isSelected: locationoption.id === this.pre_select_loc,
                item: locationoption,
            }));
           
            const { confirmed, payload: selectedLocation } = await this.showPopup(
                'LocationShowup',
                {
                    list: selectedList,
                }
            );

            if (confirmed) {
                this.all_order.set_location(selectedLocation);
            }

        }
    }

    ProductScreen.addControlButton({
        component: LocationOption,
    })


    LocationOption.template = 'LocationOption';
    Registries.Component.add(LocationOption);

});