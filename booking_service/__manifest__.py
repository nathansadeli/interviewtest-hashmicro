# -*- coding: utf-8 -*-
{
    'name': 'Equipment Booking Order',
    'version': '0.1',
    'summary': 'To allow users to create bookings for employees and equipments.',
    'author': 'Nathan Sadeli',
    'lisence': 'LGPL-3',
    'description': """
Manage Booking orders of Equipments
==================================

This application allows you to manage your booking.
""",
    'website': '',
    'depends': ['sale', 'calendar', 'hr'],
    'data': [
        'views/menu_action.xml',
        'views/menu_item.xml',
        'views/product_view.xml',
        'views/hr_employee_view.xml',
        'views/calendar_event_view.xml',
        'views/serial_number_view.xml',
        'views/team_view.xml',
        'views/sale_view.xml',
        'security/ir.model.access.csv',
    ],
    'category': 'Uncategorized',
    'installable': True,
    'auto_install': False,
    'application': True,
}