from django.db import models

from .schedules_models import Schedule
from .custom_manager import *
from .user_models import *

# Evaluations
class Evaluation(models.Model):
    evaluator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Person conducting the evaluation
    schedule = models.ForeignKey(Schedule, on_delete=models.SET_NULL, null=True)
    observation_date = models.DateField()
    evaluation_type = models.CharField(max_length=255)
    additional_comments = models.TextField(null=True, blank=True)
    # JSON fields to store structured comments and activities
    instructor_comments = models.JSONField(null=True, blank=True)
    student_comments = models.JSONField(null=True, blank=True)
    student_activities = models.JSONField(null=True, blank=True)
    instructor_activities = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return f"{self.evaluator} - {self.schedule} - {self.observation_date} - {self.evaluation_type} - {self.additional_comments} - {self.created_at} - {self.updated_at} - {self.deleted_at}"

    def restore(self):
        self.deleted_at = None
        self.save()

    def delete(self):
        self.deleted_at = True
        self.save()

# Student Evaluations Table
class StudentEvaluation(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    user_professor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    import_questions = models.ManyToManyField("StudentEvaluationQuestion", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = CustomStudentEvaluation()

    def __str__(self):
        return f"{self.title} - {self.description} - {self.created_at} - {self.updated_at} - {self.deleted_at}"

    def restore(self):
        self.deleted_at = None
        self.save()

    def delete(self):
        self.deleted_at = True
        self.save()

#STUDENT EVALUATION QUESTION TABLE
class StudentEvaluationQuestion(models.Model):
    TYPE_CHOICES = [
        ("MCQ", "Multiple Choice"),
        ("TEXT", "Text Response"),
        ("RATING", "Rating Scale"),
    ]

    student_evaluation = models.ForeignKey(StudentEvaluation, on_delete=models.SET_NULL, null=True, blank=True)
    question = models.TextField()
    type = models.CharField(max_length=15, choices=TYPE_CHOICES)  # Limited choices
    options = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = CustomStudentEvaluation()


    def __str__(self):
        return f"{self.question} - {self.type} - {self.created_at} - {self.updated_at} - {self.deleted_at}"

    def restore(self):
        self.deleted_at = None
        self.save()

#STUDENT EVALUATION RESPONSE TABLE
class StudentEvaluationResponse(models.Model):
    student_evaluation = models.ForeignKey(StudentEvaluation, on_delete=models.SET_NULL, null=True)  # Links response to evaluation
    student_eval_question = models.ForeignKey(StudentEvaluationQuestion,
                                              on_delete=models.SET_NULL, null=True)  # Links response to question
    schedule = models.ForeignKey(Schedule, on_delete=models.SET_NULL, null=True)  # Links response to schedule
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Student who provided the response
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)



    def __str__(self):
        return f"{self.student_evaluation} - {self.schedule} - {self.user} - {self.answer} - {self.created_at} - {self.updated_at} - {self.deleted_at}"

    def restore(self):
        self.deleted_at = None
        self.save()

