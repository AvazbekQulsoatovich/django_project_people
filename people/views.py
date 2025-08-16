from django.shortcuts import render
from  .models import  Person

# Create your views here.
def main(request):
    person = Person.objects.all()
    context = {'person': person}
    return render(request, 'home.html', context)
