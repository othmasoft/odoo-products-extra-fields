# -*- coding: utf-8 -*-

from odoo import models, fields, api

class product_extra_fields(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    product_id = fields.Integer('Product ID')
    manufacture = fields.Char('Manufacture')
    sku = fields.Char('sku')
    isbn = fields.Char('isbn')
    quantity = fields.Integer('Quantity')
    description = fields.Text()