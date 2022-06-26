# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class MaterialKeda(models.Model):
    _name = 'material.keda'

    code = fields.Char('Code')
    name = fields.Char('Name')
    type = fields.Selection([('fabric', 'Fabric'), ('jeans', 'Jeans'), ('cotton', 'Cotton')], 'Type')
    buy_price = fields.Float('Buy Price', default=100)
    supplier_id = fields.Many2one('res.partner', string='Supplier')

    @api.onchange('buy_price')
    def _onchange_buy_price(self):
        if self.buy_price < 100:
            raise exceptions.Warning('Buy price less than 100 !')
        else:
            print ("Buy Price more than 100 !")