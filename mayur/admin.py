from atexit import register
from django.contrib import admin
from mayur.models import Home, About, Profile, Category, Skills, Portfolio

# Register your models here.
admin.site.register(Home)


#About
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
    ]

#Skills
class SkillInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SkillInline,
    ]


#Portfolio
admin.site.register(Portfolio)