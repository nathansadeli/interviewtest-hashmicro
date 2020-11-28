#############################################################
#
#  Module Name: booking_service
#  Created On: 2020-XX-XX 00:00
#  File Name: calendarevent_serialnumber_rel_model.py
#  Author: Nathan Sadeli
#
#############################################################
# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, Warning as UserError

class PdctSerNumbRel(models.Model):

    _name = 'booking_service.calendarevent_serialnumber_rel'
    _description = 'Relation Model between Calendar Event and Serial Number'

    calendar_id = fields.Many2one(comodel_name='calendar.event', string="Calendar Id", ondelete='set null', index=True)
    product_id = fields.Many2one(comodel_name='product.product', string="Product Id", ondelete='set null', index=True)
    serial_number_id = fields.Many2one(comodel_name='booking_service.serial_number', string="Serial Number Id", ondelete='set null', index=True)
    team_id = fields.Many2one(comodel_name='booking_service.team', string="Team Id", ondelete='set null', index=True)
    sale_order_id = fields.Many2one(comodel_name='sale.order', string="Sale Order ID", ondelete='set null', index=True)
