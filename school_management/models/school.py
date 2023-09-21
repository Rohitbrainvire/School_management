from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime
from odoo.tools.translate import _

class SchoolManagement(models.Model):
    _name = 'school.management.student'
    _description = 'Student'
    _inherit = ['mail.thread']
    _rec_name = 'enr_number'

    # Grade levels for the student
    GRADE_LEVELS = [
        ('jr_kg', 'Jr. KG'),        
        ('sr_kg', 'Sr. KG'),
        ('1', '1st'),
        ('2', '2nd'),
        ('3', '3rd'),   
        ('4', '4th'),
        ('5', '5th'),
        ('6', '6th'),
        ('7', '7th'),
        ('8', '8th'),
        ('9', '9th'),
        ('10', '10th'),
        ('11', '11th'),
        ('12', '12th'),
    ]
    enr_number=fields.One2many('school.management.library') 
    DIVISION_OPTIONS = [
        ('a', 'A'),
        ('b', 'B')
    ]

    fee_status = fields.Selection([
        ('paid', 'Paid'), 
        ('pending', 'Pending')
    ], string='Fee Status')

    # Stream options for the student
    STREAM_OPTIONS = [
        ('science', 'Science'),
        ('commerce', 'Commerce'),
        ('arts', 'Arts')
    ]

    # Fields for the student model
    name_in_previous_school = fields.Char(string='Name of Previous School')
    admission_date_of_last_school = fields.Date(string='Admission Date')
    leaving_date_of_last_school = fields.Date(string='Leaving Date')
    handle=fields.Integer()
    gender = fields.Selection([
        ('Male', 'male'),
        ('Female', 'female'),
        ('Other', 'other'),
    ], string='Gender')
    kanban_edit=fields.Integer()
    student_name = fields.Many2one('school.management.student', string = 'Search')
    name = fields.Char(string='Name',tracking=True)
    standard = fields.Selection(selection=GRADE_LEVELS, string='Standard', tracking=True)
    class_teacher = fields.Many2one('school.management.teacher', compute='_depends_division', string='Class Teacher', store=True)
    division = fields.Selection(selection=DIVISION_OPTIONS, string='Division', tracking=True)
    roll_number = fields.Integer(string='Roll Number',help= 'Enter the roll number',tracking=True,copy=False)
    enr_number= fields.Char(string='Unique Enrollment Number', required=True,readonly=True, default=lambda self: _('New'),copy = False)
    image = fields.Binary(string='Profile Image')
    country_id = fields.Many2one('res.country', default=lambda self: self.env.ref('base.in'), string='Country', readonly=True)
    state_id = fields.Many2one('res.country.state', string="State", domain="[('country_id', '=', country_id)]")
    street = fields.Char(string='Street')
    city = fields.Char(string='City')
    zip_code = fields.Char(string='ZIP Code')
    address = fields.Text(string='Address', compute='_compute_address', store=True)

    phone_number = fields.Char(string='Phone Number', tracking=True,copy=False)
    dob = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    parent_name = fields.Char(string='Parent/Guardian Name')
    relation = fields.Selection(selection=[
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Relative', 'Relative'),
        ('Guardian', 'Guardian'),
        ('Sibling', 'Sibling')
    ], string='Relation with Student')
    parent_phone_number = fields.Char(string='Phone Number of Parent/Guardian')
    email = fields.Char(string='Email')
    stream = fields.Selection(selection=STREAM_OPTIONS, string='Stream')
    birth_month = fields.Char(compute='_compute_birth_month', string="Birth Month" ,store=True)

    # Check the length of the roll number
    @api.constrains('roll_number')
    def _check_roll_number_length(self):
        for record in self:
            if record.roll_number and len(str(record.roll_number)) > 4:
                raise ValidationError("Roll number should not be more than 4 digits!")

    def change_status(self):
        for rec in self:
            if rec.stream == 'science':
                rec.fee_status = 'paid'
            else:
                rec.fee_status = 'pending'   

    def action_done(self):
       print("Cron job is done succesfully!")

    def action_send_card(self):
        template_id= self.env.ref('school_management.mail_template_student').id
        self.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)
        
    def name_get(self):
        students_list = []
        for record in self:
            name = record.name + ' ' + record.enr_number
            students_list.append((record.id, name ))
        return students_list
    
    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        if args is None:
            args = []
        domain = args + ['|', '|', ('phone_number', operator, name), ('name', operator, name), ('enr_number', operator, name)]
        return super(SchoolManagement, self).search(domain, limit=limit).name_get()


   #Validate the phone number format and uniqueness
    @api.constrains('phone_number')
    def _check_phone_number(self):
        for record in self:
            phone_number = record.phone_number or ''

            if not phone_number.isdigit() or len(phone_number) < 10:
                raise ValidationError("Phone number should contain only numeric values and have a maximum length of 10 digits!")

            duplicate_records = self.search([('phone_number', '=', record.phone_number), ('id', '!=', record.id)])
            if duplicate_records:
                raise ValidationError("Phone number is already assigned to another student")
            

    # Check the age of the student
    @api.constrains('age')
    def _check_age(self):
        for record in self:
            if record.age < 4:
                raise ValidationError("Age cannot be less than 4 years!")

    # Compute the age based on the date of birth
    @api.depends('dob')
    def _compute_age(self):
        for record in self:
            if record.dob:
                today = fields.Date.today()
                dob = fields.Date.from_string(record.dob)
                record.age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            else:
                record.age =0
                
    @api.model_create_multi
    def create(self, vals):
        for val in vals:
            if val.get('enr_number', _('New')) == _('New'):
                val['enr_number'] = self.env['ir.sequence'].next_by_code('school.management.student') or _('New')
            return super(SchoolManagement, self).create(val)

    # Check the format of the ZIP code
    @api.constrains('zip_code')
    def _check_zip_code_format(self):
        for record in self:
            zip_code = record.zip_code or ''
            if zip_code and (not zip_code.isdigit() or len(zip_code) != 6):
                raise ValidationError('Invalid zip code format!')
    @api.depends('division', 'stream', 'standard')
    def _depends_division(self):
        for record in self:
            teacher = self.env['school.management.teacher'].search([
                ('standard', '=', record.standard), ('division', '=', record.division), ('stream', '=', record.stream)
            ], limit=1)
            if teacher:
                record.class_teacher = teacher.id
            else:
                record.class_teacher = False

    # Compute the full address based on the individual address fields
    @api.depends('street', 'city', 'state_id', 'country_id', 'zip_code')
    def _compute_address(self):
        for record in self:
            address_parts = []
            if record.street:
                address_parts.append(record.street)
            if record.city:
                address_parts.append(record.city)
            if record.state_id:
                address_parts.append(record.state_id.name)
            if record.zip_code:
                address_parts.append(record.zip_code)
            record.address = ", ".join(address_parts)

    # Update the stream field based on the selected standard
    @api.onchange('standard')
    def _onchange_standard(self):
        if self.standard in ['11', '12']:
            self.stream = ''
        else:
            self.stream = False

    @api.depends('dob')
    def _compute_birth_month(self):
        for record in self:
            if record.dob:
                dob = fields.Date.from_string(record.dob)
                record.birth_month = dob.strftime('%B')
            else:
                record.birth_month = ''

    def rainbow_button(self):
        return {
            'effect':{
                'fadeout':'slow',
                'type' :'rainbow_man',
                'message':'   '
            }   
            }