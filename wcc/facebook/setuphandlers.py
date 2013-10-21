from collective.grok import gs
from wcc.facebook import MessageFactory as _

@gs.importstep(
    name=u'wcc.facebook', 
    title=_('wcc.facebook import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wcc.facebook.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
