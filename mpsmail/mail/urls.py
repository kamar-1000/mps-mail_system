from django.urls import path
from . import views
urlpatterns = [
	path('',views.home),
    path('home/',views.home),
    path('create/',views.create),
    path('sentmail/',views.sentmail),
    path('inbox/',views.inbox),
    path('inbox_view/<int:id>',views.inbox_view),
    path('sentmail_view/<int:id>',views.sentmail_view),
    path('notification',views.notification)

    #path('login/',views.login),
    #path('signup/',views.signup),
]
