# *-* coding: utf-8 -*-
    
from odoo import models, fields, api

class Recipient(models.Model): 
    _name = 'nonprofit.recipient'
    _description = 'A food recipient'
    