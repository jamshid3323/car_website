from django.shortcuts import render
from django.views.generic import TemplateView
from .models import PopularCarModel, FeaturedCarModel


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data['popular_cars'] = PopularCarModel.objects.all().filter(is_active=True)
        data['featured_cars'] = FeaturedCarModel.objects.order_by('-id').filter(is_active=True)[:4]
        data['featured_cars2'] = FeaturedCarModel.objects.order_by('-id').filter(is_active=True)[4:8]
        return data
