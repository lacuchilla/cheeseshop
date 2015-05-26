from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import FormMixin

# Create your views here.

from .models import Item
from .forms import ContactForm

class IndexView(generic.FormView):
    template_name = 'orders/index.html'
    #context_object_name = 'item_list'
    form_class = ContactForm
	
    def get_context_data(self, **kwargs):
        context = super(generic.FormView, self).get_context_data(**kwargs)
        context['item_list'] = Item.objects.order_by('name')[:5]
        return context

class FormInlineView(generic.FormView):
    template_name = 'orders/form_inline.html'
    form_class = ContactForm