from rest_framework import serializers

from comments.models import Comments, Users


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'
        extra_kwargs = {
             'id': {'read_only': False, 'allow_null': True},
        }


class CommentsSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Comments
        fields = '__all__'


    def create(self, validated_data):
        user_data = validated_data.pop('user')
        if user_data:
            try:
                user = Users.objects.get(pk=user_data.get('id'))
            except Users.DoesNotExist:
                try:
                    user = Users.objects.get(email=user_data.get('email'))
                except Users.DoesNotExist:
                    user_data.pop('id')
                    user = Users.objects.create(**user_data)
        else:
            user = None
        instance = Comments.objects.create(**validated_data)
        instance.user = user
        instance.save()
        return instance

