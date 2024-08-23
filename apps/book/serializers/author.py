from rest_framework import serializers
from apps.book.models import Author

class AuthorSerializer(serializers.ModelSerializer):
    # TODO: Specify the model that this serializer will link to
    # TODO: Specify which fields should be considered in the model

    # Force django REST to recognize the method
    name = serializers.CharField(read_only = True)
    # Create a serialized method
    username = serializers.SerializerMethodField()
    # Serialized methods implementation
    def get_username(self, obj):
        return '_'.join([obj.first_name, obj.last_name])

    def validate_first_name(self, value):
        """Field Level Validation - will always execute before object level validation"""
        if '-' in value:
            # TODO: always raise a validation exception
            raise serializers.ValidationError('first name should not contain hyphen (-)')
        
        # TODO: If condition is true, then return value
        return value
    
    def validate(self, attributes):
        """Object Level Validation"""
        if attributes.get('first_name') == attributes.get('last_name'):
            raise serializers.ValidationError('first and last name should not be the same')
        
        return attributes
    
   

    class Meta:
        model = Author
        fields = '__all__' # ('id'.'first_name','last_name')
        read_only_fields = ('id',)