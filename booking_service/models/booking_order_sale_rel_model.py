#############################################################
#
#  Module Name: booking_service
#  Created On: 2020-XX-XX 00:00
#  File Name: booking_order_salse_rel_model.py
#  Author: Nathan Sadeli
#
#############################################################
# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, Warning as UserError

class InheritResUsers(models.Model):

    _inherit 			= ['sale']
