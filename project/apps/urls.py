from django.urls import path
from . import views
urlpatterns = [
    path("personal/",views.personal_data, name = "personal_data"),
    path("forms_page/",views.forms, name = "forms_page"),
]
