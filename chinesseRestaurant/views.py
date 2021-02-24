from django.shortcuts import render
from django.views.generic import ListView

from .models import Item
from django.core.paginator import Paginator, EmptyPage, \
    PageNotAnInteger


class ItemListView(ListView):
    queryset = Item.objects.get_queryset().order_by('name')
    context_object_name = 'foods'
    paginate_by = 2
    template_name = 'items/list.html'


def item_list(request):
    object_list = Item.objects.get_queryset().order_by('name')
    paginator = Paginator(object_list, 2)  # 2 foods per page
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
    num_items = Item.objects.all().count()
    context = {
        'num_items': num_items
    }
    # Render the html template home.html with the data in the context variable
    return render(request, 'home.html', context=context)
