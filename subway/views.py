from django.shortcuts import render
import requests

def Home(request):
    url = 'https://data.cityofnewyork.us/api/views/kk4q-3rt2/rows.json'
    r = requests.get(url).json()

    subway_data = []

    for x in range(0, len(r['data'])):
        station_info = {
            'name'      :  r['data'][x][10],
            'latitude'  :  r['data'][x][11][26:43],
            'longitude' :  r['data'][x][11][7:25],
            'lines'     :  r['data'][x][12],
            'notes'     :  r['data'][x][13],
        }
        subway_data.append(station_info)

    context = {'subway_data' : subway_data}

    return render(request, 'home.html', context)
