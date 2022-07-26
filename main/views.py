from django.shortcuts import render
from django.views.generic import TemplateView
from .models import PopularCarModel


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data['popular_cars'] = PopularCarModel.objects.all().filter(is_active=True)
        return data
