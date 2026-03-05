from odoo import models, fields

class ProductCategory(models.Model):
    _inherit = 'product.category'

    image_128 = fields.Image(
        string='Hình ảnh danh mục',
        max_width=128,
        max_height=128,
    )