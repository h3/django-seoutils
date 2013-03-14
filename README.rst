django-seoutils
===============

A simple django app to manage SEO related data with the admin.


Installation
------------

1. In your `settings.py`, add `seoutils` to your `INSTALLED_APPS`.
2. Sync your database

From there you will have a new app called `Seoutils` in the admin. Start by adding a `Meta` 
for the root page of your site. The URL will of course be `/` and the other fields are what
you think they are (page title, keywords, description, JavaScript).

The root URL will be used as default. For example, if you have a page with the URL `/contact/`,
seoutils will first check if a Meta exists for this URL and if it doesn't find one it will use
the Meta for the root page.

The JavaScript field is optional. It is meant to be used in special cases where you need to
add SEO specific scripts like campaign tracking code and such. You will need to declare it
in your template like this:

.. code-block:: django

    {{ meta.extra_js|safe }}


Using the context processor
---------------------------

This is the recommanded way to use `seoutils`.

In your `settings.py` add `seoutils.context_processors.meta` to your `TEMPLATE_CONTEXT_PROCESSORS`.

Then in your template you will have a `meta` variable which is a `Meta` instance. So you can use it
like this:

.. code-block:: django

    <title>{{ meta.title }}</title>
    <meta name="description" content="{{ meta.desc }}">
    <meta name="keywords" content="{{ meta.keywords }}">

Using template tags
-------------------

For a more flexible approach, you can also use a template tag to retrieve a `Meta` object for a 
specific page like this:

.. code-block:: django
    
    {% load seoutils_tags %}
    {% seometa request as meta %}
    <title>{{ meta.title }}</title>
    <meta name="description" content="{{ meta.desc }}">
    <meta name="keywords" content="{{ meta.keywords }}">

Credits
=======

This project was created and is sponsored by:

.. figure:: http://motion-m.ca/media/img/logo.png
    :figwidth: image

Motion Média (http://motion-m.ca)
