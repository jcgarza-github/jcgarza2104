# *-* coding: utf-8 -*-
    
from odoo import models, fields, api

class Book(models.Model): 
    _name = 'library.book'
    _description = 'A library book'
    