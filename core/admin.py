from django.contrib import admin
from . import models
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'level']
admin.site.register(models.Question,QuestionAdmin)

class UserSubmittedAnswerAdmin(admin.ModelAdmin):
    list_display=['id','question','user','right_answer']
admin.site.register(models.UserSubmittedAnswer,UserSubmittedAnswerAdmin)

class SkillAdmin(admin.ModelAdmin):
    list_display= ['user', 's1', 's2', 's3', 'sv1','sv2','sv3']
admin.site.register(models.Skill,SkillAdmin)


