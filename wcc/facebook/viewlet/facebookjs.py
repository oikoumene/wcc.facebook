from Acquisition import aq_inner
from zope.interface import Interface
from five import grok
from zope.component import getMultiAdapter
from Products.CMFCore.interfaces import IContentish
from plone.app.layout.viewlets import interfaces as manager
from wcc.facebook.interfaces import IProductSpecific

grok.templatedir('templates')

class FacebookJS(grok.Viewlet):
    grok.context(IContentish)
    grok.viewletmanager(manager.IHtmlHeadLinks)
    grok.template('facebookjs')
    grok.layer(IProductSpecific)

    def available(self):
        return True
