from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerForDraftOrManipulations
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filterset_class = AdvertisementFilter
    search_fields = ['title', 'description', ]
    ordering_fields = ['title', 'status', 'created_at', ]

    def get_permissions(self):
        """Получение прав для действий."""

        if self.request.user.is_staff:
            return [IsAdminUser()]

        permissions = [IsOwnerForDraftOrManipulations()]
        if self.action in ["create", "update", "partial_update", "destroy"]:
            permissions += [IsAuthenticated()]

        # if self.action in ["update", "partial_update", "destroy"]:
        #     permissions.append()

        return permissions
