# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class test_module_1(models.Model):
#     _name = 'test_module_1.test_module_1'
#     _description = 'test_module_1.test_module_1'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     custom_field_1 = fields.Integer()
#     value3 = fields.integer()
#     description = fields.Text()
#     pos_x = fields.Integer()
#     pos_y = fields.Integer()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
