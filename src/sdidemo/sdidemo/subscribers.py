from substanced.root import Root
from substanced.event import subscribe_created
from substanced.util import find_service

@subscribe_created(Root)
def root_created(event):
    catalogs = find_service(event.object, 'catalogs')
    catalogs.add_catalog('sdidemo', update_indexes=True)

