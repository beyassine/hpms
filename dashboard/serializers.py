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
        fields = ('id','objet','periodicite','equipement','zone','interventions')

    def get_interventions(self,obj):
        dd = self.context['dd']
        df= self.context['df']
        interventions=Intervention.objects.filter(planification=obj.id,datecharge__date__lte=df, datecharge__date__gte=dd)
        ints=InterventionSerializer(interventions,many=True)
        return ints.data
    
    def to_representation(self, instance):
        rep = super(PlanificationSerializer, self).to_representation(instance)
        rep['zone'] = instance.zone.designation
        rep['equipement'] = instance.equipement.designation
        return rep

class PlanificationSiteSerializer(serializers.ModelSerializer):
    planifications=serializers.SerializerMethodField()

    class Meta:
        model = Site
        fields = ('id','designation','planifications')

    def get_planifications(self,obj):
        d = self.context['week']
        d=d.strftime("%Y-%m-%d")
        date_obj = datetime.strptime(d, '%Y-%m-%d')        
        calendar_week=date_obj.isocalendar()[1]
        r=f'{date_obj.year}-W{calendar_week} w1'
        r = datetime.strptime(r , "%Y-W%W w%w")
        datefin = str(date_obj.year) + '-' + str(date_obj.month) + '-' + \
            str(calendar.monthrange(date_obj.year, date_obj.month)[1])
        datedebut = str(date_obj.year) + '-' + str(date_obj.month) + '-' + '01'
        ctx={'dd':datedebut,'df':datefin}
        planifications=Planification.objects.filter(site=obj.id)
        pls=PlanificationSerializer(planifications,many=True,context=ctx)
        return pls.data
