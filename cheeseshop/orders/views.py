from django.shortcuts import render
from django.views import generic

# Create your views here.

from .models import Item

class IndexView(generic.ListView):
    template_name = 'orders/index.html'
    context_object_name = 'item_list'
    
    def get_queryset(self):
        """Return the last five cheeses."""
        #Don't even have 5 items yet
        return Item.objects.order_by('name')[:5]

#class DetailView(generic.DetailView):
#    model = Question
#    template_name = 'polls/detail.html'