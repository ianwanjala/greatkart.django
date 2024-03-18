# this is a python function 'python processor'
#takes request as argument and 
#returns the dictionary of data as a context

from .models import Category
#function menu links

def menu_links(request):
    #fetch all category from database
    links=Category.objects.all()
    #fetches category and stors in links category to use when we want
    return dict(links=links)