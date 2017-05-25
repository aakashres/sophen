from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView, View
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


from .forms import *  # Create your views here.


class Dashboard(TemplateView):
    template_name = "dashboard.html"


class TestFrontend(TemplateView):
    template_name = "testfront.html"


class AdminLogInView(View):
    def get(self, request):
        form = LogInForm()
        context = {
            'form': form,
        }
        return render(request, 'website/adminLogIn.html', context)

    def post(self, request):
        form = LogInForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                messages.success(request, "Logged In Successfully")
                login(request, user)
                return redirect('website:dashboard')
        messages.warning(request, "Log In Failure")
        context = {
            'form': form,
        }
        return render(request, 'website/adminLogIn.html', context)


class AdminLogOutView(View):
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            logout(request)
        messages.success(request, "Logged Out Successfully")
        return redirect('website:adminLogIn')


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


class FrontendPageDetailView(DetailView):
    model = Page
    template_name = 'website/frontendPageDetail.html'


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'website/home.html', context)


class FrontendEventListView(ListView):
    model = Event
    template_name = 'website/frontendEventList.html'
    context_object_name = 'events'
    paginate_by = 12

    def get_queryset(self):
        return Event.objects.filter(deleted_at=None)


class FrontendEventDetailView(DetailView):
    model = Event
    template_name = 'website/frontendEventDetail.html'
