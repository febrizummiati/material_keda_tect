# -*- coding: utf-8 -*-

from odoo.tests import common

class TestMaterial(common.TransactionCase):
    def test_action(self):
        self.supplier_china = self.env['res.partner'].search([('name', '=', 'China Export')], limit=1)
        material_record = self.env['material.keda'].create({
            'code': 'M010',
            'name' : 'Cotton Combat A',
            'type' : 'cotton',
            'buy_price' : 175,
            'supplier_id' : self.supplier_china.id
        })
        material_record._onchange_buy_price()
