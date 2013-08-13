from collective.grok import gs
from plonegovmy.theme import MessageFactory as _

@gs.importstep(
    name=u'plonegovmy.theme', 
    title=_('plonegovmy.theme import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('plonegovmy.theme.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
