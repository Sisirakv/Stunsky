

from logging import PlaceHolder
from django import forms
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput,ClearableFileInput
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields= ['name','email', 'project_goals','phone','budeget',]
        widgets= {
            'name': TextInput(attrs={'class':'fz-21','type':'text','name':'name','required':'required','autocomplete':'off',}),
            'email': EmailInput(attrs={'class':'fz-21','type':'email','name':'email','required':'required','autocomplete':'off',}),
            'project_goals': TextInput(attrs={'class':'fz-21','type':'text','name':'project_goals','required':'required','autocomplete':'off',}),
            'phone': TextInput(attrs={'class':'fz-21','type':'text','id':'sppb-form-builder-field-2','name':'phone','required':'required','autocomplete':'off',}),
            'budeget': TextInput(attrs={'class':'fz-21','type':'text','name':'budeget','required':'required','autocomplete':'off',}),
            # 'message':Textarea(attrs={'class':'is-large','type':'text','name':'message','required':'required','autocomplete':'off',})
        }
        
        
class JobApplicationForm(forms.ModelForm):
     class Meta:
        model = ApplyNow
        fields= ['applicant_name','phone', 'email','cv']
        widgets= {
            'applicant_name': TextInput(attrs={'class':'fz-21','type':'text','name':'applicant_name','required':'required','autocomplete':'off',}),
            'phone': TextInput(attrs={'class':'fz-21','type':'text','id':'sppb-form-builder-field-2','name':'phone','required':'required','autocomplete':'off',}),
            'email': EmailInput(attrs={'class':'fz-21','type':'email','name':'email','required':'required','autocomplete':'off',}),
            'cv': FileInput(attrs={'class':'fz-21','type':'file','name':'cv','required':'required','autocomplete':'off',}),
        }