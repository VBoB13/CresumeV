from django.http import HttpResponse
from django.template import loader

from .models import Education

# Create your views here.


def index(request):
    menu_items = [
        {
            "name": "Education",
            "link": "/education",
            "icon": "ric/icons/icon_education.svg"
        },
        {
            "name": "Experiences",
            "link": "/experiences",
            "icon": "ric/icons/icon_experiences.svg"
        },
        {
            "name": "Who am I?",
            "link": "/whoami",
            "icon": "ric/icons/icon_whoami.svg"
        },
        {
            "name": "Contact me",
            "link": "/contact",
            "icon": "ric/icons/icon_contact.svg"
        }
    ]
    page_title = "Richard's Resume"
    template = loader.get_template('ric/index.html')
    context = {
        "page_title": page_title,
        "menu_items": menu_items
    }
    return HttpResponse(template.render(context, request))


def education(request):
    ed_items = Education.objects.all()
    page_title = "Richard's Education"
    template = loader.get_template('ric/education.html')
    context = {
        "page_title": page_title,
        "ed_items": ed_items,
        "list_icon": "ric/icons/icon_education.svg"
    }
    return HttpResponse(template.render(context, request))


def experiences(request):
    return HttpResponse("You're currently checking out Ric's experiences!")


def contact_me(request):
    return HttpResponse("Contact me, why dontcha?")
