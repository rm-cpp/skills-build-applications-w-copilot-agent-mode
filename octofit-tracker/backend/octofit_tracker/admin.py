from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'team')

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'duration', 'date')

class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('team', 'points')

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty')

admin.site.register(User, UserAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Leaderboard, LeaderboardAdmin)
admin.site.register(Workout, WorkoutAdmin)
