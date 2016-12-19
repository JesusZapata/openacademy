# -*- coding: utf-8 -*-

from openerp.tests.common import TransactionCase
from openerp.exceptions import ValidationError


class GlobalTestOpenAcademySession(TransactionCase):
    '''
    Test Model Session
    '''

    def setUp(self):
        super(GlobalTestOpenAcademySession, self).setUp()
        self.session = self.env['openacademy.session']
        self.partner_vauxoo = self.env.ref('base.res_partner_23')
        self.course = self.env.ref('openacademy.course1')
        self.partner_attende = self.env.ref('base.res_partner_5')

    def test_10_instructor_is_attende(self):
        '''
        Check _check_instructor_not_in_attendees constrains
        '''
        with self.assertRaisesRegexp(
                ValidationError,
                "A session's instructor can't be an attendee"
        ):
            self.session.create({
                'name': 'Session test 1',
                'seats': 1,
                'instructor_id': self.partner_vauxoo.id,
                'attendee_ids': [(6, 0, [self.partner_vauxoo.id])],
                'course_id': self.course.id,
            })

    def test_20_wkf_done(self):
        '''
        Check the workflow
        '''
        session_test = self.session.create({
            'name': 'Session test 1',
            'seats': 2,
            'instructor_id': self.partner_vauxoo.id,
            'attendee_ids': [(6, 0, [self.partner_attende.id])],
            'course_id': self.course.id,
        })

        # Check draft state
        self.assertEqual(session_test.state, 'draft',
                         'Initial state should be in "draft"')

        # Change confirmed state
        session_test.signal_workflow('confirm')
        self.assertEqual(session_test.state, 'confirmed',
                         "Signal confirm don't work fine!")

        # Change done state
        session_test.signal_workflow('done')
        self.assertEqual(session_test.state, 'done',
                         "Signal done don't work fine!")
