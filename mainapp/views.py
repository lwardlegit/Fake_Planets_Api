from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import json
from django.http import JsonResponse
from mainapp.models import Planet


def index(response):
    response = json.dumps({})
    return HttpResponse(response, content_type="text/json")

def planets(response):
    all_planets = list(Planet.objects.all().values())
    print(all_planets)
    return HttpResponse(json.dumps(all_planets), content_type="text/json")
    

def get_planet(request, planet_name):
    if request.method == 'GET':
        try:
            planet = Planet.objects.get(name=planet_name)
            response = json.dumps([
                {'planet': planet.name,
                 'avg temp': planet.temp,
                 'day length in hours': planet.hrs,
                 'mass': planet.mass,
                 'diameter': planet.diameter,
                 'circumference': planet.circumference
                 }
                ])
        except:
            response = json.dumps([{'Error': 'No planet with that name'}])
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def add_planet(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        planet_name = payload['name']
        avg_temp = payload['temp']
        day_hrs = payload['hrs']
        planet_mass = payload['mass']
        planet_diameter = payload['diameter']
        planet_circumference = payload['circumference']
       

        planet = Planet(name=planet_name,temp=avg_temp,hrs=day_hrs,mass=planet_mass, diameter=planet_diameter, circumference=planet_circumference)
        print(planet)
        try:
            planet.save()
            response = json.dumps([{ 'Success': 'Planet added successfully!'}])
        except ValueError as err:
            response = json.dumps([{ 'Error': 'Planet could not be added!'}])
           
    return HttpResponse(response, content_type='text/json')


