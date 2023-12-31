
from django.urls import path, register_converter
from women import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'year4')


urlpatterns = [
    
    path('', views.index),
    path('cats/<slug:cat_slug>/', views.categories_by_slug),
    path('cats/<int:cat_id>/', views.categories),
    path('archive/<year4:year>/', views.archive)
]
