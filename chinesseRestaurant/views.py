from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import ListView

from .models import Item


# Create your views here.
class ItemListView(ListView):
    queryset = Item.objects.all()
    context_object_name = 'foods'
    paginate_by = 3
    template_name = 'items/list.html'


def item_list(request):
    object_list = Item.objects.all()
    paginator = Paginator(object_list, 3)  # 3 foods per page
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
