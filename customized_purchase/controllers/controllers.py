# -*- coding: utf-8 -*-
from odoo import http

# class QprPurchase(http.Controller):
#     @http.route('/qpr_purchase/qpr_purchase/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qpr_purchase/qpr_purchase/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('qpr_purchase.listing', {
#             'root': '/qpr_purchase/qpr_purchase',
#             'objects': http.request.env['qpr_purchase.qpr_purchase'].search([]),
#         })

#     @http.route('/qpr_purchase/qpr_purchase/objects/<model("qpr_purchase.qpr_purchase"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qpr_purchase.object', {
#             'object': obj
#         })