from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from accounts.models import CustomUser


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'last_name', 'first_name', 'password', 'phone_number')

        def create(self, validated_data):
            return CustomUser.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.username = validated_data.get('username', instance.username)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.phone_number = validated_data.get('phone_number', instance.phone_number)

            instance.save()
            return instance

        def put(self, request, pk):
            global subscriber_saved
            saved_subscriber = get_object_or_404(CustomUser.objects.all(), pk=pk)
            data = request.data.get('article')
            serializer = UserSerializer(instance=saved_subscriber, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                subscriber_saved = serializer.save()
            return Response({"success": "Subscriber '{}' updated successfully".format(subscriber_saved.title)})

        def delete(self, request, pk):
            # Get object with this pk
            subscriber = get_object_or_404(CustomUser.objects.all(), pk=pk)
            subscriber.delete()
            return Response({"message": "Subscriber with id `{}` has been deleted.".format(pk)}, status=204)


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'phone_number', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(validated_data['username'], first_name=self.validated_data['first_name'],
                                              last_name=self.validated_data['last_name'],
                                              password=self.validated_data['password'],
                                              phone_number=self.validated_data['phone_number']
                                              )

        return user

