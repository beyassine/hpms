from django.shortcuts import render,redirect
from .forms import *
from .filters import *
from django.contrib import messages
from users.models import *
from users.forms import *
from django.contrib.auth.decorators import login_required
from datetime import datetime, date, timedelta
import calendar
from dateutil.relativedelta import relativedelta
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import parsers
from .serializers import *
import locale
from django.template.loader import render_to_string
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
import os
from django.conf import settings
from django.http import HttpResponse,JsonResponse


#locale.setlocale(locale.LC_ALL, 'fr_FR')

def home(request):
    return render(request,'dashboard/home.html')

# Templates
def form(request):
    return render(request,'dashboard/form.html')

def listintervention(request):
    return render(request,'dashboard/list.html')

# API
@api_view(['GET'])
def getplanification(request, pk):
    planification = Planification.objects.get(id=pk)
    serializer = PlanificationSerializer(planification)
    return Response(serializer.data)

@api_view(['GET'])
def getsitetplanification(request, pk):
    ctx = {'day': request.GET.get('day', None)}
    site = Site.objects.get(id=pk)
    serializer = PlanificationSiteSerializer(site,context=ctx)
    return Response(serializer.data)


#Views

## Ajax
def loadsouslot(request):
	lot=request.GET.get('lotid')	
	souslots=Souslot.objects.filter(lot=lot)
	return render(request,'dashboard/ajax/loadsouslot.html',{'souslots':souslots})

def loadcategorie(request):
	souslot=request.GET.get('souslotid')	
	categories=Categorie.objects.filter(souslot=souslot)
	return render(request,'dashboard/ajax/loadcategorie.html',{'categories':categories})

def loadequipement(request):
	categorie=request.GET.get('categorieid')	
	equipements=Equipement.objects.filter(categorie=categorie)
	return render(request,'dashboard/ajax/loadequipement.html',{'equipements':equipements})

    
## Administrateur

### Sites
 
def sites(request):
    sites=Site.objects.all()
    return render(request,'dashboard/administration/sites.html',{'sites':sites})

def detailsite(request,pk):
    site=Site.objects.get(id=pk)
    zones=Zone.objects.filter(site=site)
    intervenants=site.intervenantsite.all()
    responsables=site.responsablesite.all()
    clients=site.clientsite.all()
    context={'site':site,'zones':zones,'intervenants':intervenants,'responsables':responsables,'clients':clients}
    return render(request,'dashboard/administration/sitedetail.html',context)

def siteaddintervenant(request,pk):
    site=Site.objects.get(id=pk)
    if request.method=="POST":
        form=IntervenantsiteForm(request.POST,instance=site)
        if form.is_valid():
            form.save()
            messages.success(request, f'Site modifi?? avec succ??s')
            return redirect('detailsite',pk=site.id)
    else:
        form=IntervenantsiteForm(instance=site)

    return render(request,'dashboard/administration/siteaddintervenant.html',{'form':form})

def siteaddresponsable(request,pk):
    site=Site.objects.get(id=pk)
    if request.method=="POST":
        form=ResponsablesiteForm(request.POST,instance=site)
        if form.is_valid():
            form.save()
            messages.success(request, f'Site modifi?? avec succ??s')
            return redirect('detailsite',pk=site.id)
    else:
        form=ResponsablesiteForm(instance=site)

    return render(request,'dashboard/administration/siteaddresponsable.html',{'form':form})

def siteaddclient(request,pk):
    site=Site.objects.get(id=pk)
    if request.method=="POST":
        form=ClientsiteForm(request.POST,instance=site)
        if form.is_valid():
            form.save()
            messages.success(request, f'Site modifi?? avec succ??s')
            return redirect('detailsite',pk=site.id)
    else:
        form=ClientsiteForm(instance=site)

    return render(request,'dashboard/administration/siteaddclient.html',{'form':form})

def newsite(request):
    if request.method=="POST":
        form=SiteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Nouveau Site cr???? avec succ??s')
            return redirect('sites')
    else:
        form=SiteForm()

    return render(request,'dashboard/administration/sitenew.html',{'form':form})

