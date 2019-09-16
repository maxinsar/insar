from django.contrib import admin

from .models import Company, Vacancy, Comments


admin.site.register(Company)
admin.site.register(Vacancy)
admin.site.register(Comments)
