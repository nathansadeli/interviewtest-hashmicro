#############################################################
#
#  Module Name: booking_service
#  Created On: 2020-XX-XX 00:00
#  File Name: sale_model.py
#  Author: Nathan Sadeli
#
#############################################################
# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, Warning as UserError
from datetime import timedelta, datetime, date, time

class SaleInherit(models.Model):

    _inherit = ['sale.order']

    is_a_booking = fields.Boolean(string="Is A Booking")
    the_team_id = fields.Many2one(string="Team", comodel_name='booking_service.team', ondelete='set null', index=True)
    team_leader_id = fields.Many2one(string="Team Leader", related="the_team_id.team_leader_id", index=True)
    employee_ids = fields.One2many(string="Employees", related="the_team_id.employee_ids", index=True)
    equipment_ids = fields.One2many(string="Equipments", related="the_team_id.equipment_ids", index=True)
    booking_start = fields.Datetime(string='Booking Start', default=lambda self: fields.datetime.now()) # , default=lambda self: fields.datetime.now()
    booking_end = fields.Datetime(string='Booking End')

    @api.onchange("booking_start")
    def onchange_bookingend_leadtime(self):
        res = {}
        DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
        lead_time = 1

        if not self.booking_start:
            res = {'warning': {
                'title': _('Warning'),
                'message': _('Field ' + '" ' + 'Booking Start ' + '"' + 'must not empty!')
                }
            }

            return res
        else:
            get_booking_start = datetime.strptime(str(self.booking_start), DATETIME_FORMAT)
            temp_date = get_booking_start.strftime(DATETIME_FORMAT)
            str_booking_start = temp_date

            newtime_booking_end = get_booking_start + timedelta(hours=+ lead_time)
            self.booking_end = datetime.strptime(str(newtime_booking_end), DATETIME_FORMAT)

    def action_validate_booking_order(self):
        return True

    def action_check_booking_order(self):
        res = {}
        DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

        if not self.team_leader_id:
            return True
        # else:
        #     if self.booking_start:
        #         exect_date = self.env['booking_service.calendarevent_serialnumber_rel'].seach([('team_id', '=', self.the_team_id.id)])
        # return True