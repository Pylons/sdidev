from pyramid.httpexceptions import HTTPFound
from pyramid.renderers import get_renderer
from pyramid.view import view_config

from substanced.sdi import mgmt_view
from substanced.form import FormView
from substanced.interfaces import IFolder
from substanced.util import oid_of

from .resources import (
    Document,
    DocumentSchema,
    BinderSchema,
    )

#
#   Default "retail" view
#
@view_config(
    renderer='templates/splash.pt',
    )
def splash_view(request):
    manage_prefix = request.registry.settings.get('substanced.manage_prefix', 
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
            'master': get_renderer('templates/master.pt').implementation(),
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
        document.__creator__ = oid_of(self.request.user)
        document.__modified__ = document.__created__
        self.context[name] = document
        return HTTPFound(self.request.mgmt_path(self.context, '@@contents'))

@mgmt_view(
    name='add_binder',
    tab_title='Add Binder',
    permission='sdi.add-content',
    renderer='substanced.sdi:templates/form.pt',
    tab_condition=False,
    )
class AddBinderView(FormView):
    title = 'Add Binder'
    schema = BinderSchema()
    buttons = ('add',)

    def add_success(self, appstruct):
        registry = self.request.registry
        name = appstruct.pop('name')
        binder = registry.content.create('Binder', **appstruct)
        binder.__creator__ = oid_of(self.request.user)
        binder.__modified__ = binder.__created__
        self.context[name] = binder
        return HTTPFound(self.request.mgmt_path(self.context, '@@contents'))

