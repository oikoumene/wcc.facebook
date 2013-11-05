from zope import schema
from zope.component import getMultiAdapter
from zope.formlib import form

# XXX: Uncomment for z3cform

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

class IWccFacebookPortlet(IPortletDataProvider):
    """
    Define your portlet schema here
    """
    width = schema.Int(title=u'Width', required=True, default=600)

class Assignment(base.Assignment):
    implements(IWccFacebookPortlet)

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def title(self):
        return _('WccFacebookPortlet')

class Renderer(base.Renderer):
    
    render = ViewPageTemplateFile('templates/wccfacebookportlet.pt')

    @property
    def available(self):
        return True

# XXX: z3cform
# class AddForm(z3cformhelper.AddForm):
class AddForm(base.AddForm):

#    XXX: z3cform
#    fields = field.Fields(IWccFacebookPortlet)

    form_fields = form.Fields(IWccFacebookPortlet)

    label = _(u"Add WccFacebookPortlet")
    description = _(u"")

    def create(self, data):
        return Assignment(**data)

# XXX: z3cform
# class EditForm(z3cformhelper.EditForm):
class EditForm(base.EditForm):

#    XXX: z3cform
#    fields = field.Fields(IWccFacebookPortlet)

    form_fields = form.Fields(IWccFacebookPortlet)

    label = _(u"Edit WccFacebookPortlet")
    description = _(u"")
