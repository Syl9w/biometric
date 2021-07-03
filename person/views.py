from django.http import JsonResponse, HttpResponseBadRequest

from django.shortcuts import render
from .forms import IINForm

from datetime import datetime
from dateutil.relativedelta import relativedelta
import json
# Create your views here.

def work_with_iin(request):
    if request.method == "POST":
        form = IINForm(request.POST)
        if form.is_valid():
            
            iin = form.cleaned_data['iin']
            if iin.isdecimal():
                birthday = datetime.strptime(iin[:6], '%y%m%d')
                years = relativedelta(datetime.today(), birthday).years
                person = {iin:years}
                with open("people.json", 'r+') as file:
                    data = json.load(file)	# get data from file
                    data.update(person)
                    file.seek(0)
                    json.dump(data, file)
                return JsonResponse({"person":person})
            else:
                return HttpResponseBadRequest("Invalid input", status=400)
            
    else:
        form = IINForm()
        
    return render(request, 'person/iin.html', {'form':form})
    
def find_person(request, iin):
    with open("people.json", "r") as file:
        data = json.load(file)
    if iin in data:
        return JsonResponse({iin:data[iin]})
    else:
        return HttpResponseBadRequest("Person not found", status=400)


