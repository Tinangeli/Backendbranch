from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from hrapp.models.evaluation_models import *
from hrapp.models.custom_manager import *
from hrapp.models.user_models import *
from hrapp.models.schedules_models import *

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Supervisor', {'fields': ('supervisor',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # ✅ Modify this section to include more fields in the "Add User" form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'supervisor', 'is_staff', 'is_active')}
        ),
    )

    def get_queryset(self, request):
        return User.all_objects.all()  # Show all users (including deleted)


    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)


@admin.register(StudentEvaluation)
class StudentEvaluationAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')


@admin.register(StudentEvaluationQuestion)
class StudentEvaluationQuestionsAdmin(admin.ModelAdmin):
    list_display = ('student_evaluation', 'question', 'type', 'options')


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ("evaluator", "schedule", "observation_date", "evaluation_type", "additional_comments", "instructor_comments", "student_comments", "student_activities", "instructor_activities", "created_at", "updated_at", "deleted_at")

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("course", "professor", "subject", "room", "name", "start_time", "end_time", "semester", "year", "is_active", "deleted_at", "created_at", "updated_at")

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "code" , "is_active", "deleted_at", "created_at", "updated_at")

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
     list_display = ("name", "slug", "is_active", "deleted_at", "created_at", "updated_at")

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_active", "deleted_at", "created_at", "updated_at")

@admin.register(FacultyAssignment)
class FacultyAssignmentAdmin(admin.ModelAdmin):
    list_display = ("user", "schedule", "created_at", "updated_at", "deleted_at")