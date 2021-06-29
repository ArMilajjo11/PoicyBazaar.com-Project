from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'getbooking', views.BookingViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('',views.home, name='home'),
    path('register',views.register, name='register'),
    path('login',views.login, name='login'),
    path('book',views.book, name="book"),
    path('logout',views.logout, name="logout")
]



# path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))