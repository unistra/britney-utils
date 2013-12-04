"""
"""

import britney
from britney.errors import SporeClientBuildError
from britney.errors import SporeMethodBuildError
import logging


__clients = {}


def get_client(name, description, base_url=None, middlewares=None,
               reset=False):
    """ Build a complete spore client and store it

    :param name: name of the client
    :param description: the REST API description as a file or URL
    :param base_url: the base URL of the REST API
    :param middlewares: middlewares to enable
    :type middlewares: ordered list of 2-elements tuples -> (middleware_class, {
        'predicate': ..., 'named_arg1': ..., 'named_arg2': ..., ...})
    :param reset: regenerate or not the client


    Example :

        import britney_utils
        from britney.middleware.format import Json
        from britney.middleware.auth import Basic

        is_json = lambda environ: environ['spore.format'] == 'json'

        client = britney_utils.get_client('MyRestApi',
            'http://my-rest-api.org/description.json',
            base_url='http://rest-api.org/v2/',
            middlewares=(
                (Json, {'predicate': is_json}),
                (Basic, {'username': 'toto', 'password': 'lala'})
            ))
    """
    if name in __clients and not reset:
        return __clients[name]

    middlewares = middlewares if middlewares is not None else []

    try:
        client = britney.spyre(description, base_url=base_url)
    except (SporeClientBuildError, SporeMethodBuildError) as build_errors:
        logging.getLogger('britney').error(str(build_errors))
    else:
        for middleware in middlewares:
            kwargs = {}
            if len(middleware) == 2:
                kwargs = middleware[1]
            predicate = kwargs.pop('predicate', None)
            if predicate:
                client.enable_if(predicate, middleware[0], **kwargs)
            else:
                client.enable(middleware[0], **kwargs)
        __clients[name] = client
        return client
