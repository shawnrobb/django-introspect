Django Introspect
=================

Django Introspect is a simple Django app which returns the current version
of a running django app as plain text.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "introspect" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'introspect',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^introspect/', include('introspect.urls')),

3. Visit http://127.0.0.1:8000/introspect/ to see the current version of
django which is running in this web server.

Note that you must be logged in as