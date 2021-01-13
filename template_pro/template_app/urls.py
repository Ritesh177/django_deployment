from django.urls import path
from template_app import views

#TEMPLATE TAGGING
app_name= 'template_app'

urlpatterns=[
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]
