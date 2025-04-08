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
    if request.method == "POST":
        my_competitor = Competitor.objects.filter(pk=request.POST["pk"])
        my_competitor.delete()
    obj = Competitor.objects.all()
    context = {
        "objects": obj
    }
    return render(request, "viewcompetitors.html", context)

def competition_view(request):
    if request.method == "POST":
        r = request.POST
        c_up = Competitor.objects.get(name=request.POST["competitor-name"])
        miss_make = r["miss-make"] == "Make"
        if r["lift"] == "Snatch":
            if int(r["attempt-no"]) == 1:
                c_up.snatch_attempt_1 = r["weight"]
                c_up.snatch_attempt_1_make = miss_make
                c_up.save()
            elif int(r["attempt-no"]) == 2:
                c_up.snatch_attempt_2 = r["weight"]
                c_up.snatch_attempt_2_make = miss_make
                c_up.save()
            else:
                c_up.snatch_attempt_3 = r["weight"]
                c_up.snatch_attempt_3_make = miss_make
                c_up.save()

        else:
            if int(r["attempt-no"]) == 1:
                c_up.cnj_attempt_1 = r["weight"]
                c_up.cnj_attempt_1_make = miss_make
                c_up.save()
            elif int(r["attempt-no"]) == 2:
                c_up.cnj_attempt_2 = r["weight"]
                c_up.cnj_attempt_2_make = miss_make
                c_up.save()
            else:
                c_up.cnj_attempt_3 = r["weight"]
                c_up.cnj_attempt_3_make = miss_make
                c_up.save()

    obj = Competitor.objects.all()

    ordered_obj = []
    for i in range(len(obj)):
        if obj[i].sinclair != None:
            ordered_obj.append(obj[i])
    ordered_obj.sort(key=lambda x: x.sinclair, reverse=True)

    for i in range(len(ordered_obj)):
        ordered_obj[i].position = i+1
        ordered_obj[i].save()

    context = {
        "objects": obj
    }
    return render(request, "competition.html", context)
