from django.shortcuts import render
from .models import Competitor
from .forms import CompetitorForm

# Create your views here.

def home_view(request):
    return render(request, "home.html")

def add_competitor_view(request, *args, **kwargs):
    form = CompetitorForm()
    if request.method == "POST":
        form = CompetitorForm(request.POST)
        if form.is_valid():
            Competitor.objects.create(**form.cleaned_data)
    context = {
        "form": form
    }
    return render(request, "addcompetitors.html", context)

def view_competitors_view(request, *args, **kwargs):
    obj = Competitor.objects.all()
    context = {
        "objects": obj
    }
    return render(request, "viewcompetitors.html", context)

def competition_view(request):
    if request.method == "POST":
        print(request.body)
    obj = Competitor.objects.all()
    context = {
        "objects": obj
    }
    return render(request, "competition.html", context)
