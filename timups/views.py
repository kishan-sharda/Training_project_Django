from timups.models import  banners, watches
from django.shortcuts import render

# Create your views here.
def index(request):

    watchs = watches.objects.all()
    ban = banners.objects.all()
      
    return render(request, 'index.html', {'watchs': watchs, 'ban': ban})