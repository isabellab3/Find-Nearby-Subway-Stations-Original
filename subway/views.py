from django.shortcuts import render
import requests

def Home(request):
    url = 'https://data.cityofnewyork.us/api/views/kk4q-3rt2/rows.json'
    request = requests.get(url).json()

    subway_data = []

    for x in range(0, len(request['data'])):
        station_info = {
            'name' :      request['data'][x][10],
            'latitude' :  request['data'][x][11][26:43],
            'longitude' : request['data'][x][11][7:25],
            'lines' :     request['data'][x][12],
            'notes' :     request['data'][x][13],
        }
        subway_data.append(station_info)

    context = {'subway_data' : subway_data}

    return render(request, 'home.html', context)
