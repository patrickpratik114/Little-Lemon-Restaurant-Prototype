from django.http import HttpResponse
from django.shortcuts import render
#from .forms import BookingForm
from .models import Menu
from .forms import BookingForm


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Process the form data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            number_of_guests = form.cleaned_data['number_of_guests']
            comments = form.cleaned_data['comments']
            # Handle the reservation logic
    else:
        form = BookingForm()
    return render(request, 'book.html', {'form': form})

# Add your code here to create new views

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu":main_data})

def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 
