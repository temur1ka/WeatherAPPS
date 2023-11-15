from django.shortcuts import render, HttpResponse
import requests
import datetime
from django.contrib import messages
# Create your views here.





def home(request):
    
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'kobuleti'


    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=3a79905dec21a532e90fd06f1cdaf534'
    PARAMS = {'units':'metric'}
    API_KEY = 'AIzaSyAgLN2H6SDn4pdG64Z44nAOhrq8W_QwSpw'
    SEARCH_ENGINE = '708c1ace7f8614237'

    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    data = requests.get(city_url).json()
    count = 1
    search_items = data.get("items")
    image_url = search_items[1]['link']
    

    try:
        data = requests.get(url,PARAMS).json()

        humidity = data['main']['humidity']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        wind = data['wind']['speed']
        country = data['sys']['country']

        day = datetime.date.today()

        return render(request, 'app/home.html', {'country':country,'humidity': humidity, 'icon':icon, 'temp':temp, 'day':day, 'city':city, 'wind':wind, 'raise_error':False, 'image_url':image_url})
    except:
        day = datetime.date.today()
        raise_error = True
        messages.warning(request, "Entered City is Not Recognized under WeatherOrg Database")
        return render(request, 'app/home.html', {'country':'GE','humidity': 89, 'icon':'10n', 'temp':25, 'day':day, 'city':'kobuleti', 'wind':8.7, 'raise_error':raise_error})

         

    