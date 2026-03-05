from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    brand_id = fields.Many2one(
        'asp.brand',
        string='Thương hiệu',
        ondelete='set null',
    )