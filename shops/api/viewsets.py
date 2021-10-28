from django.db.models.query import QuerySet
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from shops.models import *
from rest_framework import status, generics
from django.http import  HttpResponse
from datetime import datetime
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import  Q

class CityView(APIView):
    """Отдает города"""
    # authentication_classes = (CsrfExemptSessionAuthentication, TokenAuthentication, BasicAuthentication)
    # permission_classes = [permissions.IsAuthenticated, IsEmployee]
    serializer_class = CitySerializer

    def get(self, request, *args, **kwargs):
        city=City.objects.all()
        serializer = CitySerializer(city, many = True)
        return Response(serializer.data)

class StreetView(APIView):
    """Отдает улицы по city_id"""
    # authentication_classes = (CsrfExemptSessionAuthentication, TokenAuthentication, BasicAuthentication)
    # permission_classes = [permissions.IsAuthenticated, IsEmployee]
    serializer_class = StreetSerializer

    def get(self, request, *args, city_id=None, **kwargs):
        street = Street.objects.filter(city__id=city_id)
        serializer = StreetSerializer(street, context={"request": request}, many = True)
        return Response(serializer.data)

class ShopView(generics.ListAPIView):
    """Отдает магазины"""
    serializer_class = ShopSerializer
    template_fields = ['name', 'city__name',  'street__name', 'house', 'opening_time', 'closing_time']
    search_fields = template_fields
    filterset_fields = template_fields
    filter_backends = [DjangoFilterBackend]

    # authentication_classes = (CsrfExemptSessionAuthentication, TokenAuthentication, BasicAuthentication)
    # permission_classes = [permissions.IsAuthenticated, IsEmployee]
    serializer_class = ShopSerializer

    def post(self, request, *args, event_id=None, **kwargs):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            """Здесь я возвращаю id последнего созданного объекта, и это неправильно
            Но у меня нет выбора, откуда мне брать id нового объекта, если его по тз запретили выводить ? Я могу делать фильтр по name, но это не уникальное значение
            :|
            """
            return Response(int(Shop.objects.last().id), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        data=Shop.objects.filter()
        data=self.status_logic(data)
        return data

    def status_logic(self, data):
        status=self.request.GET.get("status")
        if status != '1' and status != '0':
            return data
        if status=='1':
            queryset = data.filter(opening_time__lte=datetime.now(), closing_time__gt=datetime.now())
        if status=='0':
            queryset = data.filter(Q(opening_time__gte=datetime.now(), closing_time__gt=datetime.now()) | Q(opening_time__lte=datetime.now(), closing_time__lt=datetime.now()))
        return queryset


