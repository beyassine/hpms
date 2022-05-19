import django_filters
from .models import	*
from django import forms
from django.utils import timezone



class CurativeFliter(django_filters.FilterSet):

	criticite_choices=(('c1','C1'),('c2','C2'),('c3','C3'))
	statut_choices=(('Enregistrée','Enregistrée'),
		('Pris en charge','Pris en charge'),
		('Travaux en cours','Travaux en cours'),
		('Pending','Pending'),
		('Résolue','Résolue'),
		)

	date_debut=django_filters.DateFilter(field_name="datedebut",lookup_expr="date__gte",
		label='Date Réclamation Début',widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control col-sm-10', 'placeholder':'Select Date','type': 'date'}))
	date_fin=django_filters.DateFilter(field_name="datedebut",lookup_expr="date__lte",
		label='Date Réclamat Fin',widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control col-sm-10', 'placeholder':'Select Date','type': 'date'}))

	
	souslot=django_filters.ChoiceFilter(field_name="souslot",empty_label='------',widget=forms.Select(attrs={'class':'form-control',}),label='SousLot',)
	categorie=django_filters.ChoiceFilter(field_name="categorie",empty_label='------',widget=forms.Select(attrs={'class':'form-control',}),label='Categorie',)
	equipement=django_filters.ChoiceFilter(field_name="equipement",empty_label='------',widget=forms.Select(attrs={'class':'form-control',}),label='Equipement',)
	criticite= django_filters.ChoiceFilter(choices=criticite_choices,field_name="criticite",empty_label='------',widget=forms.Select(attrs={'class':'form-control',}),label='Criticité',)
	statut= django_filters.ChoiceFilter(choices=statut_choices,field_name="statut",empty_label='------',widget=forms.Select(attrs={'class':'form-control',}),label='Statut',)
	

	class Meta:
		model=Tache
		fields=('date_debut','date_fin','criticite','statut','lot','zone','souslot','categorie','equipement',)
	
	def __init__(self,site,*args, **kwargs):
		super(CurativeFliter, self).__init__(*args, **kwargs)

		self.filters['zone'].queryset=Zone.objects.filter(site__id=site)
		self.filters['zone'].field.widget.attrs.update({'class': 'form-control'})
		self.filters['zone'].field.widget.attrs.update({'label': 'Zone'})
		self.filters['lot'].field.widget.attrs.update({'class': 'form-control'})


class RondeFliter(django_filters.FilterSet):
	

	class Meta:
		model=Ronde
		fields=('intervenant',)
	
	def __init__(self,site,*args, **kwargs):
		super(RondeFliter, self).__init__(*args, **kwargs)
		
		self.filters['intervenant'].queryset=Site.objects.get(id=site).intervenantsite.all()
		self.filters['intervenant'].field.widget.attrs.update({'class': 'form-control'})