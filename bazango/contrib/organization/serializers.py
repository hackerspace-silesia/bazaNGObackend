from rest_framework import serializers
from .models import Organization, OrganizationProfile, Category
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)


class OrganizationProfileSerializer(TaggitSerializer, serializers.ModelSerializer):

    class Meta:
        model = OrganizationProfile
        exclude = ('organization',)


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class OrganizationSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    profile = OrganizationProfileSerializer(read_only=True)
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Organization
        fields = '__all__'
        depth = 1

