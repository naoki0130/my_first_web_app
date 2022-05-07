from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class ImageModel(models.Model):
    image = CloudinaryField('image', folder="media/Model_image", blank=True, null=True,)
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )

    uploaded_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

    uploaded = models.DateTimeField(
    auto_now_add=True,
    editable=False,
    blank=False,
    null=False,
    )

    def get_absolute_url(self):
        # 新規作成後にcreateのurlへ飛ばないようにリンクを指定する
        return reverse_lazy('webapp:share:index_img')


class VideoModel(models.Model):
    video = CloudinaryField("video", folder="media/Model_movie", blank=True, null=True,)
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )

    uploaded_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

    uploaded = models.DateTimeField(
    auto_now_add=True,
    editable=False,
    blank=False,
    null=False,
    )

    def get_absolute_url(self):
        # 新規作成後にcreateのurlへ飛ばないようにリンクを指定する
        return reverse_lazy('webapp:share:index_mov')