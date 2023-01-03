from django.http import HttpResponseBadRequest
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from .models import Entity
from .serializers import EntitySerializer


class EntityViewset(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

    # =======================================
    # решение 1 вопроса
    # =======================================
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save(modified_by=self.request.user)
        except ValueError:
            return HttpResponseBadRequest('<a href="/admin/">Авторизуйтесь!</a>')
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
