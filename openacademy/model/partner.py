# -*- coding: utf-8 -*-

"""
This module create model of Partner
"""

from openerp import fields, models


class Partner(models.Model):
    """"
    This class create model of Partner
    """
    _inherit = 'res.partner'
    instructor = fields.Boolean("Instructor", default=False)

    session_ids = fields.Many2many('openacademy.session',
                                   string="Attended Sessions", readonly=True)
