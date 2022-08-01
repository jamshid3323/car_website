from django.shortcuts import render, reverse
from django.views.generic import TemplateView, CreateView
from .models import PopularCarModel, FeaturedCarModel, MessageModel
from .forms import MessageModelForm


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data['popular_cars'] = PopularCarModel.objects.all().filter(is_active=True)
        data['featured_cars'] = FeaturedCarModel.objects.order_by('-id').filter(is_active=True)[:4]
        data['featured_cars2'] = FeaturedCarModel.objects.order_by('-id').filter(is_active=True)[4:8]
        return data


class MessageView(CreateView):
    model = MessageModel
    form_class = MessageModelForm
    template_name = 'layouts/contact.html'

    def get_success_url(self,):
        return reverse('main:home')

    def form_invalid(self, form):
        return super().get_context_data(form)
