from django.http import HttpResponse
from django.template import loader

from .models import Education, Experience

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


def education_detail(request, education_id):
    ed_item = Education.objects.get(pk=education_id)
    page_title = "Richard's Education"
    template = loader.get_template('ric/education_detail.html')
    context = {
        "ed_item": ed_item,
        "page_title": page_title,
        "list_icon": "ric/icons/icon_education.svg"
    }
    return HttpResponse(template.render(context, request))


def experiences(request):
    exp_items = Experience.objects.all()
    page_title = "Richard's Experiences"
    template = loader.get_template('ric/experiences.html')
    context = {
        "exp_items": exp_items,
        "page_title": page_title,
        "list_icon": "ric/icons/icon_experiences.svg"
    }
    return HttpResponse(template.render(context, request))


def experiences_detail(request, experience_id):
    exp_item = Experience.objects.get(pk=experience_id)
    page_title = "Richard's Experiences"
    template = loader.get_template('ric/experiences_detail.html')
    context = {
        "exp_item": exp_item,
        "page_title": page_title,
        "list_icon": "ric/icons/icon_experiences.svg"
    }
    return HttpResponse(template.render(context, request))


def aboutme(request):
    page_title = "Who am I?"
    template = loader.get_template('ric/aboutme.html')
    context = {
        "page_title": page_title
    }
    return HttpResponse(template.render(context, request))


def contact_me(request):
    return HttpResponse("Contact me, why dontcha?")
