from rest_framework.permissions import IsAuthenticated
from advertisements.permissions import IsOwnerOrReadOnly
from rest_framework.viewsets import ModelViewSet
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from django_filters.rest_framework import DjangoFilterBackend
from advertisements.filters import AdvertisementFilter


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['creator', 'status']
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """
        Получение прав для действий. Пользователь авторизован для создания записи и
        подтверждения его прав на удаления и редактирования записии.
        """
        if self.action == "create":
            return [IsAuthenticated()]
        elif self.action in ["destroy", "update", "partial_update"]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return []
