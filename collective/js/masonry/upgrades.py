from Products.CMFCore.utils import getToolByName
PROFILE = 'profile-collective.js.masonry:default'


def common(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile(PROFILE)

def recook(context):
    jsregistry = getToolByName(context, 'portal_javascripts')
    jsregistry.cookResources()
