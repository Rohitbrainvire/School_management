from odoo import models, fields, api

class CreateSchoolInfoWizard(models.TransientModel):
    _name = 'create_school_info.wizard'
    _description = 'Create School Info Wizard'

    student_id = fields.Many2one('school.management.student', string="Student") 
    

    def cancel_admission(self):
        print(f"Admission is canceled. Reason: {self.reason_for_cancellation}")

    def cancel_admission(self):
        for admission in self:
            admission.student_id.unlink()