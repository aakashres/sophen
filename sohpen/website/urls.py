from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^testfront/$', TestFrontend.as_view(), name="test"),
    url(r'^$', HomeView.as_view(), name="home"),


    url(r'^sophenAdmin/$', Dashboard.as_view(), name="dashboard_main"),
    url(r'^sophenAdmin/dashboard/$', Dashboard.as_view(), name="dashboard"),
    url(r'^sophenAdmin/login/$', AdminLogInView.as_view(), name='adminLogIn'),
    url(r'^sophenAdmin/logout/$', AdminLogOutView.as_view(), name='adminLogOut'),
    url(r'^sophenAdmin/password-change/$',
        ChangePasswordView.as_view(), name='changePassword'),

    url(r'^sophenAdmin/page/list/$',
        PageListView.as_view(), name='pageList'),
    url(r'^sophenAdmin/conferenceMembership/list/$',
        ConferenceMemberListView.as_view(), name='confList'),
    url(r'^sophenAdmin/conferenceMembershipDetail/(?P<pk>[\d]+)$',
        ConferenceRegistrationDetailView.as_view(), name='confDetail'),
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

    url(r'^sophenAdmin/file/list/$',
        FileListView.as_view(), name='fileList'),
    url(r'^sophenAdmin/file/create/$',
        FileCreateView.as_view(), name='fileCreate'),
    url(r'^sophenAdmin/file/(?P<pk>[\d]+)/update/$',
        FileUpdateView.as_view(), name='fileUpdate'),
    url(r'^sophenAdmin/file/(?P<pk>[\d]+)/delete/$',
        FileDeleteView.as_view(), name='fileDelete'),


    url(r'^sophenAdmin/gallery/list/$',
        GalleryListView.as_view(), name='galleryList'),
    url(r'^sophenAdmin/gallery/create/$',
        GalleryCreateView.as_view(), name='galleryCreate'),
    url(r'^sophenAdmin/gallery/(?P<pk>[\d]+)/$',
        GalleryDetailView.as_view(), name='galleryDetail'),
    url(r'^sophenAdmin/gallery/(?P<pk>[\d]+)/update/$',
        GalleryUpdateView.as_view(), name='galleryUpdate'),
    url(r'^sophenAdmin/gallery/(?P<pk>[\d]+)/delete/$',
        GalleryDeleteView.as_view(), name='galleryDelete'),

    url(r'^sophenAdmin/member/list/$',
        MemberListView.as_view(), name='memberList'),

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
    url(r'^event/(?P<slug>[\w-]+)/$',
        FrontendEventDetailView.as_view(), name='frontendEventDetail'),
    url(r'^events/$',
        FrontendEventListView.as_view(), name='frontendEventList'),
    url(r'^gallery/$',
        FrontendGalleryListView.as_view(), name='frontendGalleryList'),
    url(r'^files/$',
        FrontendFileListView.as_view(), name='frontendFileList'),
    url(r'^membership/$',
        MembershipView.as_view(), name='membership'),
    
    url(r'^conference-membership/$',
        ConferenceMembershipView.as_view(), name='confmembership'),
    url(r'^contact/$',
        ContactView.as_view(), name='contact'),
    url(r'^members/$',
        CommitteeMember.as_view(), name='members'),
]
