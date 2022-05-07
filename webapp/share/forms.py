from cloudinary.forms import CloudinaryFileField
from django import forms

from webapp.share.models import ImageModel, VideoModel

class ImageUploadForm(forms.ModelForm):
	class Meta:
		model = ImageModel
		fields = ('image', 'title')

	image = CloudinaryFileField(
			options={'folder': 'media/Model_image', 'tags': 'Model_name'})

class VideoUploadForm(forms.ModelForm):
	class Meta:
		model = VideoModel
		fields = ('video', 'title')

	video = CloudinaryFileField(
			options={'folder': 'media/Model_movie', 'tags': 'Model_name',
					'resource_type': 'video'})