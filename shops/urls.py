from django.urls import path, include
from .api import viewsets


urlpatterns = [
    path('city/', viewsets.CityView.as_view()),
    path('city/street/<str:city_id>/', viewsets.StreetView.as_view()),
    path('shop/', viewsets.ShopView.as_view()),
]


"""
1. В случае успешной обработки сервис должен отвечать статусом 200, в
случае любой ошибки — статус 400.
2. Сохранение всех объектов в базе данных.
3. Запросы:
a. GET /city/ — получение всех городов из базы;
b. GET /city//street/ — получение всех улиц города; (city_id —
идентификатор города)
c. POST /shop/ — создание магазина; Данный метод получает json c
объектом магазина, в ответ возвращает id созданной записи.
d. GET /shop/?street=&city=&open=0/1 — получение списка магазинов;
i. Метод принимает параметры для фильтрации. Параметры не
обязательны. В случае отсутствия параметров выводятся все
магазины, если хоть один параметр есть , то по нему
выполняется фильтрация.
ii. Важно!: в объекте каждого магазина выводится название
города и улицы, а не id записей.
iii. Параметр open: 0 - закрыт, 1 - открыт. Данный статус
определяется исходя из параметров «Время открытия»,
«Время закрытия» и текущего времени сервера.


"""