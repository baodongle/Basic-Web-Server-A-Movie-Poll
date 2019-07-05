from django.contrib import admin

from IntekMovieFridayPoll.models import Choice, Question

admin.site.register(Question)
admin.site.register(Choice)
