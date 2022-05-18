# views.py file
from django.http import HttpResponse


def index(request):
    return HttpResponse("<div>Энэ бол миний анхны сайт юм!</div>")

def about(request):
    return HttpResponse("<div> Энэ бол about хуудас</div>")