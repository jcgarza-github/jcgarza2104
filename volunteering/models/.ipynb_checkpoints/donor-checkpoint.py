# *-* coding: utf-8 -*-
    
from odoo import models, fields, api

class Donor(models.Model): 
    _name = 'nonprofit.donor'
    _description = 'A food donor'
    
    name = fields.Char(string='Name', required=True)
    phone = fields.Char(string='Phone')
    address = fields.Text(string='Address')
    active = fields.Boolean(string='Active', default=True)    