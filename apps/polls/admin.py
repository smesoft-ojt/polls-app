from django.contrib import admin
from apps.polls.models import PollsQuestion, Choice


# Register your models here.
class PollsQuestionAdmin(admin.ModelAdmin):
    list_display = [
        'question_text',
        'pub_date'
    ]


class ChoiceAdmin(admin.ModelAdmin):
    list_display = [
        'question',
        'choice_text',
        'votes'
    ]


admin.site.register(PollsQuestion, PollsQuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
