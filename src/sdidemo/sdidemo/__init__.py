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
    
    return config.make_wsgi_app()
