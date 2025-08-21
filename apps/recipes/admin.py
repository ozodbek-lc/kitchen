from django.contrib import admin

from apps.recipes.models import RecipeAuthorModel, RecipeModel

admin.site.register(RecipeAuthorModel)
admin.site.register(RecipeModel)