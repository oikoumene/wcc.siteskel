from collective.grok import gs
from wcc.siteskel import MessageFactory as _

@gs.importstep(
    name=u'wcc.siteskel', 
    title=_('wcc.siteskel import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wcc.siteskel.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
