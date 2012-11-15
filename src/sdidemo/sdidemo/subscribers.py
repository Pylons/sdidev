from substanced.root import Root
from substanced.event import subscribe_created
from substanced.catalog import Catalog

@subscribe_created(Root)
def root_created(event):
    catalog = Catalog()
    event.object.add_service('catalog', catalog)
    catalog.update_indexes('system', reindex=True)
    catalog.update_indexes('sdidemo', reindex=True)
        
