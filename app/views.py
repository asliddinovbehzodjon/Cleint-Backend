from django.shortcuts import render
from datetime import datetime,timedelta,date
from rest_framework.response import Response
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import BotUsers
from .serializer import BotUserSerializer
from rest_framework.views import APIView
class BotUserViewset(ModelViewSet):
    queryset = BotUsers.objects.all()
    serializer_class = BotUserSerializer
class TimeInfo(APIView):
    def get(self,request):
        today = date.today()
        nextday = today+ timedelta(days=1)
        oneweek = today - timedelta(days=7)
        oneday = today + timedelta(days=1)
        onemonth = today - timedelta(days=30)
        onedayfilter = BotUsers.objects.filter(created__range=[today,oneday]).count()
        oneweekfilter = BotUsers.objects.filter(created__range=[oneweek,nextday]).count()
        onemonthfilter = BotUsers.objects.filter(created__range=[onemonth,nextday]).count()
        allfilter = BotUsers.objects.all().count()
        return Response(data= {'today':onedayfilter,'lastweek':oneweekfilter,'lastmonth':onemonthfilter,'all':allfilter})