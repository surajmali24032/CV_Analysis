from django.db import models
from django.contrib.auth.models import User




# Create your models here.

# class Exam(models.Model):
#     question = models.CharField(max_length=100)
#     option1 = models.CharField(max_length=100)
#     option2 = models.CharField(max_length=100)
#     option3 = models.CharField(max_length=100)
#     option4 = models.CharField(max_length=100)
#     corrans = models.CharField(max_length=100)

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    s1 = models.CharField(max_length=200, default='Null')
    s2 = models.CharField(max_length=200, default='Null')
    s3 = models.CharField(max_length=200, default='Null')
    sv1 = models.CharField(max_length=200, default='Null')
    sv2 = models.CharField(max_length=200, default='Null')
    sv3 = models.CharField(max_length=200, default='Null')

# aptitude questions
class Question(models.Model):
    # category = models.ForeignKey()
    question = models.TextField()
    opt_1 = models.CharField(max_length=200)
    opt_2 = models.CharField(max_length=200)
    opt_3 = models.CharField(max_length=200)
    opt_4 = models.CharField(max_length=200)
    level = models.CharField(max_length=100)
    # time_limit = models.IntegerField()
    right_opt = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='Questions'

    def __str__(self):
        return self.question

# User submited answers
class UserSubmittedAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    right_answer = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural='User Submitted Answers'
