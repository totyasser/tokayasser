# portfolio/admin.py

from django.contrib import admin
from .models import Education, Experience, Skill, Portfolio, Testimonial

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_date', 'end_date')
    list_filter = ('institution', 'start_date')
    search_fields = ('degree', 'institution')
    ordering = ('-start_date',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'start_date', 'end_date')
    list_filter = ('company', 'start_date')
    search_fields = ('job_title', 'company')
    ordering = ('-start_date',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency')
    list_filter = ('proficiency',)
    search_fields = ('name',)
    ordering = ('-proficiency', 'name')



@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Remove 'company'
    list_filter = ('created_at',)
    search_fields = ('title', 'description')
    ordering = ('-created_at',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('name', 'comment')
    ordering = ('-created_at',)
