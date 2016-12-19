# -*- coding: utf-8 -*-
from openerp import fields, models, api

"""
This module create model of Wizard
"""


class Wizard(models.TransientModel):
    """"
    This class create model of Wizard
    """
    _name = 'openacademy.wizard'

    def _default_sessions(self):
        return self.env['openacademy.session'].browse(
            self._context.get('active_ids'))

    session_ids = fields.Many2many('openacademy.session',
                                   string="Sessions", required=True,
                                   default=_default_sessions)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    @api.multi
    def subscribe(self):
        for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids
        return {}
