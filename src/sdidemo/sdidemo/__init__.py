from pyramid.config import Configurator

from substanced import root_factory

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings, root_factory=root_factory)
    config.include('substanced')
    config.add_catalog_index('title', 'field', 'sdidemo')
    config.scan()
    return config.make_wsgi_app()
