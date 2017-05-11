from django.views import View
from django.shortcuts import render

from django.utils import timezone


class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        context = {}

        return render(request, self.template_name, context)
