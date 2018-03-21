from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from requestapp.collection.browser import check_browser_type
from requestapp.collection.colors import get_matching_color_bg, get_matching_color_text
from requestapp.collection.forms.week3forms import BasicDetailsForm, ColorForm
from requestapp.collection.forms.week4forms import MessageForm
from requestapp.models import Browsers, Colors, Message


def index(request):
    args = request.META['HTTP_USER_AGENT']
    args += '<script>alert("Hi!")</script>'

    check_browser_type(args)

    args2 = request.META
    args3 = Browsers.get_all_objects()

    return render(request, 'index.html', {'headerinfo' : args, 'allheader' : args2, 'allobjects' : args3})

class Week3Basic(View):
    def get(self, request):
        form = BasicDetailsForm()

        return render(request, 'week3.html', {'form' : form})

    def post(self, request):
        if 'details-form' in request.POST:
            form = BasicDetailsForm(request.POST)
            if form.is_valid():
                request.session['name'] = form.cleaned_data['name']
                request.session['address'] = form.cleaned_data['address']
                color_form = ColorForm()
                return render(request, 'week3-2.html', {'colorform': color_form})
            return render(request, 'week3.html', {'form': form})
        elif 'color-form' in request.POST:
            form = ColorForm(request.POST)
            if form.is_valid():
                request.session['color'] = form.cleaned_data['color']
                bgcolor = get_matching_color_bg(form.cleaned_data['color'])
                textcolor = get_matching_color_text(bgcolor)
                name = request.session['name']
                address = request.session['address']
                color = form.cleaned_data['color']
                Colors.save_color_entry(name, address, color)
                entries = Colors.get_ten_random()
                return render(request, 'week3-3.html', {'color': color,
                                                        'name' : name,
                                                        'address' : address,
                                                        'bgcolor' : bgcolor,
                                                        'defaultcolor': textcolor,
                                                        'entries' : entries,
                })
            else:
                return render(request, 'week3-2.html', {'colorform': form})

class Week4(View):
    def get(self, request):
        entries = Message.objects.all().order_by('-id')[:10]

        return render(request, 'week4.html', {'entries' : entries})

class Week4Create(View):
    def get(self, request):
        form = MessageForm()

        return render(request, 'week4C.html', {'form': form})

    def post(self, request):
        form = MessageForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/week4')
        return render(request, 'week4C.html', {'form': form})