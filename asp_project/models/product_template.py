import re
from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    brand_id = fields.Many2one(
        'asp.brand',
        string='Thương hiệu',
        ondelete='set null',
    )

    group_id = fields.Many2one(
        'product.group',
        string='Nhóm phụ tùng',
        ondelete='set null',
    )

    global_code = fields.Char(
        string='Mã quốc tế',
        index=True
    )

    global_code_normalized = fields.Char(
        string='Mã chuẩn hóa',
        compute='_compute_global_code_normalized',
        store=True,
        index=True,
    )

    alternative_product_ids = fields.Many2many(
        'product.product',
        string='Sản phẩm thay thế'
    )

    @api.depends('global_code')
    def _compute_global_code_normalized(self):
        for rec in self:
            if rec.global_code:
                # Bỏ dấu -, space, chuyển lowercase
                rec.global_code_normalized = re.sub(r'[\s\-]', '', rec.global_code).lower()
            else:
                rec.global_code_normalized = False