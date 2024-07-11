#define URL route for index() view
from django.urls import path
from . import views
#import obtain_auth_token view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(), name='menu-list'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    #add following line in urlpatterns list
    path('api-token-auth/', obtain_auth_token)
]