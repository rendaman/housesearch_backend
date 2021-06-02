from rest_framework import serializers
from .models import MakerCard, Reviews, Expense
from django.contrib.auth.models import User

class MakerCardSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = MakerCard
        fields = ('pk', 'name', 'name_hira', 'name_kata', 'name_eng', 'image_url', 'get_review_count', 'get_expense_count', 'get_expense_avg', 'get_landarea_avg', 'get_rateavg', 'ratetostr', 'get_costavg', 'get_designavg', 'get_layoutavg', 'get_specavg', 'get_attachavg', 'get_guaranteeavg', 'get_salesavg')
    def get_image_url(self, maker):
        request = self.context.get('request')
        image_url = maker.images.url
        return request.build_absolute_uri(image_url)
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('title', 'author', 'status', 'costrate', 'costcomment', 'designrate', 'designcomment', 'layoutrate', 'layoutcomment', 'specrate', 'speccomment', 'attachrate', 'attachcomment', 'guaranteerate', 'guaranteecomment', 'salesrate', 'salescomment', 'avgrate', 'maker_name', 'create_date', 'update_date')


class ExpenseSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Expense()
        fields = ('status', 'author', 'cost', 'landarea', 'gradecomment', 'costupcomment', 'costdowncomment', 'image_url', 'maker_name', 'create_date', 'update_date')
    def get_image_url(self, expense):
        request = self.context.get('request')
        image_url = ""
        if expense.image:
            image_url = request.build_absolute_uri(expense.image.url)
        return image_url

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = User
        fields = ('username',)

    def create(self, validated_data):
        return Account.objects.create_user(request_data=validated_data)