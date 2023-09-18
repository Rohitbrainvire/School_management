/** @odoo-module **/

import publicWidget from 'web.public.widget';
import core from 'web.core'

var Qweb = core.qweb
publicWidget.registry.formTemp = publicWidget.Widget.extend({
    selector: '#form_result',
    events: {
        'click #submit_button' : '_submit_button',
    },


    _submit_button: function(){
        console.log(this.$el,this.getSession())

        if(this.getSession().user_id){
            console.log('success')

            let name = this.$el.find('input#name')[0].value
            let email = this.$el.find('input#email')[0].value
            let message = this.$el.find('textarea#message')[0].value
            console.log(name,email,message)
            this._rpc({
                route: "/my_custom_page/data",
                params: {'name': name,
                         'email' : email,
                         'message': message,
                        }
            }).then((data) => {
                console.log(data,'Done')
            });

    }
    }
   
});
export default publicWidget.registry.formTemp;