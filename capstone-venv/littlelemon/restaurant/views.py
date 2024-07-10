from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from djoser import views as djoser_views
#from rest_framework_simplejwt.views import TokenObtainPairView
#from rest_framework_jwt.views import ObtainJSONWebToken

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
#    permission_classes = [permissions.IsAuthenticated] 

# Djoser views for user registration and profile retrieval
#class UserViewSet(djoser_views.UserViewSet):
#    pass

# Token generation (login) view
#class TokenLoginView(TokenObtainPairView):
#    pass