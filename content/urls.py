from django.urls import path
from content.views import home, contact
app_name ="content"
urlpatterns =[
    path("home/", home, name="home"),
    path("contact/", contact, name="contact"),
   
    
]