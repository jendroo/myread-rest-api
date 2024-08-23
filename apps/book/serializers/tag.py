from rest_framework import serializers
from apps.book.models import Tag

class TagSerializer(serializers.ModelSerializer):
    # TODO: Specify the model that this serializer will link to
    # TODO: Specify which fields should be considered in the model

    def validate_name(self, value):
        """Field Level Validation - will always execute before object level validation"""
        if any(char in value for char in '%!@#$%^&*') in value:
        #if re.search(r'[!@#$%^&*]', value):
            # TODO: always raise a validation exception
            raise serializers.ValidationError('name should not contain special characters')
        
        # TODO: If condition is true, then return value
        return value
        # Create a serialized method
    name = serializers.SerializerMethodField()
    # Serialized methods implementation
    def get_name(self, obj):
        return obj.name.title()

    class Meta:
        model = Tag
        fields = '__all__'
        read_only_fields = ('id',)