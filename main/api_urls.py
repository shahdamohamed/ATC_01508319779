from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  
    TokenRefreshView,     
    TokenBlacklistView    
)

urlpatterns = [
    path('events/', EventListAPIView.as_view(), name='api_events'),
    path('events/<int:event_id>/', EventDetailAPIView.as_view(), name='api_event_detail'),
    path('events/<int:event_id>/book/', BookEventAPIView.as_view(), name='api_book_event'),
    path('bookings/', UserBookingListAPIView.as_view(), name='api_user_bookings'),
    path('register/', RegisterAPIView.as_view(), name='api_register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    path('api/token/logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    
]
