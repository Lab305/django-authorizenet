from django import forms
from django.conf import settings
from authorizenet.fields import CreditCardField, CreditCardExpiryField, \
        CreditCardCVV2Field, CountryField

class BillingAddressForm(forms.Form):
    first_name = forms.CharField(50, label="First Name")
    last_name = forms.CharField(50, label="Last Name")
    company = forms.CharField(50, label="Company", required=False)
    address = forms.CharField(60, label="Street Address")
    city = forms.CharField(40, label="City")
    state = forms.CharField(40, label="State")
    country = CountryField(label="Country", initial="US")
    zip = forms.CharField(20, label="Postal / Zip Code")

class ShippingAddressForm(forms.Form):
    ship_to_first_name = forms.CharField(50, label="First Name")
    ship_to_last_name = forms.CharField(50, label="Last Name")
    ship_to_company = forms.CharField(50, label="Company", required=False)
    ship_to_address = forms.CharField(60, label="Street Address")
    ship_to_city = forms.CharField(40, label="City")
    ship_to_state = forms.CharField(label="State")
    ship_to_zip = forms.CharField(20, label="Postal / Zip Code")
    ship_to_country = CountryField(label="Country", initial="US")

class AIMPaymentForm(forms.Form):
    card_num = CreditCardField(label="Credit Card Number")
    exp_date = CreditCardExpiryField(label="Expiration Date")
    card_code = CreditCardCVV2Field(label="Card Security Code")


class CIMPaymentForm(forms.Form):
    card_number = CreditCardField(label="Credit Card Number")
    expiration_date = CreditCardExpiryField(label="Expiration Date")
    card_code = CreditCardCVV2Field(label="Card Security Code")


class HostedCIMProfileForm(forms.Form):
    token = forms.CharField(widget=forms.HiddenInput)
    def __init__(self, token, *args, **kwargs):
        super(HostedCIMProfileForm, self).__init__(*args, **kwargs)
        self.fields['token'].initial = token
        if settings.AUTHNET_DEBUG:
            self.action = "https://test.authorize.net/profile/manage"
        else:
            self.action = "https://secure.authorize.net/profile/manage"
        


def get_test_exp_date():
    from datetime import date, timedelta
    test_date = date.today() + timedelta(days=365)
    return test_date.strftime('%m%y')
