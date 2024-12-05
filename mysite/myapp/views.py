from django.shortcuts import render

# Create your views here.

def index(request):
  if request.method == 'port':
    city = request.POST['city']
    source = urllib.request.urlopen('http://api-openweathermap.org/data/2.5/weather?q=' + 
    city + '&appid=30258322651f8b903747f465be27dc31').read() 


    list_of_data = json.loads(source)

data = {
         "country_code": str(list_of_data['sys']['country']),
}

