from django.contrib import admin

# Register your models here.
from .models import user
from .models import Ticket
from .models import Agent
admin.site.register(user)
admin.site.register(Ticket)
admin.site.register(Agent)