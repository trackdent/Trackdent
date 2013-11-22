# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = ' '.join(word.capitalize() for word in request.application.split('_'))
response.subtitle = T('Dental Office Management Application')

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (CAT(I(_class="icon-time"), T('Calendar')), False, URL('default', 'calendar', args=session.current_id)),
    (CAT(I(_class="icon-user"), T('Patients')), False, URL('default',"index", args=session.current_id)),
    (CAT(I(_class="icon-book"), T('Contacts')), False, "", [
        (T('Labs'), False, URL('default', 'labs', args=session.current_id)),
        (T('Other Contacts'), False, URL('default', 'index', args=session.current_id, vars=dict(contacts=True)))
    ])
    ]

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
    response.menu+=[
        (CAT(I(_class="icon-cog"), T('Administration')), False, '', [
                (T('Database'), False, URL(app,'appadmin','index'))]
        ),
        (CAT( T('Help')), False, "", [
            ("", False, A(T('TrackDent Help'), _href=URL('default', 'help', args=session.current_id))),
            (T('About') + " " + request.application, False, URL('default', 'about', args=session.current_id))
        ])
        ]
_()
