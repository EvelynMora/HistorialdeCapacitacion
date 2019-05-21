# -*- coding: utf-8 -*-
from odoo import http

# class Capacitaciones(http.Controller):
#     @http.route('/capacitaciones/capacitaciones/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/capacitaciones/capacitaciones/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('capacitaciones.listing', {
#             'root': '/capacitaciones/capacitaciones',
#             'objects': http.request.env['capacitaciones.capacitaciones'].search([]),
#         })

#     @http.route('/capacitaciones/capacitaciones/objects/<model("capacitaciones.capacitaciones"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('capacitaciones.object', {
#             'object': obj
#         })