from django import forms
from .models import *
from users.models import User

##Site
class SiteForm(forms.ModelForm):

	error_css_class = 'text-xs font-weight-bold text-danger text-uppercase '

	class Meta:
		model= Site
		fields=('designation','libelle')		
		

	def __init__(self, *args, **kwargs):
		super(SiteForm, self).__init__(*args, **kwargs)
        							
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'

class IntervenantsiteForm(forms.ModelForm):

	error_css_class = 'text-xs font-weight-bold text-danger text-uppercase '

	class Meta:
		model= Site
		fields=('intervenantsite',)		

		widgets={'intervenantsite':forms.CheckboxSelectMultiple}

	def __init__(self, *args, **kwargs):
		super(IntervenantsiteForm, self).__init__(*args, **kwargs)
        							
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'
			self.fields['intervenantsite'].queryset =User.objects.filter(is_collab=True)
			self.fields['intervenantsite'].label = ''

class ResponsablesiteForm(forms.ModelForm):

	error_css_class = 'text-xs font-weight-bold text-danger text-uppercase '

	class Meta:
		model= Site
		fields=('responsablesite',)		

		widgets={'responsablesite':forms.CheckboxSelectMultiple,}

	def __init__(self, *args, **kwargs):
		super(ResponsablesiteForm, self).__init__(*args, **kwargs)
        							
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'
			self.fields['responsablesite'].queryset =User.objects.filter(is_responsable=True)
			self.fields['responsablesite'].label = ''

class ClientsiteForm(forms.ModelForm):

	error_css_class = 'text-xs font-weight-bold text-danger text-uppercase '

	class Meta:
		model= Site
		fields=('clientsite',)		

		widgets={'clientsite':forms.CheckboxSelectMultiple,}

	def __init__(self, *args, **kwargs):
		super(ClientsiteForm, self).__init__(*args, **kwargs)
        							
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'
			self.fields['clientsite'].queryset =User.objects.filter(is_client=True)
			self.fields['clientsite'].label = ''

			
##Zone
class ZoneForm(forms.ModelForm):

	error_css_class = 'text-xs font-weight-bold text-danger text-uppercase '

	class Meta:
		model= Zone
		fields=('designation','libelle')		

	def __init__(self, *args, **kwargs):
		super(ZoneForm, self).__init__(*args, **kwargs)
        							
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'


##Lots Equipement
class LotForm(forms.ModelForm):

	error_css_class = 'text-xs font-weight-bold text-danger text-uppercase '

	class Meta:
		model= Lot
		fields=('designation','libelle')		

	def __init__(self, *args, **kwargs):
		super(LotForm, self).__init__(*args, **kwargs)
        							
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'

##Sous Lots Equipement
class SouslotForm(forms.ModelForm):

	error_css_class = 'text-xs font-weight-bold text-danger text-uppercase '

	class Meta:
		model= Souslot
		fields=('designation','libelle')		

	def __init__(self, *args, **kwargs):
		super(SouslotForm, self).__init__(*args, **kwargs)
        							
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'

##Categories Equipement
class CategorieForm(forms.ModelForm):

	error_css_class = 'text-xs font-weight-bold text-danger text-uppercase '

	class Meta:
		model= Categorie
		fields=('designation','libelle')		

	def __init__(self, *args, **kwargs):
		super(CategorieForm, self).__init__(*args, **kwargs)
        							
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'

##Equipement
class EquipementForm(forms.ModelForm):

	error_css_class = 'text-xs font-weight-bold text-danger text-uppercase '

	class Meta:
		model= Equipement
		fields=('designation','libelle')		

	def __init__(self, *args, **kwargs):
		super(EquipementForm, self).__init__(*args, **kwargs)
        							
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'

#Maintenance

