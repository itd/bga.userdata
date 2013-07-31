from plone.app.users.userdataschema import IUserDataSchema
from plone.app.users.userdataschema import IUserDataSchemaProvider
from zope import schema
from zope.interface import implements
from bga.userdata import _


# gender_options = SimpleVocabulary([
#     SimpleTerm(value='Male', title=_(u'Male')),
#     SimpleTerm(value='Female', title=_(u'Female')),
# ])


def validateAccept(value):
    if not value == True:
        return False
    return True



class UserDataSchemaProvider(object):
    implements(IUserDataSchemaProvider)

    def getSchema(self):
        """
        """

        #self.widget.visible = {'edit': 'hidden', 'view': 'invisible'}
        return IEnhancedUserDataSchema


class IEnhancedUserDataSchema(IUserDataSchema):
    """ Use all the fields from the default user data schema, and add various
    extra fields.
    """

    #IUserDataSchema.form_fields.omit('portrait', 'pdelete')

    location = schema.TextLine(
        title=_(u'label_location', default=u'Location'),
        description=_(u'help_location',
                      default=u"Your location - either city and "
                      "country - or in a company setting, where "
                      "your office is located."),
        required=False,
        )

    address = schema.TextLine(
        title=_(u'label_address', default=u'Street Address'),
        description=_(u'help_address',
                      default=u"Your street address."),
        required=False,
    )

    city = schema.TextLine(
        title=_(u'label_city', default=u'City'),
        description=_(u'help_city',
                      default=u"The city where you live."),
        required=False,
    )

    state = schema.TextLine(
        title=_(u'label_state', default=u'State'),
        description=_(u'help_state',
                      default=u"State."),
        required=False,
    )

    zipcode = schema.TextLine(
        title=_(u'label_zipcode', default=u'Zip code'),
        description=_(u'help_zipcode',
                      default=u"Zip or mailing code"),
        required=False,
    )

    country = schema.TextLine(
        title=_(u'label_country', default=u'Country/Nation'),
        description=_(u'help_country',
                      default=u"The country/nation where you live."),
        required=False,
    )

    phone = schema.TextLine(
        title=_(u'label_phone', default=u'Telephone number'),
        description=_(u'help_phone',
                      default=u"Leave your phone number so we can reach you."),
        required=False,
    )

    newsletter = schema.Bool(
        title=_(u'label_newsletter', default=u'Subscribe to newsletter'),
        description=_(u'help_newsletter',
                      default=u"If you tick this box, we'll subscribe you to "
                              "our newsletter."),
        default=False,
    )

    accept = schema.Bool(
        title=_(u'label_accept', default=u'Accept terms of use'),
        description=_(u'help_accept',
                      default=u"Tick this box to indicate that you have found,"
                              " read, and accepted the terms of use "
                              "for this site."),
        required=True,
        constraint=validateAccept,
    )


    #    IUserDataSchema["location"].widget.visible = {"edit": "invisible" }
    #IUserDataSchema["portrait"].widget.visible = {"edit": "invisible" }
    #IUserDataSchema["pdelete"].widget.visible = {"edit": "invisible" }

    # fullname = schema.TextLine(
    #     title=_(u'label_full_name', default=u'Full Name'),
    #     description=_(u'help_full_name_creation',
    #                   default=u"Enter full name, e.g. John Smith."),
    #     required=False)
    #
    # email = schema.ASCIILine(
    #     title=_(u'label_email', default=u'E-mail'),
    #     description=u'',
    #     required=True,
    #     constraint=checkEmailAddress)
    #
    # home_page = schema.TextLine(
    #     title=_(u'label_homepage', default=u'Home page'),
    #     description=_(u'help_homepage',
    #                   default=u"The URL for your external home page, "
    #                   "if you have one."),
    #     required=False)
    #
    # description = schema.Text(
    #     title=_(u'label_biography', default=u'Biography'),
    #     description=_(u'help_biography',
    #                   default=u"A short overview of who you are and what you "
    #                   "do. Will be displayed on your author page, linked "
    #                   "from the items you create."),
    #     required=False, visible = False)
    #
    # location = schema.TextLine(
    #     title=_(u'label_location', default=u'Location'),
    #     description=_(u'help_location',
    #                   default=u"Your location - either city and "
    #                   "country - or in a company setting, where "
    #                   "your office is located."),
    #     required=False)
    #
    # portrait = FileUpload(title=_(u'label_portrait', default=u'Portrait'),
    #     description=_(u'help_portrait',
    #                   default=u'To add or change the portrait: click the '
    #                   '"Browse" button; select a picture of yourself. '
    #                   'Recommended image size is 75 pixels wide by 100 '
    #                   'pixels tall.'),
    #     required=False)
    #
    # pdelete = schema.Bool(
    #     title=_(u'label_delete_portrait', default=u'Delete Portrait'),
    #     description=u'',
    #     required=False)
