#############################################################
#
#  Module Name: booking_service
#  Created On: 2020-XX-XX 00:00
#  File Name: hr_employee_model.py
#  Author: Nathan Sadeli
#
#############################################################
# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, Warning as UserError

class HrEmployeeInherit(models.Model):

    _inherit = ['hr.employee']

    def action_view_calendar_by_employee(self):
        print("Employee selected: " + str(self.id))

        partner_id = self.env['res.partner'].search([('id', '=', self.user_id.partner_id.id)])

        print("Partner ID Selected Employee: " + str(partner_id.id))

        action = self.env.ref('booking_service.action_view_calendar')
        result = action.read()[0]
        result['domain'] = [('partner_ids', 'in', partner_id.id)]
        return result