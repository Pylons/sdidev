from substanced.catalog import Field, catalog_factory

@catalog_factory('sdidemo')
class Indexes(object):
    title = Field()
    
class IndexViews:
    def __init__(self, resource):
        self.resource = resource

    def title(self, default):
        return unicode(getattr(self.resource, 'title', default))

def includeme(config):
    config.add_indexview(
        IndexViews,
        catalog_name='sdidemo',
        index_name='title',
        attr='title'
        )
