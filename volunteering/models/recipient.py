# *-* coding: utf-8 -*-
    
from odoo import models, fields, api

class Recipient(models.Model): 
    _name = 'nonprofit.recipient'
    _description = 'A food recipient'

    name = fields.Char(string='Name', required=True)
    phone = fields.Char(string='Phone')
    address = fields.Text(string='Address')
    active = fields.Boolean(string='Active', default=True)
