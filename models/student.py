# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class Student(models.Model):
    _name = 'school.student'
    _description = 'School Student'

    name = fields.Char(string='Name')
    birth_date = fields.Date(string='Birth Date')
    age = fields.Integer(string='Age', compute='_calculate_age', readonly=True, store=True)
    final_exam_grade = fields.Float(string='Final Exam Grade')
    subject_ids = fields.Many2many('school.subject', string='Subjects')
    
    @api.depends('birth_date')
    def _calculate_age(self):
        today = datetime.today()
        for student in self:
            if student.birth_date:
                birth_date = fields.Date.from_string(student.birth_date)
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                student.age = age
