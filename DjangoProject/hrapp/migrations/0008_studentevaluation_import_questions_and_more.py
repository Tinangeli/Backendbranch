# Generated by Django 5.1.7 on 2025-03-31 06:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrapp', '0007_alter_user_options_studentevaluation_user_professor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentevaluation',
            name='import_questions',
            field=models.ManyToManyField(blank=True, to='hrapp.studentevaluationquestion'),
        ),
        migrations.AlterField(
            model_name='studentevaluationquestion',
            name='student_evaluation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hrapp.studentevaluation'),
        ),
    ]
