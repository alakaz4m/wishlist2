from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^dashboard$', views.dashboard),
        url(r'^wish_items/create/process$', views.create_item_process),
        url(r'^wish_items/create$', views.create_item),
        url(r'^wish_items/(?P<item_id>\d+)$', views.item_page),
        url(r'^wish_items/(?P<item_id>\d+)/destroy$', views.destroy),
        url(r'^wish_items/(?P<item_id>\d+)/add$', views.item_wishfor),
        url(r'^wish_items/(?P<item_id>\d+)/remove$', views.item_remove),

]
