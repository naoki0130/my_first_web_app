import imp
from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# カテゴリテーブル
class Category(models.Model):

    # カテゴリ名
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
    )

    def __str__(self):
        return self.name

# タグテーブル
class Tag(models.Model):

    # タグ名
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
    )

    def __str__(self):
        return self.name

# ポストテーブル
class Post(models.Model):

    # 作成日時
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=False,
        null=False,
    )

    # 更新日時
    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        blank=False,
        null=False,
    )

    # 著者
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

    # タイトル
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )

    # ボディ
    body = models.TextField(
        blank=True,
        null=False,
    )

    # カテゴリ：FK
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    # タグ：MtoM
    tags = models.ManyToManyField(
        Tag,
        blank=True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # 新規作成後にcreateのurlへ飛ばないようにリンクを指定する
        return reverse_lazy('webapp:blog:index')

