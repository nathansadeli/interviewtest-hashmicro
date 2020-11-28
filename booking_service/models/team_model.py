#############################################################
#
#  Module Name: booking_service
#  Created On: 2020-XX-XX 00:00
#  File Name: team_model.py
#  Author: Nathan Sadeli
#
#############################################################
# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, Warning as UserError

class Team(models.Model):

    _name = 'booking_service.team'
    _description = 'Creating a team of attendee from booking equipments'
    _rec_name = 'name'

    name = fields.Char(string="Team Name")
    team_leader_id = fields.Many2one(string="Team Leader", comodel_name='hr.employee', ondelete='set null', index=True)
    employee_ids = fields.One2many(string="Employees", comodel_name='booking_service.hremployee_team_rel', inverse_name='team_id', ondelete='cascade', index=True)
    equipment_ids = fields.One2many(string="Equipments", comodel_name='booking_service.calendarevent_serialnumber_rel', inverse_name='calendar_id', ondelete='cascade', index=True)
