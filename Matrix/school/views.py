from django.shortcuts import render

# Create your views here.
class School:
    def __init__(self, key, name, lat, lng):
        self.key  = key
        self.name = name
        self.lat  = lat
        self.lng  = lng

schools = (
    School('hv',      'Happy Valley Elementary',   37.9045286, -122.1445772),
    School('stanley', 'Stanley Middle',            37.8884474, -122.1155922),
    School('wci',     'Walnut Creek Intermediate', 37.9093673, -122.0580063)
)
schools_by_key = {school.key: school for school in schools}

def home(request):

	context = {}

	return render(request, "school/home.html", context)

def registration(request):
	context = {'schools': schools }

	return render(request, "school/registration.html", context)

def maps(request):
    school = schools_by_key.get('hv')
    if school:
        context = {'school': school }
        return render(request, "school/map.html", context)
    else:
        print('error')
