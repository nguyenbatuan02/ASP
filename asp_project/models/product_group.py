from odoo import models, fields


class ProductGroup(models.Model):
    _name = 'product.group'
    _description = 'Nhóm phụ tùng'
    _order = 'name'

    name = fields.Char(
        string='Name',
        required=True
    )

    code = fields.Char(
        string='Code'
    )

    description = fields.Text(
        string='Description'
    )

    active = fields.Boolean(
        default=True
    )