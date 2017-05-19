from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy, reverse

from .forms import *  # Create your views here.


class TestAdmin(TemplateView):
    template_name = "testadmin.html"


class TestFrontend(TemplateView):
    template_name = "testfront.html"


class PageCreateView(SuccessMessageMixin, CreateView):
    model = Page
    template_name = 'website/pageCreate.html'
    form_class = PageForm
    success_url = reverse_lazy("website:pageList")
    success_message = "Page Successfully Added"


class PageUpdateView(SuccessMessageMixin, UpdateView):
    model = Page
    template_name = 'website/pageUpdate.html'
    form_class = PageForm
    success_url = reverse_lazy("website:pageList")
    success_message = "Page Successfully Updated"


class PageDeleteView(SuccessMessageMixin, DeleteView):
    model = Page
    template_name = 'website/delete.html'
    success_url = reverse_lazy("website:pageList")
    success_message = "Page Successfully Deleted"


class PageDetailView(DetailView):
    model = Page
    template_name = 'website/pageDetail.html'


class PageListView(ListView):
    model = Page
    template_name = 'website/pageList.html'
    context_object_name = 'pages'

    def get_queryset(self):
        return Page.objects.filter(deleted_at=None)


class FrontendPageDetailView(DetailView):
    model = Page
    template_name = 'website/frontendPageDetail.html'


class EventCreateView(SuccessMessageMixin, CreateView):
    model = Event
    template_name = 'website/eventCreate.html'
    form_class = EventForm
    success_url = reverse_lazy("website:eventList")
    success_message = "Event Successfully Added"


class EventUpdateView(SuccessMessageMixin, UpdateView):
    model = Event
    template_name = 'website/eventUpdate.html'
    form_class = EventForm
    success_url = reverse_lazy("website:eventList")
    success_message = "Event Successfully Updated"


class EventDeleteView(SuccessMessageMixin, DeleteView):
    model = Event
    template_name = 'website/delete.html'
    success_url = reverse_lazy("website:eventList")
    success_message = "Event Successfully Deleted"


class EventDetailView(DetailView):
    model = Event
    template_name = 'website/eventDetail.html'


class EventListView(ListView):
    model = Event
    template_name = 'website/eventList.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.filter(deleted_at=None)


class MenuCreateView(SuccessMessageMixin, CreateView):
    model = Menu
    template_name = 'website/menuCreate.html'
    form_class = MenuForm
    success_url = reverse_lazy("website:menuList")
    success_message = "Menu Successfully Added"


class MenuUpdateView(SuccessMessageMixin, UpdateView):
    model = Menu
    template_name = 'website/menuUpdate.html'
    form_class = MenuForm
    success_url = reverse_lazy("website:menuList")
    success_message = "Menu Successfully Updated"


class MenuDeleteView(SuccessMessageMixin, DeleteView):
    model = Menu
    template_name = 'website/delete.html'
    success_url = reverse_lazy("website:menuList")
    success_message = "Menu Successfully Deleted"


class MenuDetailView(DetailView):
    model = Menu
    template_name = 'website/menuDetail.html'


class MenuListView(ListView):
    model = Menu
    template_name = 'website/menuList.html'
    context_object_name = 'menus'

    def get_queryset(self):
        return Menu.objects.filter(deleted_at=None)


class SliderCreateView(SuccessMessageMixin, CreateView):
    model = Slider
    template_name = 'website/sliderCreate.html'
    form_class = SliderForm
    success_url = reverse_lazy("website:sliderList")
    success_message = "Menu Successfully Added"


class SliderUpdateView(SuccessMessageMixin, UpdateView):
    model = Slider
    template_name = 'website/sliderUpdate.html'
    form_class = SliderForm
    success_url = reverse_lazy("website:sliderList")
    success_message = "Slider Successfully Updated"


class SliderDeleteView(SuccessMessageMixin, DeleteView):
    model = Slider
    template_name = 'website/delete.html'
    success_url = reverse_lazy("website:sliderList")
    success_message = "Slider Successfully Deleted"


class SliderDetailView(DetailView):
    model = Slider
    template_name = 'website/sliderDetail.html'


class SliderListView(ListView):
    model = Slider
    template_name = 'website/sliderList.html'
    context_object_name = 'photos'

    def get_queryset(self):
        return Slider.objects.filter(deleted_at=None)
