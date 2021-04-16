# *-* coding: utf-8 -*-
    
from odoo import models, fields, api

class Member(models.Model): 
    _name = 'library.member'
    _description = 'A library member'

    name = fields.Char(string='Name', required=True)
    memberID = fields.Integer(string='Member ID')
    active = fields.Boolean(string='Active', default=True)