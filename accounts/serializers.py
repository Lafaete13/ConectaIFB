from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password') 

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)

        # se houver nova senha, criptografa
        if password:
            user.set_password(password)

        user.save()
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        # atualiza os demais campos da tabela
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # se houver nova senha, criptografa
        if password:
            instance.set_password(password)
        
        instance.save()
        
        return instance