def updatesite(request,pk):    
    site = Site.objects.get(id=pk)

    if request.method=="POST":
        form=SiteForm(request.POST,instance=site)
        if form.is_valid():
            form.save()
            messages.success(request, f'Site modifi?? avec succ??s')
            return redirect('sites')
    else:
        form=SiteForm(instance=site)

    return render(request,'dashboard/administration/siteupdate.html',{'form':form})

def deletesite(request,pk):
    site=Site.objects.get(id=pk)
    if request.method=="POST":
        site.delete()
        messages.success(request, f'Site supprim?? avec succ??s')
        return redirect('sites')
    return render(request,'dashboard/administration/sitedelete.html',{'site':site})

### Zones

def newzone(request,pk):
    site=Site.objects.get(id=pk)
    if request.method=="POST":
        form=ZoneForm(request.POST)
        if form.is_valid():
            form.instance.site=site
            form.save()
            messages.success(request, f'Nouvelle zone cr???? avec succ??s')
            return redirect('detailsite',pk=site.id)
    else:
        form=ZoneForm()

    return render(request,'dashboard/administration/zonenew.html',{'form':form})


def updatezone(request,pk):
    zone=Zone.objects.get(id=pk)
    site=zone.site
    if request.method=="POST":
        form=ZoneForm(request.POST,instance=zone)
        if form.is_valid():
            form.save()
            messages.success(request, f'Zone modifi??e avec succ??s')
            return redirect('detailsite',pk=site.id)
    else:
        form=ZoneForm(instance=zone)

    return render(request,'dashboard/administration/zoneupdate.html',{'form':form})


def deletezone(request,pk):
    zone=Zone.objects.get(id=pk)
    site=zone.site
    if request.method=="POST":
        zone.delete()
        messages.success(request, f'Zone supprim??e avec succ??s')
        return redirect('detailsite',pk=site.id)
    return render(request,'dashboard/administration/zonedelete.html',{'zone':zone})


### Equipements

#### Lots Equipements

def lotequipements(request):
    lots=Lot.objects.all()
    return render(request,'dashboard/administration/lotequipements.html',{'lots':lots})

def detaillotequipement(request,pk):
    lot=Lot.objects.get(id=pk)
    slots=Souslot.objects.filter(lot=lot)
    context={'lot':lot,'slots':slots}
    return render(request,'dashboard/administration/detaillotequipement.html',context)

def newlot(request):
    if request.method=="POST":
        form=LotForm(request.POST)
        if form.is_valid():
            lot=form.save()
            messages.success(request, f'Nouveau Lot cr???? avec succ??s')
            return redirect('lotequipements')
    else:
        form=LotForm()

    return render(request,'dashboard/administration/lotnew.html',{'form':form})

def updatelot(request,pk):    
    lot = Lot.objects.get(id=pk)

    if request.method=="POST":
        form=LotForm(request.POST,instance=lot)
        if form.is_valid():
            form.save()
            messages.success(request, f'Lot Equipement modifi?? avec succ??s')
            return redirect('lotequipements')
    else:
        form=SiteForm(instance=lot)

    return render(request,'dashboard/administration/lotupdate.html',{'form':form})

def deletelot(request,pk):
    lot = Lot.objects.get(id=pk)

    if request.method=="POST":
        lot.delete()
        messages.success(request, f'Lot Equipement supprim?? avec succ??s')
        return redirect('lotequipements')
    return render(request,'dashboard/administration/lotdelete.html',{'lot':lot})

#### Sous Lots Equipements

def detailsouslot(request,pk):
    slot=Souslot.objects.get(id=pk)
    cats=Categorie.objects.filter(souslot=slot)
    context={'slot':slot,'cats':cats}

    return render(request,'dashboard/administration/detailsouslot.html',context)

def newsouslot(request,pk):
    lot=Lot.objects.get(id=pk)
    if request.method=="POST":
        form=SouslotForm(request.POST)
        if form.is_valid():
            form.instance.lot=lot
            form.save()
            messages.success(request, f'Nouveau sous-lot cr???? avec succ??s')
            return redirect('detaillotequipement',pk=lot.id)
    else:
        form=SouslotForm()

    return render(request,'dashboard/administration/souslotnew.html',{'form':form})

