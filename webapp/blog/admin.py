from django.contrib import admin
from . import models

# カテゴリモデル
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

# タグモデル
@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    pass

# ポストモデル
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    pass