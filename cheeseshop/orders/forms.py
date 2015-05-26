# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.forms.formsets import BaseFormSet, formset_factory

NUMBER_CHOICES = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
)

class ContactForm(forms.Form):
#     date = forms.DateField(required=False)
#     subject = forms.CharField(
# 	max_length=100,
# 	help_text='my_help_text',
# 	required=True,
# 	widget=forms.TextInput(attrs={'placeholder': 'placeholdertest'}),
# 	)
# 	password = forms.CharField(widget=forms.PasswordInput)
# 	message = forms.CharField(required=False, help_text='<i>my_help_text</i>')
# 	sender = forms.EmailField(label='Sender © unicode')
# 	secret = forms.CharField(initial=42, widget=forms.HiddenInput)
# 	cc_myself = forms.BooleanField(
# 								 required=False, help_text='You will get a copy in your mailbox.')
# 	select1 = forms.ChoiceField(choices=RADIO_CHOICES)
# 	select2 = forms.MultipleChoiceField(
# 									  choices=RADIO_CHOICES,
# 									  help_text='Check as many as you like.',
# 									  )
 	select = forms.ChoiceField(choices=NUMBER_CHOICES)
# 	select4 = forms.MultipleChoiceField(
# 									  choices=MEDIA_CHOICES,
# 									  help_text='Check as many as you like.',
# 									  )
# 	category1 = forms.ChoiceField(
# 								choices=RADIO_CHOICES, widget=forms.RadioSelect)
# 	category2 = forms.MultipleChoiceField(
# 										choices=RADIO_CHOICES,
# 										widget=forms.CheckboxSelectMultiple,
# 										help_text='Check as many as you like.',
# 										)
# 	category3 = forms.ChoiceField(
# 								widget=forms.RadioSelect, choices=MEDIA_CHOICES)
# 	category4 = forms.MultipleChoiceField(
# 										choices=MEDIA_CHOICES,
# 										widget=forms.CheckboxSelectMultiple,
# 										help_text='Check as many as you like.',
# 										)
# 	addon = forms.CharField(
# 						  widget=forms.TextInput(attrs={'addon_before': 'before', 'addon_after': 'after'}),
# 						  )
# 
# 	required_css_class = 'bootstrap3-req'
# 
# 	def clean(self):
# 	  cleaned_data = super(TestForm, self).clean()
# 		  raise forms.ValidationError(
# 									  "This error was added to show the non field errors styling.")
# 			  return cleaned_data



class ContactBaseFormSet(BaseFormSet):
    def add_fields(self, form, index):
        super(ContactBaseFormSet, self).add_fields(form, index)

    def clean(self):
        super(ContactBaseFormSet, self).clean()
        raise forms.ValidationError("This error was added to show the non form errors styling")

ContactFormSet = formset_factory(forms.Form, formset=ContactBaseFormSet,
                                 extra=2,
                                 max_num=4,
                                 validate_max=True)


class FilesForm(forms.Form):
    text1 = forms.CharField()
    file1 = forms.FileField()
    file2 = forms.FileField(required=False)
    file3 = forms.FileField(widget=forms.ClearableFileInput)
    file4 = forms.FileField(required=False, widget=forms.ClearableFileInput)


class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()

    def clean(self):
        cleaned_data = super(ArticleForm, self).clean()
        raise forms.ValidationError("This error was added to show the non field errors styling.")
        return cleaned_data
