from django.contrib import admin

from users.models import Fiscal, Requisitante, Xerox

# Register your models here.

admin.site.register(Fiscal)
admin.site.register(Requisitante)
admin.site.register(Xerox)