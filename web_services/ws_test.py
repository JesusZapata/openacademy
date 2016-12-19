# -*- coding: utf-8 -*-
import functools
import xmlrpclib

HOST = 'localhost'
PORT = 8069
DB = 'odoo'
USER = 'admin'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST, PORT)

# 1. Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB, USER, PASS)
print "Logged in as %s (uid:%d)" % (USER, uid)

call = functools.partial(
    xmlrpclib.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)

sessions = call('openacademy.session', 'search_read', [], ['name', 'seats'])
for session in sessions:
    print "Session %s (%s seats)" % (session['name'], session['seats'])

course_id = call('openacademy.course', 'search', [
                 ('name', 'ilike', 'Course 0')])[0]
session_id = call('openacademy.session', 'create', {
    'name': 'My session',
    'course_id': course_id,
})
