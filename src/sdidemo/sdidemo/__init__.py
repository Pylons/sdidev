from pyramid.config import Configurator

from substanced import root_factory

from substanced.workflow import Workflow

workflow = Workflow(initial_state="draft", type="document")

workflow.add_state("draft")
workflow.add_state("published")
workflow.add_transition('to_publish', from_state='draft', to_state='published')
workflow.add_transition('to_draft', from_state='published', to_state='draft')

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings, root_factory=root_factory)
    config.include('substanced')
    config.add_catalog_index('title', 'field', 'sdidemo')
    config.add_workflow(workflow, ('Document',))

    config.scan()
    # Let's override the built-in add view
#    from substanced.folder import Folder
#    from .views import MyAddFolderView
#    config.add_content_type('Folder', Folder,
#                            add_view='my_add_folder',
#                            icon='icon-folder-close')

    # Do some evolution
    config.add_evolution_package('sdidemo.evolution')
    return config.make_wsgi_app()
