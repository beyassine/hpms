from rest_framework import serializers
from .models import *
import calendar
from datetime import datetime, date, timedelta

class InterventionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Intervention
        fields = '__all__'
        

class PlanificationSerializer(serializers.ModelSerializer):

    interventions=serializers.SerializerMethodField()

    class Meta:
        model = Planification
        fields = ('id','objet','periodicite','interventions')

    def get_interventions(self,obj):
        dd = self.context['dd']
        df= self.context['df']
        interventions=Intervention.objects.filter(planification=obj.id,datecharge__date__lte=df, datecharge__date__gte=dd)
        ints=InterventionSerializer(interventions,many=True)
        return ints.data

class PlanificationSiteSerializer(serializers.ModelSerializer):
    planifications=serializers.SerializerMethodField()

    class Meta:
        model = Site
        fields = ('id','designation','planifications')

    def get_planifications(self,obj):
        d = self.context['day']
        date_obj = datetime.strptime(d, '%Y-%m-%d')
        datefin = str(date_obj.year) + '-' + str(date_obj.month) + '-' + \
            str(calendar.monthrange(date_obj.year, date_obj.month)[1])
        datedebut = str(date_obj.year) + '-' + str(date_obj.month) + '-' + '01'
        ctx={'dd':datedebut,'df':datefin}
        planifications=Planification.objects.filter(site=obj.id)
        pls=PlanificationSerializer(planifications,many=True,context=ctx)
        return pls.data
