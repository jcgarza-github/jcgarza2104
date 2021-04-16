# *-* coding: utf-8 -*-
    
from odoo import models, fields, api

class Book(models.Model): 
    _name = 'library.book'
    _description = 'A library book'
    
    title = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author', required=True)
    description = fields.Text(string='Description')
    category = fields.Selection(string='Category',
                                 selection=[('fiction', 'Fiction'),
                                            ('nonfiction', 'Non-Fiction'),
                                            ('childrens', 'Children\'s')],
                                 copy=False)
    active = fields.Boolean(string='Active', default=True)
