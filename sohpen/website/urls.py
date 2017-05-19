from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^testadmin/$', TestAdmin.as_view(), name="testadmin"),
    url(r'^testfront/$', TestFrontend.as_view(), name="test"),

    url(r'^sophenAdmin/page/list/$',
        PageListView.as_view(), name='pageList'),
    url(r'^sophenAdmin/page/create/$',
        PageCreateView.as_view(), name='pageCreate'),
    url(r'^sophenAdmin/page/(?P<slug>[\w-]+)/$',
        PageDetailView.as_view(), name='pageDetail'),
    url(r'^sophenAdmin/page/(?P<slug>[\w-]+)/update/$',
        PageUpdateView.as_view(), name='pageUpdate'),
    url(r'^sophenAdmin/page/(?P<slug>[\w-]+)/delete/$',
        PageDeleteView.as_view(), name='pageDelete'),

    url(r'^sophenAdmin/event/list/$',
        EventListView.as_view(), name='eventList'),
    url(r'^sophenAdmin/event/create/$',
        EventCreateView.as_view(), name='eventCreate'),
    url(r'^sophenAdmin/event/(?P<slug>[\w-]+)/$',
        EventDetailView.as_view(), name='eventDetail'),
    url(r'^sophenAdmin/event/(?P<slug>[\w-]+)/update/$',
        EventUpdateView.as_view(), name='eventUpdate'),
    url(r'^sophenAdmin/event/(?P<slug>[\w-]+)/delete/$',
        EventDeleteView.as_view(), name='eventDelete'),

    url(r'^sophenAdmin/menu/list/$',
        MenuListView.as_view(), name='menuList'),
    url(r'^sophenAdmin/menu/create/$',
        MenuCreateView.as_view(), name='menuCreate'),
    url(r'^sophenAdmin/menu/(?P<pk>[\d]+)/$',
        MenuDetailView.as_view(), name='menuDetail'),
    url(r'^sophenAdmin/menu/(?P<pk>[\d]+)/update/$',
        MenuUpdateView.as_view(), name='menuUpdate'),
    url(r'^sophenAdmin/menu/(?P<pk>[\d]+)/delete/$',
        MenuDeleteView.as_view(), name='menuDelete'),


    url(r'^sophenAdmin/slider/list/$',
        SliderListView.as_view(), name='sliderList'),
    url(r'^sophenAdmin/slider/create/$',
        SliderCreateView.as_view(), name='sliderCreate'),
    url(r'^sophenAdmin/slider/(?P<pk>[\d]+)/$',
        SliderDetailView.as_view(), name='sliderDetail'),
    url(r'^sophenAdmin/slider/(?P<pk>[\d]+)/update/$',
        SliderUpdateView.as_view(), name='sliderUpdate'),
    url(r'^sophenAdmin/slider/(?P<pk>[\d]+)/delete/$',
        SliderDeleteView.as_view(), name='sliderDelete'),

    url(r'^page/(?P<slug>[\w-]+)/$',
        FrontendPageDetailView.as_view(), name='frontendPageDetail'),
]
