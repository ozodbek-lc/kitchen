from django.db import models


class RecipeAuthorModel(models.Model):
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='authors/')
    bio = models.TextField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'recipe author'
        verbose_name_plural = 'recipe authors'


class RecipeModel(models.Model):
    image = models.ImageField(upload_to='recipes/')
    category = models.CharField(max_length=128)
    title = models.CharField(max_length=255)
    overview = models.CharField(max_length=255)
    duration = models.PositiveSmallIntegerField()
    serving = models.PositiveSmallIntegerField(default=1)

    author = models.ForeignKey(
        RecipeAuthorModel,
        on_delete=models.CASCADE,
        related_name='recipes'
    )
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'