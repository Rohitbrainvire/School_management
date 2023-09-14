odoo.define("pos_training.Phone", function (require) {
  "use strict";
  const PartnerDetailsEdit = require("point_of_sale.PartnerDetailsEdit");
  const Registries = require("point_of_sale.Registries");

  const Phone = (PartnerDetailsEdit) =>
    class extends PartnerDetailsEdit {
        setup(){
            super.setup()
            this.changes.phone_number = this.props.partner.phone_number
        }
        async saveChanges(){
            const db = await this.env.services.rpc({
                model:"res.partner",
                method:"search_read",
                args:[[['phone_number','=',this.changes.phone_number],['id','!=',this.props.partner.id]]]
            })
            if(db>0 && this.changes.phone_number != null){
                this.showNotification(`Mobile Number already registered for ${loadedData[0].name}!!`)
            }
            else{
                super.saveChanges()
            }
        }

    }
    Phone.template="custom.mobile.res"
    Registries.Component.extend(PartnerDetailsEdit,Phone)
})