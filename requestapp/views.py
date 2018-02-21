from django.shortcuts import render

# Create your views here.
from requestapp.collection.browser import check_browser_type
from requestapp.models import Browsers


def index(request):
    args = request.META['HTTP_USER_AGENT']
    args += '<script>alert("Hi!")</script>'

    check_browser_type(args)

    args2 = request.META
    args3 = Browsers.get_all_objects()

    return render(request, 'index.html', {'headerinfo' : args, 'allheader' : args2, 'allobjects' : args3})