def updatesouslot(request,pk):
    slot=Souslot.objects.get(id=pk)
    lot=slot.lot
    if request.method=="POST":
        form=SouslotForm(request.POST,instance=slot)
        if form.is_valid():
            messages.success(request, f'Sous-Lot modifi?? avec succ??s')
            return redirect('detaillotequipement',pk=lot.id)
    else:
        form=SouslotForm(instance=slot)

    context={'form':form,'slot':slot}

    return render(request,'dashboard/administration/souslotupdate.html',context)

def deletesouslot(request,pk):
    slot=Souslot.objects.get(id=pk)
    lot=slot.lot
    if request.method=="POST":
        slot.delete()
        messages.success(request, f'Sous-Lot supprim?? avec succ??s')
        return redirect('detaillotequipement',pk=lot.id)
    

    return render(request,'dashboard/administration/souslotdelete.html',{'slot':slot})

#### Cat??gories

def detailcategorie(request,pk):
    cat=Categorie.objects.get(id=pk)
    equipements=Equipement.objects.filter(categorie=cat)
    context={'cat':cat,'equipements':equipements}

    return render(request,'dashboard/administration/detailcategorie.html',context)

def newcategorie(request,pk):
    slot=Souslot.objects.get(id=pk)
    if request.method=="POST":
        form=CategorieForm(request.POST)
        if form.is_valid():
            form.instance.souslot=slot
            cat=form.save()
            messages.success(request, f'Nouvelle Cat??gorie cr????e avec succ??s')
            return redirect('detailsouslot',pk=slot.id)
    else:
        form=CategorieForm()

    return render(request,'dashboard/administration/categorienew.html',{'form':form})

def updatecategorie(request,pk):
    cat=Categorie.objects.get(id=pk)
    slot=cat.souslot
    if request.method=="POST":
        form=CategorieForm(request.POST,instance=cat)
        if form.is_valid():
            messages.success(request, f'Cat??gorie modifi??e avec succ??s')
            return redirect('detailsouslot',pk=slot.id)
    else:
        form=CategorieForm(instance=cat)

    context={'form':form,'cat':cat}

    return render(request,'dashboard/administration/categorieupdate.html',context)

def deletecategorie(request,pk):
    cat=Categorie.objects.get(id=pk)
    slot=cat.souslot
    if request.method=="POST":
        cat.delete()
        messages.success(request, f'Cat??gorie supprim?? avec succ??s')
        return redirect('detailsouslot',pk=slot.id)
    

    return render(request,'dashboard/administration/categoriedelete.html',{'cat':cat})

#### Equipements

def detailequipement(request,pk):
    equipement=Equipement.objects.get(id=pk)
    context={'equipement':equipement}

    return render(request,'dashboard/administration/detailequipement.html',context)

def newequipement(request,pk):
    cat=Categorie.objects.get(id=pk)
    if request.method=="POST":
        form=EquipementForm(request.POST)
        if form.is_valid():
            form.instance.categorie=cat
            form.save()
            messages.success(request, f'Nouveau Equipement cr???? avec succ??s')
            return redirect('detailcategorie',pk=cat.id)
    else:
        form=EquipementForm()

    return render(request,'dashboard/administration/equipementnew.html',{'form':form})

def updateequipement(request,pk):
    equipement=Equipement.objects.get(id=pk)
    cat=equipement.categorie
    if request.method=="POST":
        form=EquipementForm(request.POST,instance=equipement)
        if form.is_valid():
            messages.success(request, f'Equipement modifi?? avec succ??s')
            return redirect('detailcategorie',pk=cat.id)
    else:
        form=CategorieForm(instance=equipement)

    context={'form':form,'equipement':equipement}

    return render(request,'dashboard/administration/categorieupdate.html',context)

def deleteequipement(request,pk):
    equipement=Equipement.objects.get(id=pk)
    cat=equipement.categorie
    if request.method=="POST":
        equipement.delete()
        messages.success(request, f'Equipement supprim?? avec succ??s')
        return redirect('detailcategorie',pk=cat.id)
    

    return render(request,'dashboard/administration/equipementdelete.html',{'equipement':equipement})

### QR CODE

