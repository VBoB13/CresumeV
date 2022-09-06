from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(request):
    menu_items = [
        {"name": "Education", "link": "/education"},
        {"name": "Experiences", "link": "/experiences"},
        {"name": "Who am I?", "link": "/whoami"},
        {"name": "Contact me", "link": "/contact"}
    ]
    page_title = "Richard's Resume"
    template = loader.get_template('ric/index.html')
    context = {
        "page_title": page_title,
        "menu_items": menu_items
    }
    return HttpResponse(template.render(context, request))


def education(request):
    return HttpResponse("You're currently checking out Ric's education!")


def experiences(request):
    return HttpResponse("You're currently checking out Ric's experiences!")


def contact_me(request):
    return HttpResponse("Contact me, why dontcha?")
