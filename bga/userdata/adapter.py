from plone.app.users.browser.personalpreferences import UserDataPanelAdapter


class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
    """
    """

    def get_address(self):
        return self.context.getProperty('address', '')

    def set_address(self, value):
        return self.context.setMemberProperties({'address': value})

    address = property(get_address, set_address)

    def get_city(self):
        return self.context.getProperty('city', '')

    def set_city(self, value):
        return self.context.setMemberProperties({'city': value})

    city = property(get_city, set_city)

    def get_state(self):
        return self.context.getProperty('state', '')

    def set_state(self, value):
        return self.context.setMemberProperties({'state': value})

    state = property(get_state, set_state)

    def get_zipcode(self):
        return self.context.getProperty('zipcode', '')

    def set_zipcode(self, value):
        return self.context.setMemberProperties({'zipcode': value})

    zipcode = property(get_zipcode, set_zipcode)

    def get_country(self):
        return self.context.getProperty('country', '')

    def set_country(self, value):
        return self.context.setMemberProperties({'country': value})

    country = property(get_country, set_country)

    def get_phone(self):
        return self.context.getProperty('phone', '')

    def set_phone(self, value):
        return self.context.setMemberProperties({'phone': value})

    phone = property(get_phone, set_phone)

    def get_newsletter(self):
        return self.context.getProperty('newsletter', '')

    def set_newsletter(self, value):
        return self.context.setMemberProperties({'newsletter': value})

    newsletter = property(get_newsletter, set_newsletter)

    def get_accept(self):
        return self.context.getProperty('accept', '')

    def set_accept(self, value):
        return self.context.setMemberProperties({'accept': value})

    accept = property(get_accept, set_accept)

