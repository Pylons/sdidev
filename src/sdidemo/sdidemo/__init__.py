from pyramid.config import Configurator
from pyramid.security import NO_PERMISSION_REQUIRED
from pyramid.httpexceptions import HTTPForbidden

from substanced import root_factory
from substanced.sdi.views.login import login

from substanced.workflow import Workflow

workflow = Workflow(initial_state="draft", type="document")

workflow.add_state("draft")
workflow.add_state("published")
workflow.add_state("rejected")

workflow.add_transition('publish', from_state='draft', to_state='published')
workflow.add_transition('unpublish', from_state='published', to_state='draft')
workflow.add_transition(
    'reject_published', from_state='published', to_state='rejected')
workflow.add_transition(
    'reject_draft', from_state='draft', to_state='rejected')
workflow.add_transition('unreject', from_state='rejected', to_state='draft')

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings, root_factory=root_factory)
    config.include('substanced')
    config.include('.catalog')
    config.include('.evolution')
    config.add_workflow(workflow, ('Document',))

    config.scan()
    # paster serve entry point
    settings['debug_templates'] = 'true'
    config.add_route('deformdemo', '/deformdemo*traverse')
    config.add_static_view('static_demo', 'deformdemo:static')
    config.add_translation_dirs(
        'colander:locale',
        'deform:locale',
        'deformdemo:locale'
        )
    def onerror(*arg):
        pass
    config.scan('deformdemo', onerror=onerror)
    # override login page to show login info
    config.add_mgmt_view(
        login,
        name='login',
        renderer='sdidemo:templates/login.pt',
        tab_condition=False,
        permission=NO_PERMISSION_REQUIRED)
    config.add_mgmt_view(
        login,
        context=HTTPForbidden,
        renderer='sdidemo:templates/login.pt',
        tab_condition=False,
        permission=NO_PERMISSION_REQUIRED
        )
    return config.make_wsgi_app()