class CurativeForm(forms.ModelForm):

	error_css_class = 'text-xs font-weight-bold text-danger text-uppercase '

	class Meta:
		model= Tache
		fields=('criticite','objet','statut','intervenant','zone','lot','souslot','categorie','equipement','imagear')		
		widgets={'datedebut':forms.DateTimeInput(format=('%d/%m/%Y %H:%M'), attrs={'class':'form-control'}),
				'datefin':forms.DateTimeInput(format=('%d/%m/%Y %H:%M'), attrs={'class':'form-control'}),
				}
		
	def __init__(self,site,*args, **kwargs):
		super(CurativeForm, self).__init__(*args, **kwargs)
        							
		
		self.fields['intervenant'].queryset = site.intervenantsite.all()
		self.fields['intervenant'].empty_label = "------"	
		self.fields['zone'].queryset = Zone.objects.filter(site=site)
		self.fields['zone'].empty_label = "------"	
		self.fields['lot'].empty_label = "------"	
		self.fields['souslot'].queryset = Souslot.objects.none()		
		self.fields['souslot'].empty_label = "------"	
		self.fields['categorie'].queryset = Categorie.objects.none()
		self.fields['categorie'].empty_label = "------"	
		self.fields['equipement'].queryset = Equipement.objects.none()
		self.fields['equipement'].empty_label = "------"	

		if 'lot' in self.data:
			try:
				lotid= int(self.data.get('lot'))
				lot=Lot.objects.get(id=lotid)					
				self.fields['souslot'].queryset =Souslot.objects.filter(lot=lot)
			except (ValueError, TypeError):
				pass  
		elif self.instance.pk:
			self.fields['souslot'].queryset = Souslot.objects.filter(lot=self.instance.lot)
		
		if 'souslot' in self.data:
			try:
				souslotid= int(self.data.get('souslot'))
				souslot=Souslot.objects.get(id=souslotid)					
				self.fields['categorie'].queryset =Categorie.objects.filter(souslot=souslot)
			except (ValueError, TypeError):
				pass  
		elif self.instance.pk:
			self.fields['categorie'].queryset = Categorie.objects.filter(souslot=self.instance.souslot)
		
		if 'categorie' in self.data:
			try:
				categorieid= int(self.data.get('categorie'))
				categorie=Categorie.objects.get(id=categorieid)					
				self.fields['equipement'].queryset =Equipement.objects.filter(categorie=categorie)
			except (ValueError, TypeError):
				pass  
		elif self.instance.pk:
			self.fields['equipement'].queryset = Equipement.objects.filter(categorie=self.instance.categorie)
		
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'

class UpdateCurativeForm(forms.ModelForm):

	error_css_class = 'text-xs font-weight-bold text-danger text-uppercase '

	class Meta:
		model= Tache
		fields=('criticite','objet','statut','intervenant','zone','lot','souslot','categorie','equipement','datedebut','datefin','imagear','imagepr')		
		widgets={'datedebut':forms.DateTimeInput(format=('%d/%m/%Y %H:%M'), attrs={'class':'form-control'}),
				'datefin':forms.DateTimeInput(format=('%d/%m/%Y %H:%M'), attrs={'class':'form-control'}),
				}
		
	def __init__(self,site,*args, **kwargs):
		super(UpdateCurativeForm, self).__init__(*args, **kwargs)
        							
		
		self.fields['intervenant'].queryset = site.intervenantsite.all()
		self.fields['intervenant'].empty_label = "------"	
		self.fields['zone'].queryset = Zone.objects.filter(site=site)
		self.fields['zone'].empty_label = "------"	
		self.fields['lot'].empty_label = "------"	
		self.fields['souslot'].queryset = Souslot.objects.none()		
		self.fields['souslot'].empty_label = "------"	
		self.fields['categorie'].queryset = Categorie.objects.none()
		self.fields['categorie'].empty_label = "------"	
		self.fields['equipement'].queryset = Equipement.objects.none()
		self.fields['equipement'].empty_label = "------"	

		if 'lot' in self.data:
			try:
				lotid= int(self.data.get('lot'))
				lot=Lot.objects.get(id=lotid)					
				self.fields['souslot'].queryset =Souslot.objects.filter(lot=lot)
			except (ValueError, TypeError):
				pass  
		elif self.instance.pk:
			self.fields['souslot'].queryset = Souslot.objects.filter(lot=self.instance.lot)
		
		if 'souslot' in self.data:
			try:
				souslotid= int(self.data.get('souslot'))
				souslot=Souslot.objects.get(id=souslotid)					
				self.fields['categorie'].queryset =Categorie.objects.filter(souslot=souslot)
			except (ValueError, TypeError):
				pass  
		elif self.instance.pk:
			self.fields['categorie'].queryset = Categorie.objects.filter(souslot=self.instance.souslot)
		
		if 'categorie' in self.data:
			try:
				categorieid= int(self.data.get('categorie'))
				categorie=Categorie.objects.get(id=categorieid)					
				self.fields['equipement'].queryset =Equipement.objects.filter(categorie=categorie)
			except (ValueError, TypeError):
				pass  
		elif self.instance.pk:
			self.fields['equipement'].queryset = Equipement.objects.filter(categorie=self.instance.categorie)
		
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'

