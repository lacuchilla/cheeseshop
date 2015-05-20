from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect

# Create your views here.

from .models import Item
from .orderform import ContactForm

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

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})


