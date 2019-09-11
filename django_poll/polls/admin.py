from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "Django Poll Admin"
admin.site.site_title = "Django Poll Admin"
admin.site.index_title = "Welcome to Django Poll Admin"


class ChoiseInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiseInline]


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
