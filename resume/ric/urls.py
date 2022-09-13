from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('education/', views.education, name='education'),
    path(
        'education/<int:education_id>/',
        views.education_detail, name='education_detail'
    ),
    path('experience/', views.experiences, name='experiences'),
    path(
        'experience/<int:experience_id>/',
        views.experiences_detail, name='experience_detail'
    ),
    path('whoami/', views.aboutme, name='whoami'),
    path('contact/', views.contact_me, name='contact')
]
