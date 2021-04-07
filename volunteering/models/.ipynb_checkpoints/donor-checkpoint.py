# *-* coding: utf-8 -*-
    
from odoo import models, fields, api

class Donor(models.Model): 
    _name = 'nonprofit.donor'
    _description = 'A food donor'
    