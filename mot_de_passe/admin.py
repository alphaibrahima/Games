from django.contrib import admin
from . import models





# Reorganisation du tableau d'administration des posts
@admin.register(models.UnContreUn)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user1', 'user2', 'is_accept', 'timestamp')
    # prepopulated_fields = {
    #     "slug" : ("title",),
    # }

# Reorganisation du tableau d'administration des comments
@admin.register(models.ScoreTwo)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user1', 'user2', 'points1', 'points2', "date")
    list_filter = ("user1", "user2", "points1", "points2")
    search_fields = ("points1", "points2", "user1", "user2")


admin.site.register(models.Mots)
admin.site.register(models.Score)
admin.site.register(models.Feedback)

