from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Bb
from django.shortcuts import render


def index(request):
    bbs = Bb.objects.order_by('-published')
    return render(request, 'bboard/index.html', {'bbs':bbs})
# Create your views here.
