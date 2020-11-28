#############################################################
#
#  Module Name: booking_service
#  Created On: 2020-XX-XX 00:00
#  File Name: serial_number_product_product_rel_model.py
#  Author: Nathan Sadeli
#
#############################################################
# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, Warning as UserError

class SerialNumber(models.Model):

    _name = 'booking_service.serial_number'
    _description = 'This model are manifest all product serial number'
    _rec_name = 'serial_no'

    serial_no = fields.Char(string="Serial Numbers")
    product_id = fields.Many2one(string="Product", comodel_name='product.product', ondelete='set null', index=True)

    def action_view_calendar_by_sn(self):
        print("Serial Number selected: " + str(self.serial_no))

        action = self.env.ref('booking_service.action_view_calendar_sn')
        result = action.read()[0]
        # result['context'] = {'default_serial_number':self.id}
        result['domain'] = [('equipment_ids.serial_number_id', 'in', self.serial_no)]
        return result