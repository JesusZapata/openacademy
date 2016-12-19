# -*- coding: utf-8 -*-

from psycopg2 import IntegrityError

from openerp.tests.common import TransactionCase
from openerp.tools import mute_logger


class GlobalOpenAcademyCourse(TransactionCase):
    """
    Test Model Course
    """

    def setUp(self):
        super(GlobalOpenAcademyCourse, self).setUp()
        self.course = self.env['openacademy.course']

    def create_course(self, course_name, course_description,
                      course_responsible_id):
        course_id = self.course.create({
            'name': course_name,
            'description': course_description,
            'responsible_id': course_responsible_id,
        })
        return course_id

    @mute_logger('openerp.sql_db')
    def test_10_same_name_description(self):
        """
        Test constraints name_description_check
        """
        with self.assertRaisesRegexp(
                IntegrityError,
                'new row for relation "openacademy_course" violates'
                ' check constraint "openacademy_course_name_description_check"'
        ):
            self.create_course('test', 'test', None)

    @mute_logger('openerp.sql_db')
    def test_20_two_courses_same_name(self):
        """
        Test constraints name_unique
        """
        self.create_course('test1', 'test_description', None)

        with self.assertRaisesRegexp(
            IntegrityError,
            'duplicate key value violates unique'
            ' constraint "openacademy_course_name_unique"'
        ):
            self.create_course('test1', 'test_description', None)

    def test_15_duplicate_course(self):
        """
        Test copy method
        """
        course = self.env.ref('openacademy.course0')
        course.copy()
