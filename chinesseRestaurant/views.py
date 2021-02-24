from django.shortcuts import render
from django.views.generic import ListView

from .models import Item, Order
from django.core.paginator import Paginator, EmptyPage, \
    PageNotAnInteger


class ItemListView(ListView):
    model = Item
    queryset = Item.objects.get_queryset().order_by('name')
    context_object_name = 'foods'
    paginate_by = 3
    template_name = 'items/list.html'


def item_list(request):
    object_list = Item.objects.get_queryset().order_by('name')
    paginator = Paginator(object_list, 3)  # 2 foods per page
    page = request.GET.get('page')
    try:
        foods = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        foods = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        foods = paginator.page(paginator.num_pages)

    return render(request,
                  'items/list.html',
                  {'page': page,
                   'foods': foods})


# Create your views here.
def home(request):
    num_orders = Order.objects.all()
    context = {
        'num_orders': num_orders
    }
    # Render the html template home.html with the data in the context variable
    return render(request, 'home.html', context=context)
