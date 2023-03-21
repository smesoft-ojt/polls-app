from django.contrib import admin
from apps.polls.models import PollsQuestion, Choice

# Register your models here.
admin.site.register(PollsQuestion)
admin.site.register(Choice)
