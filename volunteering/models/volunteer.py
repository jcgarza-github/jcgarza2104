# *-* coding: utf-8 -*-
    
from odoo import models, fields, api

class Volunteer(models.Model): 
    _name = 'nonprofit.volunteer'
    _description = 'A food runner'

    name = fields.Char(string='Name', required=True)
    phone = fields.Char(string='Phone')
    email = fields.Text(string='email')
    active = fields.Boolean(string='Active', default=True)    