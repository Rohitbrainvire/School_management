/* @odoo-module */

import publicWidget from 'web.public.widget';

publicWidget.registry.EmployeeInformation = publicWidget.Widget.extend({
    selector: '.employees-information',
    start() {
        let employeeRow = this.el.querySelector('#employees-information-row');

        if (employeeRow) {
            this._rpc({
                route: '/employees',  
                params: {},           
            }).then(data => {
                let html = '';
                console.log(data)
                data.forEach(emp => {
                    html += `<div class="col-lg-3 mb-5">
                        <div class="d-flex align-items-center">
                            <div class="img-container mr-3 rounded">
                                <img class="employee-image rounded" src="data:image/png;base64,${emp.employee_image}"/>
                            </div>
                            <div>
                                <h5 class="mb-0">${emp.employee_name || ''}</h5>
                                <div>${emp.employee_phone_number || ''}</div>
                                <div>${emp.employee_work_exp || ''}</div>
                                <div>${emp.employee_city || ''}</div>
                            </div>
                        </div>
                    </div>`;
                });
                employeeRow.innerHTML = html;
            });
        }
    },
});

export default publicWidget.registry.EmployeeInformation;