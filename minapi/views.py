from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Stores
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
import requests
from rest_framework.decorators import api_view


def minseller(request):
    # FINDING OUT THE INGREDIENTS TO MAKE A SPECIFIC RECIPE

    recipe_name=request.POST["name1"]
    ingredients=Recipe.objects.filter(name=recipe_name).values('ingredients')

    if len(ingredients)==0:
        return render(request,'index.html',{'flag1':2})
    k=ingredients[0]['ingredients']

    ingredients1=k.split(',')
    # WRITING CUSTOM QUERY TO FIND THE SUM OF INGREDIENTS AFTER DISCOUNT
    # WHICH ARE STORED IN COLUMNS NAMED AS after_discount_ingredientName

    custom_query='SELECT id,('
    for i in range(len(ingredients1)):
        ingredients1[i]='after_discount_'+ingredients1[i]
        if i<len(ingredients1)-1:
            custom_query=custom_query+ingredients1[i]+'+'
        else:
            custom_query=custom_query+ingredients1[i]
    custom_query=custom_query+') as SUM FROM minapi_Stores order by SUM Limit 2'

    obj=Stores.objects.raw(custom_query)
    serializers=StoresSerializer(obj,many=True) #API VIEW CONSISTING OF ALL THE DATA

    count=0
    ingredients1.append('name')
    ingredients1.append('id')

    # CLEANING THE API DATA AND RETAINING ONLY REQUIRED VALUES OF INGREDIENTS
    for i in serializers.data:
        for j in list(i.keys()):
            if j not in ingredients1:
                del i[j]
        i["price"]=obj[count].SUM
        count+=1
    data1=serializers.data
    return render(request,'index.html',{'data1':data1,'flag1':1,'ingredients1':ingredients1})
    
    

class Recipe1(APIView):
    def get(self,request):
        obj=Recipe.objects.all()
        serializers=RecipeSerializer(obj,many=True)
        return Response(serializers.data)

# INITIALLY DISPLAYS ALL THE RECIPES AVAILABLE FROM THE API
def home(request):
    data=requests.request('GET','http://127.0.0.1:8000/recipe/')
    data=data.json()
    return render(request,'index.html',{'data':data,'flag1':0})

'''
def minseller(request):
    v=request.POST["name"]
    url='http://127.0.0.1:8000/min?name='+v+'/'
    data=requests.request('GET',url)
    return render(request,'index.html',{'data':data,'flag1':3})
'''