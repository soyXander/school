# -*- coding: utf-8 -*-

from odoo import models, fields
from . import subject

class Student(models.Model):
    _name = 'school.student'
    _description = 'School Student'

    name = fields.Char(string='Name')
    birth_date = fields.Date(string='Birth Date')
    age = fields.Integer(string='Age')
    final_exam_grade = fields.Float(string='Final Exam Grade')
    subject_ids = fields.Many2many('school.subject', string='Subjects')