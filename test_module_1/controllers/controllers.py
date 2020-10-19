# -*- coding: utf-8 -*-
# from odoo import http


# class TestModule1(http.Controller):
#     @http.route('/test_module_1/test_module_1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_module_1/test_module_1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_module_1.listing', {
#             'root': '/test_module_1/test_module_1',
#             'objects': http.request.env['test_module_1.test_module_1'].search([]),
#         })

#     @http.route('/test_module_1/test_module_1/objects/<model("test_module_1.test_module_1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_module_1.object', {
#             'object': obj
#         })
