from zope import schema
from zope.component import getMultiAdapter
from zope.formlib import form

from z3c.form import field

from plone.formwidget.contenttree import ObjPathSourceBinder
from z3c.relationfield.schema import RelationList, RelationChoice

from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.cache import render_cachekey

from Acquisition import aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from wcc.facebook import MessageFactory as _

class IEcumenicalYouthFacebookPortlet(IPortletDataProvider):
    """
    Define your portlet schema here
    """
    
    width = schema.Int(title=u'Width', required=True, default=600)

class Assignment(base.Assignment):
    implements(IEcumenicalYouthFacebookPortlet)

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def title(self):
        return _('Ecumenical Youth Facebook Portlet')

class Renderer(base.Renderer):
    
    render = ViewPageTemplateFile('templates/ecumenicalyouthfacebookportlet.pt')

    @property
    def available(self):
        return True

class AddForm(base.AddForm):
    form_fields = form.Fields(IEcumenicalYouthFacebookPortlet)
    label = _(u"Add Ecumenical Youth Facebook Portlet")
    description = _(u"")

    def create(self, data):
        return Assignment(**data)

class EditForm(base.EditForm):
    form_fields = form.Fields(IEcumenicalYouthFacebookPortlet)
    label = _(u"Edit Ecumenical Youth Facebook Portlet")
    description = _(u"")
