# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class MaterialKeda(http.Controller):
    @http.route('/page/material',type="http", auth='public', website=True)
    def index(self):
        supplier_rec = request.env['res.partner'].sudo().search([])

        return http.request.render('material_keda.material_data', {'supplier_rec' : supplier_rec})

    @http.route('/page/creatematerial', type="http", auth='public', website=True)
    def create_webmaterial(self,**kw):
        request.env['material.keda'].sudo().create(kw)
        return request.render('material_keda.material_thanks', {})