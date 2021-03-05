from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from .models import Profile
from .forms import LoginForm
from .forms import SignUp
from .models import Item, Order, Category, Profile


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
            # Create a new user object but avoid saving it yeet
            new_user = form.save(commit=False)
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            new_user.save()
            Profile.objects.create(user=new_user)
            login(request, user)
            Profile.objects.create(user=new_user)
            return redirect('chinesseRestaurant:home')
    else:
        form = SignUp()
    return render(request, 'registration/signup.html', {'form': form})


def order_now(request):
    return render(request, 'registration/order_now.html')


def covidWarning(request):
    return render(request, 'covidPrec.html')


def menu(request):
    return render(request, 'menu.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'home.html')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'Registration/login.html', {'form': form})


from django.contrib.auth.decorators import login_required


@login_required
def customerView(request):
    return render(request, 'base.html')


from .forms import LoginForm, SignUp, \
    UserEditForm, ProfileEditForm


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return render(request, 'base.html')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
            instance=request.user.profile)
    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})
