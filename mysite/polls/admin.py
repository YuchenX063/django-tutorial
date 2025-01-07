from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3 # by default, provide enough fields for 3 choices

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ['collapse']}),
    ]
    inlines = [ChoiceInLine]
# create a model admin class and pass it to admin.site.register() as the second argument
# inlines -- allow users to add question-related choices on the same page; used for models with foreign key relationships

admin.site.register(Question, QuestionAdmin)