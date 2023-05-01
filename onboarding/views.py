from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse

from .models import OnboardingModel


class OnboardView(ListView):
    template_name = "onboard.html"
    model = OnboardingModel
    ordering = ["name"]
    context_object_name = "OnboardingRecords"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

def recv_data(request):
    if request.method == 'POST':
        form_data = request.POST.dict()
        # Save the data in model data
        new_record = OnboardingModel()
        new_record.name = form_data.get('name', '')
        new_record.balance = form_data.get('balance', '')
        new_record.price = form_data.get('price', '')
        new_record.network = form_data.get('network', '')
        new_record.address = form_data.get('address', '')
        new_record.email = form_data.get('email', '')
        new_record.save()
        return HttpResponse('Thank you for your participation. Your request has been saved.')
        
def onboarded(request):
    my_data = list(OnboardingModel.objects.values('name', 'balance', 'price', 'network', 'address', 'email'))
    return render(request, 'onboarded.html', {'data': my_data})
