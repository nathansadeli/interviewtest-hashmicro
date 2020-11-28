#############################################################
#
#  Module Name: booking_service
#  Created On: 2020-XX-XX 00:00
#  File Name: hremployee_team_rel_model.py
#  Author: Nathan Sadeli
#
#############################################################
# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, Warning as UserError

class HREmployeeTeamRel(models.Model):

    _name = 'booking_service.hremployee_team_rel'
    _description = 'Relation Model between HR Employee and Team'

    employee_id = fields.Many2one(string="Employee ID", comodel_name='hr.employee', ondelete='set null', index=True)
    team_id = fields.Many2one(string="Team", comodel_name='booking_service.team', ondelete='set null', index=True)
    sale_order_id = fields.Many2one(string="Sale Order ID", comodel_name='sale.order', ondelete='set null', index=True)
