from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Item, Order, Category


class ItemListView(ListView):
    model = Item
    queryset = Item.objects.get_queryset().order_by('name')
    context_object_name = 'foods'
    paginate_by = 3
    template_name = 'items/list.html'


def item_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    items = Item.objects.fitler(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        items = items.filter(category=category)

    return render(request,
                  'items/list.html',
                  {'category' : category,
                   'categories' : categories,
                   'items' : items})


# Create your views here.
def home(request):
    num_orders = Order.objects.all()
    context = {
        'num_orders': num_orders
    }
    # Render the html template home.html with the data in the context variable
    return render(request, 'home.html', context=context)
