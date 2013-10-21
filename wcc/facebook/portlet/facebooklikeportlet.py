from zope import schema
from zope.component import getMultiAdapter
from zope.formlib import form
from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.cache import render_cachekey

from Acquisition import aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from wcc.facebook import MessageFactory as _

class IFacebookLikePortlet(IPortletDataProvider):
    """
    Define your portlet schema here
    """
    pass

class Assignment(base.Assignment):
    implements(IFacebookLikePortlet)

    @property
    def title(self):
        return _('Facebook Like Portlet')

class Renderer(base.Renderer):
    
    render = ViewPageTemplateFile('templates/facebooklikeportlet.pt')

    @property
    def available(self):
        return True

class AddForm(base.NullAddForm):
    form_fields = form.Fields(IFacebookLikePortlet)
    label = _(u"Add Facebook Like Portlet")
    description = _(u"")

    def create(self):
        return Assignment()
