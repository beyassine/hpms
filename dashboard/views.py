from django.shortcuts import render,redirect
from .forms import *
from .filters import *
from django.contrib import messages
from users.models import *
from users.forms import *
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'dashboard/home.html')

# Templates
def form(request):
    return render(request,'dashboard/form.html')

def listintervention(request):
    return render(request,'dashboard/list.html')

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
            messages.success(request, f'Site modifié avec succés')
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
            messages.success(request, f'Site modifié avec succés')
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
            messages.success(request, f'Site modifié avec succés')
            return redirect('detailsite',pk=site.id)
    else:
        form=ClientsiteForm(instance=site)

    return render(request,'dashboard/administration/siteaddclient.html',{'form':form})

def newsite(request):
    if request.method=="POST":
        form=SiteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Nouveau Site créé avec succés')
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
            messages.success(request, f'Site modifié avec succés')
            return redirect('sites')
    else:
        form=SiteForm(instance=site)

    return render(request,'dashboard/administration/siteupdate.html',{'form':form})

def deletesite(request,pk):
    site=Site.objects.get(id=pk)
    if request.method=="POST":
        site.delete()
        messages.success(request, f'Site supprimé avec succés')
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
            messages.success(request, f'Nouvelle zone créé avec succés')
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
            messages.success(request, f'Zone modifiée avec succés')
            return redirect('detailsite',pk=site.id)
    else:
        form=ZoneForm(instance=zone)

    return render(request,'dashboard/administration/zoneupdate.html',{'form':form})


def deletezone(request,pk):
    zone=Zone.objects.get(id=pk)
    site=zone.site
    if request.method=="POST":
        zone.delete()
        messages.success(request, f'Zone supprimée avec succés')
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
            messages.success(request, f'Nouveau Lot créé avec succés')
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
            messages.success(request, f'Lot Equipement modifié avec succés')
            return redirect('lotequipements')
    else:
        form=SiteForm(instance=lot)

    return render(request,'dashboard/administration/lotupdate.html',{'form':form})

def deletelot(request,pk):
    lot = Lot.objects.get(id=pk)

    if request.method=="POST":
        lot.delete()
        messages.success(request, f'Lot Equipement supprimé avec succés')
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
            messages.success(request, f'Nouveau sous-lot créé avec succés')
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
            messages.success(request, f'Sous-Lot modifié avec succés')
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
        messages.success(request, f'Sous-Lot supprimé avec succés')
        return redirect('detaillotequipement',pk=lot.id)
    

    return render(request,'dashboard/administration/souslotdelete.html',{'slot':slot})

#### Catégories

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
            messages.success(request, f'Nouvelle Catégorie créée avec succés')
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
            messages.success(request, f'Catégorie modifiée avec succés')
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
        messages.success(request, f'Catégorie supprimé avec succés')
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
            messages.success(request, f'Nouveau Equipement créé avec succés')
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
            messages.success(request, f'Equipement modifié avec succés')
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
        messages.success(request, f'Equipement supprimé avec succés')
        return redirect('detailcategorie',pk=cat.id)
    

    return render(request,'dashboard/administration/equipementdelete.html',{'equipement':equipement})

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
            messages.success(request, f'Nouveau Collaborateur créé avec succés')
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
            messages.success(request, f'Collaborateur modifié avec succés')
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
        messages.success(request, f'Collaborateur supprimé avec succés')
        return redirect('collabs')
    

    return render(request,'dashboard/administration/collabdelete.html',{'user':user})

## Sites

### Home

def sitehome(request,pk):
    site=Site.objects.get(id=pk)
    context={'site':site}
    return render(request,'dashboard/maintenance/sitehome.html',context)


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
            messages.success(request, f'Nouvelle Intervention Curative ajoutée avec succés')
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
            messages.success(request, f'Intervention modifiée avec succés')
            return redirect('curativedetail',pk=tache.id)
        else:
            print(form.errors)
    else:
        form=UpdateCurativeForm(site,instance=tache)

    context={'site':site,'form':form}
    return render(request,'dashboard/maintenance/curativeupdate.html',context)

def deletecurative(request,pk):
    tache=Tache.objects.get(id=pk)
    site=tache.site

    if request.method=="POST":
        tache.delete()
        messages.success(request, f'Intervention supprimée avec succés')
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
            messages.success(request, f'Fiche Intervention modifiée avec succés')
            return redirect('curativedetail',pk=tache.id)
    else:
        form=FicheForm(instance=tache)

    context={'site':site,'form':form}
    return render(request,'dashboard/maintenance/fichecurative.html',context)



### Maintenance Préventive

def preventive(request,pk):
    site=Site.objects.get(id=pk)
    taches=Tache.objects.filter(site=site)

    context={'site':site,'taches':taches}

    return render(request,'dashboard/maintenance/preventive.html',context)


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
            messages.success(request, f'Nouveau stock ajouté avec succés')
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
            messages.success(request, f'Stock Modifié avec succés')
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
        messages.success(request, f'Stock supprimé avec succés')
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
            messages.success(request, f'Nouveau Mouvement ajouté avec succés')
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
        messages.success(request, f'Mouvement supprimé avec succés')
        return redirect('stockdetail',pk=stock.id)    
    
    context={'site':site,'stock':stock,'mouvement':mouvement}
    return render(request,'dashboard/stock/mouvementdelete.html',context)