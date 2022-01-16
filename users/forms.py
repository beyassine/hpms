from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,UserChangeForm
from .models import *

class CollabForm(UserCreationForm):

	error_css_class = 'text-xs font-weight-bold text-danger text-uppercase '

	class Meta:
		model=User
		fields=('first_name','last_name','password1','password2','is_collab','is_responsable','is_client','email')		
	

	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)

		self.fields['password1'].help_text=''
		self.fields['password2'].help_text=''
		self.fields['first_name'].label= 'Nom'
		self.fields['first_name'].widget.attrs['class'] = 'form-control'
		self.fields['email'].label= 'Adresse Email'
		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['last_name'].label= 'Prénom'
		self.fields['last_name'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].label= 'Mot de Passe'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].label= 'Confirmation Mot de Passe'
		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['is_collab'].label= 'Intervenant'		
		self.fields['is_collab'].widget.attrs['class'] = 'form-check-input'
		self.fields['is_collab'].widget.attrs['name'] = 'radio-statut'
		self.fields['is_responsable'].label= 'Responsable'
		self.fields['is_responsable'].widget.attrs['class'] = 'form-check-input'
		self.fields['is_client'].label= 'Client'
		self.fields['is_client'].widget.attrs['class'] = 'form-check-input'
		self.fields['is_client'].widget.attrs['name'] = 'radio-statut'

		self.fields['email'].error_messages['unique']='Un compte est déjà créé avec cette adresse email'

class UpdatecollabForm(UserChangeForm):

	error_css_class = 'text-xs font-weight-bold text-danger text-uppercase '

	class Meta:
		model=User
		fields=('first_name','last_name','is_collab','is_responsable','is_client','email')		
	

	def __init__(self, *args, **kwargs):
		super(UserChangeForm, self).__init__(*args, **kwargs)

		self.fields['first_name'].label= 'Nom'
		self.fields['first_name'].widget.attrs['class'] = 'form-control'
		self.fields['email'].label= 'Adresse Email'
		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['last_name'].label= 'Prénom'
		self.fields['last_name'].widget.attrs['class'] = 'form-control'
		self.fields['is_collab'].label= 'Intervenant'		
		self.fields['is_collab'].widget.attrs['class'] = 'form-check-input'
		self.fields['is_collab'].widget.attrs['name'] = 'radio-statut'
		self.fields['is_responsable'].label= 'Responsable'
		self.fields['is_responsable'].widget.attrs['class'] = 'form-check-input'
		self.fields['is_client'].label= 'Client'
		self.fields['is_client'].widget.attrs['class'] = 'form-check-input'
		self.fields['is_client'].widget.attrs['name'] = 'radio-statut'

		self.fields['email'].error_messages['unique']='Un compte est déjà créé avec cette adresse email'


class UserLoginForm(AuthenticationForm):

	error_css_class = 'text-xs font-weight-bold text-danger text-uppercase '
		
	

	def __init__(self, *args, **kwargs):
		super(UserLoginForm, self).__init__(*args, **kwargs)	
		
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control form-control-user'
	

		

		