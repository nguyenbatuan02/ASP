from odoo import models, fields

class AspBrand(models.Model):
    _name = 'asp.brand'
    _description = 'Thương hiệu sản phẩm'
    _order = 'name asc'

    name = fields.Char(string='Tên thương hiệu', required=True)
    description = fields.Text(string='Mô tả')
    image_128 = fields.Image(
        string='Logo',
        max_width=128,
        max_height=128,
    )
    product_count = fields.Integer(
        string='Số sản phẩm',
        compute='_compute_product_count',
    )

    def _compute_product_count(self):
        for brand in self:
            brand.product_count = self.env['product.template'].search_count(
                [('brand_id', '=', brand.id)]
            )
