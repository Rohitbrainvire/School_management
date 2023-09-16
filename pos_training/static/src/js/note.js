odoo.define("pos_training.OrderPopUp", function (require) {
  "use strict";
  const AbstractAwaitablePopup = require("point_of_sale.AbstractAwaitablePopup");
  const { Order } = require("point_of_sale.models")
  const { useState } = owl;
  const Registries = require("point_of_sale.Registries");

  class OrderPopUp extends AbstractAwaitablePopup {
    setup() {
      super.setup()
      this.state = useState({ note: this.props.initial_note })
    }

    getPayload() {
      return this.state.note
    }
  }

  OrderPopUp.template = "pos_training.OrderPopUp";

  Registries.Component.add(OrderPopUp);

  const LocalData = (Order) => class extends Order {

    export_as_JSON() {
      const json = super.export_as_JSON()
      json.json_note = this.order_note
      return json
    }
    init_from_JSON(json) {
      super.init_from_JSON(...arguments)
      this.set_note(json.json_note)
    }
    set_note(note) {
      this.order_note = note
    }
    get_note() {
      return this.order_note
    }
  }

  Registries.Model.extend(Order, LocalData);
});