/** @odoo-module **/

import publicWidget from 'web.public.widget';
import core from 'web.core'

var Qweb = core.qweb
publicWidget.registry.formTemp = publicWidget.Widget.extend({
    selector: '#custom_sec',
    events: {
        'click #submit_button': '_submit_button',
        'click button#sign_button': function () {
            var link = $('button#sign_button').data('link');
            if (link) {
                window.location.href = link;
            }
        }
    },
    _submit_button: function () {
        // console.log(this.$el, this.getSession())

       
            console.log('success')

            function custom_pop(el, title = "title", msg = "nothing", button_name = null, link = null) {
                var popup_el = el.find('div#exampleModal');
                var popup_title = el.find('h1#exampleModalLabel')[0]
                var popup_msg = el.find('div#popup_body')[0]
                var popup_ok = el.find('button#sign_button')
                popup_title.innerHTML = title
                popup_msg.innerHTML = msg
                if (link != null && button_name != null) {
                    popup_ok[0].innerHTML = button_name
                    popup_ok.attr('data-link', link);
                } else {
                    popup_ok[0].style.display = 'none'
                }
                popup_el.modal('show');
            }

            let name = this.$el.find('input#name')[0].value
            let email = this.$el.find('input#email')[0].value
            let message = this.$el.find('textarea#message')[0].value
            let profession = this.$el.find('select#profession')[0].value
            console.log(name, email, message, profession)

            if (this.getSession().user_id) {
                this._rpc({
                    route: "/my_custom_page/data",
                    params: {
                        'name': name,
                        'email': email,
                        'message': message,
                        'profession': profession,
                    }
                }).then((data) => {
                    custom_pop(this.$el, 'success', 'data saved')
                });
            } else {
                custom_pop(this.$el, 'Alert', 'Please login before submit', 'login', 'http://localhost:8069/web/login')
            }
        
    }
});
export default publicWidget.registry.formTemp;