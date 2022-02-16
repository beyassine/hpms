from django.db import models
from django.utils import timezone
from django.urls import reverse
from users.models import User
from PIL import Image

#Site
class Site(models.Model):
	designation=models.CharField(max_length=1000,verbose_name='Désignation',default='')
	libelle=models.CharField(max_length=100,verbose_name='Libellé',default='',blank=True)
	responsablesite=models.ManyToManyField(User,blank=True,related_name='responsablesite')
	intervenantsite=models.ManyToManyField(User,blank=True,related_name='intervenantsite')
	clientsite=models.ManyToManyField(User,blank=True,related_name='clientsite')

	def __str__(self):
		return f'{self.designation}'

#Zone
class Zone(models.Model):	
	site=models.ForeignKey(Site,on_delete=models.CASCADE,verbose_name="Site")
	designation=models.CharField(max_length=1000,verbose_name='Désignation',default='')
	libelle=models.CharField(max_length=100,verbose_name='Libellé',default='',blank=True)

	def __str__(self):
		return f'{self.designation}'


#Lots Equipements
class Lot(models.Model):
	designation=models.CharField(max_length=1000,verbose_name='Désignation',default='')
	libelle=models.CharField(max_length=100,verbose_name='Libellé',default='',blank=True)

	def __str__(self):
		return f'{self.designation}'

#Sous Lots Equipements
class Souslot(models.Model):
	lot=models.ForeignKey(Lot,on_delete=models.CASCADE,verbose_name="Lot")
	designation=models.CharField(max_length=1000,verbose_name='Désignation',default='')
	libelle=models.CharField(max_length=100,verbose_name='Libellé',default='',blank=True)

	def __str__(self):
		return f'{self.designation}'

#Categorie Equipements
class Categorie(models.Model):
	souslot=models.ForeignKey(Souslot,on_delete=models.CASCADE,verbose_name="Sous Lot")
	designation=models.CharField(max_length=1000,verbose_name='Désignation',default='')
	libelle=models.CharField(max_length=100,verbose_name='Libellé',default='',blank=True)

	def __str__(self):
		return f'{self.designation}'

#Equipements
class Equipement(models.Model):
	categorie=models.ForeignKey(Categorie,on_delete=models.CASCADE,verbose_name="Catégorie")
	designation=models.CharField(max_length=1000,verbose_name='Désignation',default='')
	libelle=models.CharField(max_length=100,verbose_name='Libellé',default='',blank=True)

	def __str__(self):
		return f'{self.designation}'

#Stock

class Stock(models.Model):

	site=models.ForeignKey(Site,on_delete=models.CASCADE,verbose_name="Site")
	lot=models.ForeignKey(Lot,on_delete=models.SET_NULL,null=True,verbose_name='Lot',default='')	
	souslot=models.ForeignKey(Souslot,on_delete=models.SET_NULL,null=True,verbose_name='Sous-Lot',default='')
	categorie=models.ForeignKey(Categorie,on_delete=models.SET_NULL,null=True,verbose_name='Catégorie',default='')		
	equipement=models.ForeignKey(Equipement,on_delete=models.SET_NULL,null=True,verbose_name='Equipement',default='')
	stock=models.IntegerField(default=0,verbose_name='Stock')

class Mouvement(models.Model):
	mvmnt=((1,'Entrée'),(2,'Sortie'))
	date=models.DateTimeField(default=timezone.now)
	stock=models.ForeignKey(Stock,on_delete=models.CASCADE,verbose_name="Stock")
	mouvement=models.IntegerField(choices=mvmnt,default='1')
	quantite=models.IntegerField(default=0,verbose_name='Quantité')



# Tache

class Tache(models.Model):

	planifie=models.BooleanField(default=False)
	
	criticite=(('c1','C1'),('c2','C2'),('c3','C3'))

	statut_choices=(('Enregistrée','Enregistrée'),
		('Pris en charge','Pris en charge'),
		('Travaux en cours','Travaux en cours'),
		('Pending','Pending'),
		('Résolue','Résolue'),
		)

	auteur=models.ForeignKey(User, on_delete=models.SET_NULL,null=True ,verbose_name='Auteur')
	criticite=models.CharField(max_length=100, choices=criticite,default='c1')
	statut=models.CharField(max_length=100,choices=statut_choices,default='Pris en charge')
	objet=models.CharField(max_length=1000,verbose_name='Objet',default='')	
	#Intervenant
	intervenant=models.ForeignKey(User,on_delete=models.SET_NULL,null=True ,related_name='Intervenant')
	#Site
	site=models.ForeignKey(Site, on_delete=models.CASCADE,verbose_name='Site',default='')
	zone=models.ForeignKey(Zone,on_delete=models.SET_NULL,null=True, verbose_name='Zone',default='')
	#Equipement
	lot=models.ForeignKey(Lot,on_delete=models.SET_NULL,null=True,verbose_name='Lot',default='')	
	souslot=models.ForeignKey(Souslot,on_delete=models.SET_NULL,null=True,verbose_name='Sous-Lot',default='')
	categorie=models.ForeignKey(Categorie,on_delete=models.SET_NULL,null=True,verbose_name='Catégorie',default='')		
	equipement=models.ForeignKey(Equipement,on_delete=models.SET_NULL,null=True,verbose_name='Equipement',default='')
	#date de raclamation 
	datecreated=models.DateTimeField(default=timezone.now)
	# date Prise en charge
	datecharge=models.DateTimeField(default=timezone.now)
	#date début travaux
	datedebut=models.DateTimeField(default=timezone.now,verbose_name='Date Début')
	debut=models.BooleanField(default=False)
	# pending
	pending=models.BooleanField(default=False)
	pendingstart=models.DateTimeField(default=timezone.now,verbose_name='pendingstart')
	endpending=models.BooleanField(default=False)
	pendingend=models.DateTimeField(default=timezone.now,verbose_name='pendingend')
	#date résolution
	resolu=models.BooleanField(default=False)
	dateresolu=models.DateTimeField(default=timezone.now,verbose_name='dateresolu')
	#date clôture
	clos=models.BooleanField(default=False)
	datefin=models.DateTimeField(default=timezone.now,verbose_name='Date Fin')
	#Périodicité
	periodicite=models.IntegerField(default=1,verbose_name='Durée d\'intervention (jours)')
	#Fiche
	description=models.TextField(verbose_name='Description',default='',blank=True)
	effet=models.TextField(verbose_name=' Effet sur équipement/ouvrage',default='',blank=True)
	rechange=models.TextField(verbose_name=' Piéces de rechange/Consommable',default='',blank=True)
	#Images
	imagepr = models.ImageField(null=True,verbose_name=' Image Etat Finale',upload_to='interventions',blank=True)
	imagear = models.ImageField(null=True,verbose_name=' Image Etat Initiale ',upload_to='interventions',blank=True)

	def __str__(self):
		return f'{self.objet }' 

	@property
	def get_html_url(self):
		url = reverse('tachedeatail', args=(self.id,))
		return f'<a href="{url}"> {self.titre} </a>'
