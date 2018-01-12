# -*- coding: utf-8 -*-
from odoo import http

# class CjTutorAttachment(http.Controller):
#     @http.route('/cj_tutor_attachment/cj_tutor_attachment/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cj_tutor_attachment/cj_tutor_attachment/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cj_tutor_attachment.listing', {
#             'root': '/cj_tutor_attachment/cj_tutor_attachment',
#             'objects': http.request.env['cj_tutor_attachment.cj_tutor_attachment'].search([]),
#         })

#     @http.route('/cj_tutor_attachment/cj_tutor_attachment/objects/<model("cj_tutor_attachment.cj_tutor_attachment"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cj_tutor_attachment.object', {
#             'object': obj
#         })