/* @odoo-module */
import { registry } from "@web/core/registry";
import { Component, useState, onWillDestroy } from "@odoo/owl";

function useMouse() {
   const position = useState({ x: 0, y: 0 });

   function update(e) {
      position.x = e.clientX;
      position.y = e.clientY;
   }
   window.addEventListener('mousemove', update);
   onWillDestroy(() => {
      window.removeEventListener('mousemove', update);
   });

   return position;
}


// Main root component
class Root extends Component {
   static template = "Root";

   setup() {
      this.counter = useState({ value: 0 });
      this.mouse = useMouse();
   }

   increment() {
      this.counter.value++;
   }
}


registry.category("actions").add("action_component", Root);