from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from django_comments.models import Comment
from core.models import User, Item, Image
from versatileimagefield.serializers import VersatileImageFieldSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class UserSerializer(serializers.ModelSerializer):
    profile_picture = VersatileImageFieldSerializer(
        sizes=[
            ('thumbnail__50x50', 'thumbnail__50x50'),
        ]
    )

    class Meta:
        model = User
        fields = ('pk', 'username', 'profile_picture')


class ImageSerializer(serializers.ModelSerializer):
    itemshot = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail__100x100', 'thumbnail__100x100'),
            ('thumbnail__300x200', 'thumbnail__300x200'),
            ('thumbnail__400x400', 'thumbnail__400x400'),
        ]
    )

    class Meta:
        model = Image
        fields = ('id', 'itemshot')


class ItemSerializer(GeoFeatureModelSerializer):
    image_ids = serializers.CharField(max_length=200, write_only=True)
    images = ImageSerializer(many=True, read_only=True)
    user_id = serializers.CharField(max_length=20, write_only=True)
    user = UserSerializer(read_only=True)
    cnt_of_comments = serializers.SerializerMethodField()

    def get_cnt_of_comments(self, obj):
        # TODO use calculated values instead of constant
        return Comment.objects.filter(
            object_pk=obj.id, content_type=8, site_id=1).count()

    class Meta:
        model = Item
        geo_field = "point"

        fields = ('pk', 'memo', 'created_at', 'images', 'image_ids',
                  'user_id', 'user', 'price', 'address', 'created_at',
                  'cnt_of_comments')

    def create(self, validated_data):
        image_ids = validated_data.pop('image_ids')
        item = super(ItemSerializer, self).create(validated_data)

        for image_id in image_ids.split(','):
            try:
                image = Image.objects.get(id=image_id)
                item.images.add(image)

            except ObjectDoesNotExist:
                pass

        return item


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
