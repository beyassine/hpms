from dashboard.models import *



def base(request):
    	
    sites=Site.objects.all()
	
    return {'sites':sites}
