from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField() #HE MIGRADO SIN HABER GUARDADO ESTA COLUMNA
        
    class Meta:
        model = Review
        exclude = ('watchlist', )
        # fields = '__all__'

class WatchListSerializer(serializers.ModelSerializer):
    
    reviews = ReviewSerializer(many=True, read_only=True)
    
    # len_name = serializers.SerializerMethodField()
    
    class Meta:
        model = WatchList
        fields = '__all__'
        # fields = ['id', 'name', 'description'] # concretar los campos que quieres(apareceran todos los escritos en el array)
        # exclude = ['name'] concretar los campos que no quieres(NO apareceran todos los escritos en el array)

'''
class StreamPlatformSerializer(serializers.ModelSerializer):
    
    watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.StringRelatedField(many=True)
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='movie-detail')
    
    
    class Meta:
        model = StreamPlatform
        fields = '__all__'
'''


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    
    watchlist = WatchListSerializer(many=True, read_only=True) #HAY UN ERROR AQUI
    # watchlist = serializers.StringRelatedField(many=True)
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='movie-detail')
    
    
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        
    '''
    def get_len_name(self, object):
        length = len(object.name)
        return length
    
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Title and description should be different')
        else:
            return data
        
    def validate_name(self, value):
        
        if len(value) < 2:
            raise serializers.ValidationError('Name its too short')
        else:
            return value
    '''

'''
def name_lenght(value):
    if len(value) < 2:
            raise serializers.ValidationError('Name is too short')
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_lenght])
    description = serializers.CharField()
    active = serializers.BooleanField()
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
    
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Title and description should be different')
        else:
            return data
'''
'''
    def validate_name(self, value):
        
        if len(value) < 2:
            raise serializers.ValidationError('Name its too short')
        else:
            return value
'''