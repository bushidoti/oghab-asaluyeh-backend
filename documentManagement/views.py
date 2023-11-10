import django_filters
from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, BasePermission
from django_filters.fields import CSVWidget, MultipleChoiceField
from .serializer import DocumentSerializer
from .models import Document
from django_filters import rest_framework as df_filters


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'size'
    page_query_param = 'page'


class MyPermission(BasePermission):
    message = "دسترسی لازم را ندارید."
    permission_map = {
        "GET": "{app_label}.view_{model_name}",
        "POST": "{app_label}.add_{model_name}",
        "PUT": "{app_label}.change_{model_name}",
        "PATCH": "{app_label}.change_{model_name}",
        "DELETE": "{app_label}.delete_{model_name}",
    }

    def _get_permission(self, method, perm_slug):
        app, model = perm_slug.split(".")
        if method not in self.permission_map:
            raise MethodNotAllowed(method)
        perm = self.permission_map.get(method).format(app_label=app, model_name=model)
        return perm

    def has_permission(self, request, view):
        perm = self._get_permission(
            method=request.method, perm_slug=view.perm_slug
        )
        if request.user.has_perm(perm):
            return True
        return False


class MultipleField(MultipleChoiceField):
    def valid_value(self, value):
        return True


class MultipleFilter(df_filters.MultipleChoiceFilter):
    field_class = MultipleField


class DocumentFilter(django_filters.rest_framework.FilterSet):
    name = django_filters.rest_framework.CharFilter(field_name='name', lookup_expr='contains')
    type = django_filters.rest_framework.CharFilter(field_name='type', lookup_expr='contains')
    topicContract = django_filters.rest_framework.CharFilter(field_name='topicContract', lookup_expr='contains')
    contractNumber = django_filters.rest_framework.CharFilter(field_name='contractNumber', lookup_expr='contains')
    typeContract = django_filters.rest_framework.CharFilter(field_name='typeContract', lookup_expr='contains')
    office = MultipleFilter(
        lookup_expr="contains",
        field_name="office",
        widget=CSVWidget
    )
    type_form = MultipleFilter(
        lookup_expr="contains",
        field_name="type_form",
        widget=CSVWidget
    )
    dateContract = django_filters.rest_framework.CharFilter(field_name='dateContract', lookup_expr='contains')
    id = django_filters.rest_framework.NumberFilter(field_name='id', lookup_expr='contains')
    clearedStatus = django_filters.rest_framework.BooleanFilter(field_name='clearedStatus', lookup_expr='contains')

    class Meta:
        model = Document
        fields = ['name', 'type_form', 'contractNumber', 'office', 'typeContract', 'topicContract',
                  'dateContract', 'clearedStatus', 'id']


class DocumentApi(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, MyPermission]
    perm_slug = "documentManagement.document"
    pagination_class = CustomPageNumberPagination
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = DocumentFilter
