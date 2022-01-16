from django.urls import path
from . import views 


urlpatterns=[

	path('',views.home,name='home'),
	path('form/',views.form,name='form'),
	path('list/',views.listintervention,name='listintervention'),

	#Ajax
	path('ajax/loadsouslot',views.loadsouslot,name='loadsouslot'),
	path('ajax/loadcategorie',views.loadcategorie,name='loadcategorie'),
	path('ajax/loadequipement',views.loadequipement,name='loadequipement'),

	#Administrateur

	##Sites
	path('administrateur/sites',views.sites,name='sites'),
	path('administrateur/sites/nouveau',views.newsite,name='newsite'),
	path('administrateur/sites/<int:pk>/modifier',views.updatesite,name='updatesite'),
	path('administrateur/sites/<int:pk>/supprimer',views.deletesite,name='deletesite'),
	path('administrateur/sites/<int:pk>',views.detailsite,name='detailsite'),
	path('administrateur/sites/<int:pk>/intervenants',views.siteaddintervenant,name='siteaddintervenant'),
	path('administrateur/sites/<int:pk>/responsables',views.siteaddresponsable,name='siteaddresponsable'),
	path('administrateur/sites/<int:pk>/clients',views.siteaddclient,name='siteaddclient'),

	###Zones
	path('administrateur/zones/<int:pk>/nouveau',views.newzone,name='newzone'),
	path('administrateur/zones/<int:pk>/modifier',views.updatezone,name='updatezone'),
	path('administrateur/zones/<int:pk>/supprimer',views.deletezone,name='deletezone'),


	##Equipements

	###Lots Equipement
	path('administrateur/lotequipements',views.lotequipements,name='lotequipements'),
	path('administrateur/lotequipements/<int:pk>/',views.detaillotequipement,name='detaillotequipement'),
	path('administrateur/lotequipements/nouveau',views.newlot,name='newlot'),
	path('administrateur/lotequipements/<int:pk>/modifier',views.updatelot,name='updatelot'),
	path('administrateur/lotequipements/<int:pk>/supprimer',views.deletelot,name='deletelot'),

	###Sous Lots Equipement
	path('administrateur/souslotequipements/<int:pk>/',views.detailsouslot,name='detailsouslot'),
	path('administrateur/souslotequipements/<int:pk>/nouveau',views.newsouslot,name='newsouslot'),
	path('administrateur/souslotequipements/<int:pk>/modifier',views.updatesouslot,name='updatesouslot'),
	path('administrateur/souslotequipements/<int:pk>/supprimer',views.deletesouslot,name='deletesouslot'),

	###Catégorie Equipement
	path('administrateur/categorieequipements/<int:pk>/',views.detailcategorie,name='detailcategorie'),
	path('administrateur/categorieequipements/<int:pk>/nouveau',views.newcategorie,name='newcategorie'),
	path('administrateur/categorieequipements/<int:pk>/modifier',views.updatecategorie,name='updatecategorie'),
	path('administrateur/categorieequipements/<int:pk>/supprimer',views.deletecategorie,name='deletecategorie'),

	###Equipement
	path('administrateur/equipements/<int:pk>/',views.detailequipement,name='detailequipement'),
	path('administrateur/equipements/<int:pk>/nouveau',views.newequipement,name='newequipement'),
	path('administrateur/equipements/<int:pk>/modifier',views.updateequipement,name='updateequipement'),
	path('administrateur/equipements/<int:pk>/supprimer',views.deleteequipement,name='deleteequipement'),

	###Collabs
	path('administrateur/collaborateurs',views.collabs,name='collabs'),
	path('administrateur/collaborateurs/nouveau',views.newcollab,name='newcollab'),
	path('administrateur/collaborateurs/<int:pk>/modifier',views.updatecollab,name='updatecollab'),
	path('administrateur/collaborateurs/<int:pk>/supprimer',views.deletecollab,name='deletecollab'),
	
	## Sites
	### Tableau de Bord
	path('sites/<int:pk>',views.sitehome,name='sitehome'),
	### Maintenance Curative
	path('sites/<int:pk>/curative',views.curative,name='curative'),
	path('sites/curative/<int:pk>/nouveau',views.newcurative,name='newcurative'),
	path('sites/curative/<int:pk>/modifier',views.updatecurative,name='updatecurative'),
	path('sites/curative/<int:pk>/supprimer',views.deletecurative,name='deletecurative'),
	path('sites/curative/intervention/<int:pk>',views.curativedetail,name='curativedetail'),
	### Maintenance Préventive
	path('sites/<int:pk>/preventive',views.preventive,name='preventive'),
	### Gestion de stock
	path('sites/<int:pk>/stock',views.stock,name='stock'),
	
	
]
