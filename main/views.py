from django.shortcuts import render, reverse
from django.views.generic import TemplateView, CreateView
from .models import PopularCarModel, FeaturedCarModel, MessageModel
from .forms import MessageModelForm
from django.core.mail import send_mail
from django.conf.global_settings import EMAIL_HOST_USER
from .utils import send_bot_message


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
        return super().form_invalid(form)

    def form_valid(self, form):
        # message = f"Assalomu alaykum {form.instance.name}! xabaringizni qabul qildim."
        # send_mail("Yangi xabar", message, EMAIL_HOST_USER, [form.instance.email])
        send_bot_message(form.cleaned_data)
        return super().form_valid(form)
