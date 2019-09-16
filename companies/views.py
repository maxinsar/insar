from django.shortcuts import render
from .models import Company, Vacancy, Comments
from django.http import HttpResponse
from django.views import View


class CompanyView(View):

    template_name = "company/list_company.html"

    def get(self, request, *args, **kwargs):
        companies = Company.objects.all()
        return render(request, self.template_name, {'companies':companies})