def equipementintervention(request,pk1,pk2):
    site=Site.objects.get(id=pk1)
    equipement=Equipement.objects.get(id=pk2)
    m = get_date(request.GET.get('month', None))
    month = m.strftime("%Y-%m-%d")
    tm = m.strftime("%m")
    pm = (m - relativedelta(months=1)).strftime("%m-%Y")
    nm = (m + relativedelta(months=1)).strftime("%m-%Y")
    date_obj = datetime.strptime(month, '%Y-%m-%d')
    datefin = str(date_obj.year) + '-' + str(date_obj.month) + '-' + \
            str(calendar.monthrange(date_obj.year, date_obj.month)[1])
    datedebut = str(date_obj.year) + '-' + str(date_obj.month) + '-' + '01'
   
    taches=Tache.objects.filter(site=site,equipement=equipement,datecharge__date__lte=datefin, datecharge__date__gte=datedebut)
    interventions=Intervention.objects.filter(planification__site=site,planification__equipement=equipement,datecharge__date__lte=datefin, datecharge__date__gte=datedebut)
    
    context={'site':site,'interventions':interventions,'taches':taches,'equipement':equipement,
    'this_month': month, 'm': m, 'tm': tm, 'pm': pm, 'nm': nm, 'prev_month': prev_month(m), 'next_month': next_month(m)}

    return render(request,'dashboard/administration/equipementintervention.html',context)


def fetch_resources(uri, rel):
    path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))

    return path
    
def render_to_pdf(template_src, context_dict={},):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result,link_callback=fetch_resources)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


