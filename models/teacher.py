# -*- coding: utf-8 -*-

from odoo import models, fields

class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'School Teacher'

    name = fields.Char(string='Name')
    profile = fields.Text(string='Profile')
    subject_ids = fields.One2many('school.subject', 'teacher_id', string='Subjects')