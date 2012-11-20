from pyramid.config import Configurator

from substanced import root_factory

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings, root_factory=root_factory)
    config.include('substanced')
    config.add_catalog_index('title', 'field', 'sdidemo')
    config.scan()

    slickgrid_static_path = settings.get('slickgrid.static_path', None)
    if slickgrid_static_path is None:
        raise RuntimeError, 'You must specify the slickgrid.static_path variable' \
                            ' to point to your slickgrid sources. Or: use the ini' \
                            ' provided by the buildout, which automates this.'

    config.add_static_view('/sg-static', slickgrid_static_path,
        cache_max_age=60 * 60 * 24 * 365)

    return config.make_wsgi_app()