#Opens up page as PDF
class QrPDF(View):
    def get(self,request,pk1,pk2, *args, **kwargs):
        site=Site.objects.get(id=self.kwargs.get('pk1'))
        equipement=Equipement.objects.get(id=self.kwargs.get('pk2'))
        url=f'https://myhpms.herokuapp.com/sites/{site.id}/equipementintervention/{equipement.id}'
        data={'site':site,'equipement':equipement,'url':url}
        pdf = render_to_pdf('dashboard/administration/qr_template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

def getqr(request,pk):    
    site=Site.objects.get(id=pk)
    if request.method=="POST":
        form=QrForm(site,request.POST)
        if form.is_valid():
            equipement=form.instance.equipement
            return redirect('QrPDF',pk1=site.id,pk2=equipement.id)
    else:
        form=QrForm(site)

    return render(request,'dashboard/administration/getqr.html',{'form':form,'site':site})

#Rondes QR

class RondeQrPDF(View):
    def get(self,request,pk1,pk2, *args, **kwargs):
        site=Site.objects.get(id=self.kwargs.get('pk1'))
        equipement=Equipement.objects.get(id=self.kwargs.get('pk2'))
        url=f'https://myhpms.herokuapp.com/sites/{site.id}/ronde/{equipement.id}/ajouter'
        data={'site':site,'equipement':equipement,'url':url}
        pdf = render_to_pdf('dashboard/administration/rondeqr_template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

def getrondeqr(request,pk):    
    site=Site.objects.get(id=pk)
    if request.method=="POST":
        form=RondeQrForm(site,request.POST)
        if form.is_valid():
            equipement=form.instance.equipement
            return redirect('RondeQrPDF',pk1=site.id,pk2=equipement.id)
    else:
        form=RondeQrForm(site)

    return render(request,'dashboard/administration/getrondeqr.html',{'form':form,'site':site})


### Collaborateurs

def collabs(request):
    intervenants=User.objects.filter(is_collab=True)
    responsables=User.objects.filter(is_responsable=True)
    clients=User.objects.filter(is_client=True)

    context={'intervenants':intervenants,'responsables':responsables,'clients':clients}

    return render(request,'dashboard/administration/collabdetail.html',context)

def newcollab(request):

    if request.method=="POST":
        nom=request.POST.get('first_name')
        prenom=request.POST.get('last_name')
        form=CollabForm(request.POST)
        if form.is_valid():
            form.instance.username=nom+'.'+prenom
            form.save()
            messages.success(request, f'Nouveau Collaborateur cr???? avec succ??s')
            return redirect('collabs')
    else:
        form=CollabForm()

    return render(request,'dashboard/administration/collabnew.html',{'form':form})

def updatecollab(request,pk):
    user=User.objects.get(id=pk)

    if request.method=="POST":
        form=UpdatecollabForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Collaborateur modifi?? avec succ??s')
            return redirect('collabs')
        else:
            print(form.errors)
    else:
        form=UpdatecollabForm(instance=user)

    return render(request,'dashboard/administration/collabupdate.html',{'form':form})

def deletecollab(request,pk):
    user=User.objects.get(id=pk)

    if request.method=="POST":
        user.delete()
        messages.success(request, f'Collaborateur supprim?? avec succ??s')
        return redirect('collabs')
    

    return render(request,'dashboard/administration/collabdelete.html',{'user':user})

## Sites

### Home

def sitehome(request,pk):
    site=Site.objects.get(id=pk)
    context={'site':site}
    return render(request,'dashboard/maintenance/sitehome.html',context)

## Rondes 
def ronde(request,pk):
    site=Site.objects.get(id=pk)
    d = get_date(request.GET.get('day', None))
    day = d.strftime("%Y-%m-%d")

    td = d.strftime("%d/%m/%Y")

    rondes=Ronde.objects.filter(site=site,datecreated__date=day).order_by('-id')    
    filter=RondeFliter(site.id,request.GET,request=request,queryset=rondes)
    frondes=filter.qs
    context={'site':site,'rondes':frondes,'td':td,'prev_day':prev_day(d),'next_day':next_day(d),'filter':filter}

    return render(request,'dashboard/ronde/ronde.html',context)

def newronde(request,pk1,pk2):
    site=Site.objects.get(id=pk1)
    equipement=Equipement.objects.get(id=pk2)

    if request.method=="POST":
        Ronde.objects.create(site=site,equipement=equipement,intervenant=User.objects.get(username='admin'))
        messages.success(request, f'Ronde ajout??e avec succ??s')
        return redirect('ronde',pk=site.id)    
    
    context={'site':site,'equipement':equipement}

    return render(request,'dashboard/ronde/rondenew.html',context)

### Maintenance Curative

def curative(request,pk):
    site=Site.objects.get(id=pk)
    taches=Tache.objects.filter(site=site).order_by('-id')
    filter=CurativeFliter(site.id,request.GET,request=request,queryset=taches)
    ftaches=filter.qs
    context={'site':site,'taches':ftaches,'filter':filter}
    return render(request,'dashboard/maintenance/curative.html',context)

def curativedetail(request,pk):
    tache=Tache.objects.get(id=pk)
    site=tache.site
    context={'tache':tache,'site':site}
    return render(request,'dashboard/maintenance/curativedetail.html',context)

def newcurative(request,pk):
    site=Site.objects.get(id=pk)
    if request.method=="POST":
        form=CurativeForm(site,request.POST,request.FILES)
        if form.is_valid():
            form.instance.site=site
            form.instance.auteur=User.objects.get(username='admin')
            form.save()
            messages.success(request, f'Nouvelle Intervention Curative ajout??e avec succ??s')
            return redirect('curative',pk=site.id)
    else:
        form=CurativeForm(site)

    context={'site':site,'form':form}
    return render(request,'dashboard/maintenance/curativenew.html',context)

def updatecurative(request,pk):
    tache=Tache.objects.get(id=pk)
    site=tache.site
    if request.method=="POST":
        form=UpdateCurativeForm(site,request.POST,request.FILES,instance=tache)
        if form.is_valid():
            form.save()
            messages.success(request, f'Intervention modifi??e avec succ??s')
            return redirect('curativedetail',pk=tache.id)
    else:
        form=UpdateCurativeForm(site,instance=tache)

    context={'site':site,'form':form}
    return render(request,'dashboard/maintenance/curativeupdate.html',context)

def deletecurative(request,pk):
    tache=Tache.objects.get(id=pk)
    site=tache.site

    if request.method=="POST":
        tache.delete()
        messages.success(request, f'Intervention supprim??e avec succ??s')
        return redirect('curative',pk=site.id)    
    
    context={'site':site,'tache':tache}

    return render(request,'dashboard/maintenance/curativedelete.html',context)

def fichecurative(request,pk):
    tache=Tache.objects.get(id=pk)
    site=tache.site
    if request.method=="POST":
        form=FicheForm(request.POST,instance=tache)
        if form.is_valid():
            form.save()
            messages.success(request, f'Fiche Intervention modifi??e avec succ??s')
            return redirect('curativedetail',pk=tache.id)
    else:
        form=FicheForm(instance=tache)

    context={'site':site,'form':form}
    return render(request,'dashboard/maintenance/fichecurative.html',context)



### Maintenance Pr??ventive

def preventive(request,pk):
    site=Site.objects.get(id=pk)
    interventions=Intervention.objects.filter(planification__site=site)
    m = get_date(request.GET.get('month', None))
    month = m.strftime("%Y-%m-%d")
    mday='day='+ str(month)
    tm = m.strftime("%m/%y")
    strm=calendar.month_name[int(m.strftime("%m"))]
    pm = (m - relativedelta(months=1)).strftime("%m/%y")
    nm = (m + relativedelta(months=1)).strftime("%m/%y")
    context={'site':site,'interventions':interventions,'site_id':site.id,'mday':mday,'strm':strm,
    'this_month': month, 'm': m, 'tm': tm, 'pm': pm, 'nm': nm, 'prev_month': prev_month(m), 'next_month': next_month(m)}

    return render(request,'dashboard/maintenance/preventive.html',context)

def newpreventive(request,pk):
    site=Site.objects.get(id=pk)
    if request.method=="POST":
        form=PreventiveForm(site,request.POST)
        if form.is_valid():
            if form.instance.periodicite == 'Hebdomadaire':
                delta=7
            elif form.instance.periodicite == 'Mensuelle':
                delta=30
            elif form.instance.periodicite == 'Trimestrielle':
                delta=90    
            elif form.instance.periodicite == 'Semestrielle':
                delta=180  
            elif form.instance.periodicite == 'Semestrielle':
                delta=365  
            form.instance.site=site
            tachedate=form.instance.datedebut
            p=form.save()
           
            while tachedate <= form.instance.datefin :
                Intervention.objects.create(planification=p,datecharge=tachedate)
                tachedate += timedelta(days=delta)

            messages.success(request, f'Nouvelle Planification ajout??e avec succ??s')
            return redirect('preventive',pk=site.id)
    else:
        form=PreventiveForm(site)

    context={'site':site,'form':form}
    return render(request,'dashboard/maintenance/preventivenew.html',context)

def preventiveupdate(request,pk1,pk2):
    planification=Planification.objects.get(id=pk2)
    site=planification.site
    if request.method=="POST":
        form=UpdatePreventiveForm(site,request.POST,instance=planification)
        if form.is_valid():
            form.save()
            messages.success(request, f'Planification modifi??e avec succ??s')
            return redirect('preventive',pk=site.id)
        else:
            print(form.errors)
    else:
        form=UpdatePreventiveForm(site,instance=planification)

    context={'site':site,'form':form,'planification':planification}
    return render(request,'dashboard/maintenance/preventiveupdate.html',context)

def deletepreventive(request,pk):
    planification=Planification.objects.get(id=pk)
    site=planification.site

    if request.method=="POST":
        planification.delete()
        messages.success(request, f'Planification supprim??e avec succ??s')
        return redirect('preventive',pk=site.id)    
    
    context={'site':site,'planification':planification}

    return render(request,'dashboard/maintenance/planificationdelete.html',context)

def intervention(request,pk1,pk2):
    intervention=Intervention.objects.get(id=pk2)
    planificatin=intervention.planification
    site=intervention.planification.site
    context={'intervention':intervention,'planificatin':planificatin,'site':site}

    return render(request,'dashboard/maintenance/intervention.html',context)

def updateintervention(request,pk):
    intervention=Intervention.objects.get(id=pk)
    site=intervention.planification.site
    if request.method=="POST":
        form=PreventiveFicheForm(site,request.POST,request.FILES,instance=intervention)
        if form.is_valid():
            form.save()
            messages.success(request, f'Intervention modifi??e avec succ??s')
            return redirect('intervention',pk1=site.id,pk2=intervention.id)
    else:
        form=PreventiveFicheForm(site,instance=intervention)
    
    context={'site':site,'intervention':intervention,'form':form}
    return render(request,'dashboard/maintenance/interventionupdate.html',context)
    


def get_date(req_month):
    if req_month:
        year, month, day = (int(x) for x in req_month.split('-'))
        return date(year, month, day)
    return datetime.today().date()


def prev_month(m):
    prev_month = m - relativedelta(months=1)
    month = 'month=' + str(prev_month.year) + '-' + \
        str(prev_month.month) + '-' + str(prev_month.day)
    return month


def next_month(m):

    next_month = m + relativedelta(months=1)
    month = 'month=' + str(next_month.year) + '-' + \
        str(next_month.month) + '-' + str(next_month.day)
    return month

def prev_day(d):  

    prev_day= d - timedelta(days=1)
    day='day=' + str(prev_day.year) + '-' + str(prev_day.month)+ '-' + str(prev_day.day)
    return day

def next_day(d):

    next_day = d + timedelta(days=1)
    day='day=' + str(next_day.year) + '-' + str(next_day.month)+ '-' + str(next_day.day)
    return day


### Gestion Stock

def stock(request,pk):
    site=Site.objects.get(id=pk)
    stocks=Stock.objects.filter(site=site)
    context={'site':site,'stocks':stocks}

    return render(request,'dashboard/stock/stock.html',context)

def newstock(request,pk):
    site=Site.objects.get(id=pk)
    if request.method=="POST":
        form=StockForm(site,request.POST)
        if form.is_valid():
            form.instance.site=site
            form.save()
            messages.success(request, f'Nouveau stock ajout?? avec succ??s')
            return redirect('stock',pk=site.id)
    else:
        form=StockForm(site)

    context={'site':site,'form':form}
    return render(request,'dashboard/stock/stocknew.html',context)

def updatestock(request,pk):
    stock=Stock.objects.get(id=pk)
    site=stock.site
    if request.method=="POST":
        form=StockForm(site,request.POST,instance=stock)
        if form.is_valid():
            form.save()
            messages.success(request, f'Stock Modifi?? avec succ??s')
            return redirect('stock',pk=site.id)
    else:
        form=StockForm(site,instance=stock)

    context={'site':site,'stock':stock,'form':form}
    return render(request,'dashboard/stock/stockupdate.html',context)


def deletestock(request,pk):
    stock=Stock.objects.get(id=pk)
    site=stock.site

    if request.method=="POST":
        stock.delete()
        messages.success(request, f'Stock supprim?? avec succ??s')
        return redirect('stock',pk=site.id)    
    
    context={'site':site,'stock':stock}

    return render(request,'dashboard/stock/stockdelete.html',context)



def stockdetail(request,pk):
    stock=Stock.objects.get(id=pk)
    site=stock.site
    mouvements=Mouvement.objects.filter(stock=stock)
    context={'site':site,'stock':stock,'mouvements':mouvements}

    return render(request,'dashboard/stock/stockdetail.html',context)

def newmvmnt(request,pk):
    stock=Stock.objects.get(id=pk)
    site=stock.site
    if request.method=="POST":
        form=MouvementForm(request.POST)
        if form.is_valid():
            form.instance.stock=stock
            
            if form.instance.mouvement == 1 :
                stock.stock=stock.stock+int(form.instance.quantite)
                stock.save()
            else:
                q=stock.stock-int(form.instance.quantite)
                if q < 0 :
                    form.instance.quantite=stock.stock
                    stock.stock = 0
                    stock.save()
                else:
                    stock.stock=q
                    stock.save()

            form.save()
            messages.success(request, f'Nouveau Mouvement ajout?? avec succ??s')
            return redirect('stockdetail',pk=stock.id)

    else:
        form=MouvementForm()
    context={'site':site,'form':form}
    return render(request,'dashboard/stock/mouvementnew.html',context)

def deletemvmnt(request,pk):
    mouvement=Mouvement.objects.get(id=pk)
    stock=mouvement.stock
    site=stock.site

    if request.method=="POST":
        mouvement.delete()
        messages.success(request, f'Mouvement supprim?? avec succ??s')
        return redirect('stockdetail',pk=stock.id)    
    
    context={'site':site,'stock':stock,'mouvement':mouvement}
    return render(request,'dashboard/stock/mouvementdelete.html',context)