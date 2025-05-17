from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import get_object_or_404
from .models import Event, Booking
from .serializers import *
from django.http import HttpResponseRedirect

# List all events
class EventListAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]

# Retrieve event details
class EventDetailAPIView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'
    lookup_url_kwarg = 'event_id'

# Book an event (requires authentication)
class BookEventAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        already_booked = Booking.objects.filter(user=request.user, event=event).exists()
        
        if already_booked:
            return Response({"detail": "Already booked"}, status=status.HTTP_400_BAD_REQUEST)

        Booking.objects.create(user=request.user, event=event)
        return Response({"detail": "Booking successful"}, status=status.HTTP_201_CREATED)
    
# List bookings of the authenticated user
class UserBookingListAPIView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

# Registration endpoint (API version)
class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def toggle_theme(request):
    current = request.COOKIES.get('theme', 'light')
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie('theme', 'dark' if current == 'light' else 'light')
    return response
