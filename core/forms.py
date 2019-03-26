'''
core.forms
---------------

form to check post requests

@copyright:(c) 2013 SynergyLabs
@license:UCSD License. See License file for details.
'''
from django import forms


class CampusForm(forms.Form):

    institution = forms.CharField()
    campus = forms.CharField()


class BuildForm(CampusForm):

    building = forms.CharField()