class FicheForm(forms.ModelForm):

	error_css_class = 'text-xs font-weight-bold text-danger text-uppercase '

	class Meta:
		model= Tache
		fields=('description','effet','rechange')
		
	def __init__(self,*args, **kwargs):
		super(FicheForm, self).__init__(*args, **kwargs)
		
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'
		
		
#Stock

class StockForm(forms.ModelForm):

	error_css_class = 'text-xs font-weight-bold text-danger text-uppercase '

	class Meta:
		model= Stock
		fields=('stock','lot','souslot','categorie','equipement',)		

	def __init__(self,site,*args, **kwargs):
		super(StockForm, self).__init__(*args, **kwargs)

		self.fields['lot'].empty_label = "------"	
		self.fields['souslot'].queryset = Souslot.objects.none()		
		self.fields['souslot'].empty_label = "------"	
		self.fields['categorie'].queryset = Categorie.objects.none()
		self.fields['categorie'].empty_label = "------"	
		self.fields['equipement'].queryset = Equipement.objects.none()
		self.fields['equipement'].empty_label = "------"	

		if 'lot' in self.data:
			try:
				lotid= int(self.data.get('lot'))
				lot=Lot.objects.get(id=lotid)					
				self.fields['souslot'].queryset =Souslot.objects.filter(lot=lot)
			except (ValueError, TypeError):
				pass  
		elif self.instance.pk:
			self.fields['souslot'].queryset = Souslot.objects.filter(lot=self.instance.lot)
		
		if 'souslot' in self.data:
			try:
				souslotid= int(self.data.get('souslot'))
				souslot=Souslot.objects.get(id=souslotid)					
				self.fields['categorie'].queryset =Categorie.objects.filter(souslot=souslot)
			except (ValueError, TypeError):
				pass  
		elif self.instance.pk:
			self.fields['categorie'].queryset = Categorie.objects.filter(souslot=self.instance.souslot)
		
		if 'categorie' in self.data:
			try:
				categorieid= int(self.data.get('categorie'))
				categorie=Categorie.objects.get(id=categorieid)					
				self.fields['equipement'].queryset =Equipement.objects.filter(categorie=categorie)
			except (ValueError, TypeError):
				pass  
		elif self.instance.pk:
			self.fields['equipement'].queryset = Equipement.objects.filter(categorie=self.instance.categorie)
		
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'

## Mouvement Stock

class MouvementForm(forms.ModelForm):

	error_css_class = 'text-xs font-weight-bold text-danger text-uppercase '

	class Meta:
		model= Mouvement
		fields=('mouvement','quantite')		

	def __init__(self,*args, **kwargs):
		super(MouvementForm, self).__init__(*args, **kwargs)
        							
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'
