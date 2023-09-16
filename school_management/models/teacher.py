from odoo import models, fields, api
from datetime import datetime

class SchoolManagementTeacher(models.Model):
    _name = 'school.management.teacher'
    _description = 'Teacher'
   

    name = fields.Char(string='Teacher Name')
    student_id = fields.One2many('school.management.student', 'class_teacher', string="students")
    standard = fields.Selection(string='Standard assigned to teacher',
                                selection=[('jr_kg', 'Jr. KG'),
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
                                           ('12', '12th')])
    DIVISION_OPTIONS = [
        ('a', 'A'),
        ('b', 'B')
    ]

    STREAM_OPTIONS = [
        ('science', 'Science'),
        ('commerce', 'Commerce'),
        ('arts', 'Arts')
    ]
    division = fields.Selection(selection=DIVISION_OPTIONS, string='Division')
    stream = fields.Selection(selection=STREAM_OPTIONS, string='Stream')
   
