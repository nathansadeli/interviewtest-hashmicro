#############################################################
#
#  Module Name: booking_service
#  Created On: 2020-XX-XX 00:00
#  File Name: product_model.py
#  Author: Nathan Sadeli
#
#############################################################
# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, Warning as UserError

class ProductTemplateInherit(models.Model):

    _inherit = ['product.template']

    is_an_equipment = fields.Boolean(string="Is An Equipment", related="product_variant_ids.is_an_equipment")
    serial_no_ids = fields.One2many(string="Serial Numbers", related="product_variant_ids.serial_no_ids")
    calendar_event_id = fields.Many2one(string="Calendar", related="product_variant_ids.calendar_event_id")

class ProductProductInherit(models.Model):

    _inherit = ['product.product']

    is_an_equipment = fields.Boolean(string="Is An Equipment")
    serial_no_ids = fields.One2many(string="Serial Numbers", comodel_name='booking_service.serial_number', inverse_name='product_id', ondelete='cascade', index=True)
    calendar_event_id = fields.Many2one(string="Calendar", comodel_name='calendar.event', ondelete='set null', index=True)