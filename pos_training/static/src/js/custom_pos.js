odoo.define("pos_training.Note", function (require) {
  "use strict";
  const ProductScreen = require("point_of_sale.ProductScreen");
  const Registries = require("point_of_sale.Registries");

  const Note = (ProductScreen) =>
    class extends ProductScreen {
      async onClick() {
        const order_obj = this.env.pos.get_order()
            const { confirmed, payload : payload_note } = await this.showPopup('OrderPopUp',{
              initial_note:order_obj.get_note()
            });
            if (confirmed){
              order_obj.set_note(payload_note)
            }
        }
    };
  Note.template = "pos_training.Note";
  Registries.Component.extend(ProductScreen, Note);
  return Note;
});