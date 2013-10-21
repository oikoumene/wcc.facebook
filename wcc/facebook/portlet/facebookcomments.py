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

class IFacebookComments(IPortletDataProvider):
    """
    Define your portlet schema here
    """
    width = schema.Int(title=u'Width', default=600)

class Assignment(base.Assignment):
    implements(IFacebookComments)

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def title(self):
        return _('Facebook Comments')

class Renderer(base.Renderer):
    
    render = ViewPageTemplateFile('templates/facebookcomments.pt')

    @property
    def available(self):
        return True

class AddForm(base.AddForm):
    form_fields = form.Fields(IFacebookComments)
    label = _(u"Add Facebook Comments")
    description = _(u"")

    def create(self, data):
        return Assignment(**data)

class EditForm(z3cformhelper.EditForm):
    form_fields = form.Fields(IFacebookComments)
    label = _(u"Edit Facebook Comments")
    description = _(u"")
