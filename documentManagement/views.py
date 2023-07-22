import django_filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializer import DocumentSerializer
from .models import Document


class DocumentApi(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['employer', 'typeContract', 'id', 'contractNumber', 'dateContract', 'topicContract',
                        'clearedStatus']

