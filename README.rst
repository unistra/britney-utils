=============
britney-utils
=============

Britney-utils comes with some utilities to create and manage clients build by Britney.

.. image:: https://secure.travis-ci.org/unistra/britney-utils.png?branch=master
    :target: https://travis-ci.org/unistra/britney-utils

    
.. image:: https://coveralls.io/repos/unistra/britney-utils/badge.png
    :target: https://coveralls.io/r/unistra/britney-utils

.. image:: https://landscape.io/github/unistra/britney-utils/master/landscape.svg?style=flat
   :target: https://landscape.io/github/unistra/britney-utils/master
   :alt: Code Health

Install
=======

britney-utils is working on Python 2.7 and Python >= 3.2. To install the module, use pip ::

    $> pip install britney-utils


Use it...
=========


... to create a basic client
----------------------------

You can easily create a client with the **get_client** function. It will create and save the client to retrieve it later with his name, acting as a cache ::

    import britney_utils

    client = britney_utils.get_client('my_client',
                                      '/path/to/spore/description.json',
                                      base_url='http://my-rest-api.org/v1/')


... to reset an instance
------------------------

If an instance is already created with a name you gave in first place, you can easily reset and rebuild it. In this example, we except that the **my_client** SPORE client already exist ::

    client = britney_utils.get_client('my_client',
                                      '/path/to/spore/description.json',
                                      reset=True)


A new instance is created with the **my_client** name and saved


... to create a pre-build instance with middlewares
---------------------------------------------------

Creating a rich client with all middlewares needed activated is useful. You can do this like this ::

    from britney.middleware import auth, format
    import britney_utils

    middlewares = (
        (format.Json, {'predicate': lambda env: env['format'] == 'json'}),
        (auth.Basic, {'username': 'toto', 'password': 'xxxxxx'})
    )

    client = britney_utils.get_client('my_client',
                                      '/path/to/spore/description.json',
                                      middlewares=middlewares)
