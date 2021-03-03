from django.shortcuts import render, get_object_or_404
from .forms import SignUp
from .models import Item, Order, Category, Customer
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def item_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()

    items = Item.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        items = items.filter(category=category)

    return render(request,
                  'items/list.html',
                  {'category': category,
                   'categories': categories,
                   'items': items})

# Create your views here.
def home(request):
    num_orders = Order.objects.all()
    context = {
        'num_orders': num_orders
    }
    # Render the html template home.html with the data in the context variable
    return render(request, 'home.html', context=context)


def signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            login(request, user)
            return redirect('chinesseRestaurant:home')
    else:
        form = SignUp()
    return render(request, 'registration/signup.html', {'form': form})

def order_now(request):
    return render(request, 'order_now.html')

def covidWarning(request):
    return render(request, 'covidPrec.html')


