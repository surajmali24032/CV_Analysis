# Generated by Django 4.0.4 on 2022-05-13 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSubmittedAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('right_answer', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'User Submitted Answers',
            },
        ),
        migrations.DeleteModel(
            name='Exam',
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name_plural': 'Questions'},
        ),
        migrations.AddField(
            model_name='usersubmittedanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.question'),
        ),
        migrations.AddField(
            model_name='usersubmittedanswer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]