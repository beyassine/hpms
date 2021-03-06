from django.urls import path
from . import views 


urlpatterns=[

	path('',views.home,name='home'),
	path('form/',views.form,name='form'),
	path('list/',views.listintervention,name='listintervention'),

	#API
	path('api/<int:pk>/getplanification/', views.getplanification, name="getplanification"),
	path('api/<int:pk>/getsitetplanification', views.getsitetplanification, name="getsitetplanification"),

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

	###Cat??gorie Equipement
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

	###QR CODE
	path('sites/<int:pk1>/equipementintervention/<int:pk2>',views.equipementintervention,name='equipementintervention'),
	path('administrateur/sites/<int:pk>/getqr',views.getqr,name='getqr'),
	path('sites/<int:pk1>/<int:pk2>/qr',views.QrPDF.as_view(),name='QrPDF'),

	###RondeQr CODE
	path('administrateur/sites/<int:pk>/getrondeqr',views.getrondeqr,name='getrondeqr'),
	path('sites/<int:pk1>/<int:pk2>/rondeqr',views.RondeQrPDF.as_view(),name='RondeQrPDF'),
	
	## Sites
	### Tableau de Bord
	path('sites/<int:pk>',views.sitehome,name='sitehome'),
	### Rondes
	path('sites/<int:pk>/ronde',views.ronde,name='ronde'),
	path('sites/<int:pk1>/ronde/<int:pk2>/ajouter',views.newronde,name='rondenew'),
	### Maintenance Curative
	path('sites/<int:pk>/curative',views.curative,name='curative'),
	path('sites/curative/<int:pk>/nouveau',views.newcurative,name='newcurative'),
	path('sites/curative/<int:pk>/modifier',views.updatecurative,name='updatecurative'),
	path('sites/curative/<int:pk>/supprimer',views.deletecurative,name='deletecurative'),
	path('sites/curative/intervention/<int:pk>',views.curativedetail,name='curativedetail'),
	path('sites/curative/<int:pk>/modifierfiche',views.fichecurative,name='fichecurative'),
	### Maintenance Pr??ventive
	path('sites/<int:pk>/preventive',views.preventive,name='preventive'),
	path('sites/preventive/<int:pk>/nouveau',views.newpreventive,name='newpreventive'),
	path('sites/<int:pk1>/preventive/intervention/<int:pk2>',views.intervention,name='intervention'),
	path('sites/preventive/<int:pk>/modifier',views.updateintervention,name='updateintervention'),
	path('sites/<int:pk1>/preventive/<int:pk2>/modifier',views.preventiveupdate,name='preventiveupdate'),
	path('sites/preventive/<int:pk>/supprimer',views.deletepreventive,name='deletepreventive'),
	### Gestion de stock
	path('sites/<int:pk>/stock',views.stock,name='stock'),
	path('sites/stock/<int:pk>/noveau',views.newstock,name='newstock'),
	path('sites/stock/<int:pk>',views.stockdetail,name='stockdetail'),
	path('sites/stock/<int:pk>/modifier',views.updatestock,name='stockupdate'),
	path('sites/stock/<int:pk>/supprimer',views.deletestock,name='stockdelete'),
	path('sites/stock/<int:pk>/noveaumvmnt',views.newmvmnt,name='newmouvement'),
	path('sites/stock/<int:pk>/supprimermvmnt',views.deletemvmnt,name='deletmouvement'),
	
]
