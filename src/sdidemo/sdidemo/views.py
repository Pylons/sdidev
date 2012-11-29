from pyramid.httpexceptions import HTTPFound
from pyramid.renderers import get_renderer
from pyramid.view import view_config

from substanced.sdi import mgmt_view
from substanced.form import FormView
from substanced.interfaces import IFolder

from .resources import Document
from .resources import DocumentSchema

#
#   Default "retail" view
#
@view_config(
    renderer='templates/splash.pt',
)
def splash_view(request):
    manage_prefix = request.registry.settings.get(
        'substanced.manage_prefix',
        '/manage')
    return {'manage_prefix': manage_prefix}

#
#   "Retail" view for documents.
#
@view_config(
    context=Document,
    renderer='templates/document.pt',
)
def document_view(context, request):
    return {'title': context.title,
            'body': context.body,
            'master': get_renderer(
                'templates/master.pt').implementation(),
    }

#
#   SDI "add" view for documents
#
@mgmt_view(
    context=IFolder,
    name='add_document',
    tab_title='Add Document',
    permission='sdi.add-content',
    renderer='substanced.sdi:templates/form.pt',
    tab_condition=False,
)
class AddDocumentView(FormView):
    title = 'Add Document'
    schema = DocumentSchema()
    buttons = ('add',)

    def add_success(self, appstruct):
        registry = self.request.registry
        name = appstruct.pop('name')
        document = registry.content.create('Document', **appstruct)
        self.context[name] = document
        return HTTPFound(
            self.request.mgmt_path(self.context, '@@contents'))

from substanced.sdi import LEFT, RIGHT, MIDDLE

@mgmt_view(name='tab_1', tab_title='Tab 1',
           renderer='templates/tab_1.pt'
)
def tab_1(context, request):
    return {}


@mgmt_view(name='tab_2', tab_title='Tab 2',
           renderer='templates/tab_1.pt',
           tab_before='tab_1')
def tab_2(context, request):
    return {}


@mgmt_view(name='tab_3', tab_title='Tab 3',
           renderer='templates/tab_1.pt', tab_near=RIGHT)
def tab_3(context, request):
    return {}


@mgmt_view(name='tab_4', tab_title='Tab 4',
           renderer='templates/tab_1.pt', tab_near=LEFT)
def tab_4(context, request):
    return {}


@mgmt_view(name='tab_5', tab_title='Tab 5',
           renderer='templates/tab_1.pt', tab_near=LEFT)
def tab_5(context, request):
    return {}

