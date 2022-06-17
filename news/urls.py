from django.urls import path
from .views import news_list, news_detail, news_category, news_create, news_delete, news_update

urlpatterns = [
    path("", news_list, name="news_list"),
    path("category/<int:id>", news_category, name="news_category"),
    path("deleteNews/<int:id>", news_delete, name="news_delete"),
    path("addupdate/<int:id>", news_update, name="news_update"),
    path("<slug:slug>/<int:id>", news_detail, name="news_detail"),
    path("addnews/", news_create, name="news_create"),
]
