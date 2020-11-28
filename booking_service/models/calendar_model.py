#############################################################
#
#  Module Name: booking_service
#  Created On: 2020-XX-XX 00:00
#  File Name: calendar_model.py
#  Author: Nathan Sadeli
#
#############################################################
# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, Warning as UserError

class CalendarEventInherit(models.Model):

    _inherit = ['calendar.event']

    equipment_ids = fields.One2many(string="Equipments", comodel_name='booking_service.calendarevent_serialnumber_rel', inverse_name='calendar_id', ondelete='cascade', index=True)
    serial_number_id = fields.Many2one(comodel_name='booking_service.serial_number', string="Serial Number Id", ondelete='set null', index=True)