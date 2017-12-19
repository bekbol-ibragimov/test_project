
from django.shortcuts import render
from .forms import SubscriberForm

def landing(request):
    name = "TTname"
    print("asd")
    current_day = "03.01.2017"
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)

    return render(request, 'landing/landing.html', locals())