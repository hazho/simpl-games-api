from django.shortcuts import get_object_or_404

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Subscriber
from .serializers import SubscriberSerializer


class SubscriberList(ListCreateAPIView):
    model = Subscriber
    serializer_class = SubscriberSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).order_by('id')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SubscriberDetail(RetrieveUpdateDestroyAPIView):
    model = Subscriber
    serializer_class = SubscriberSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    lookup_field = 'id'

    def get_object(self):
        return get_object_or_404(self.model, user=self.request.user, id=self.kwargs['id'])
