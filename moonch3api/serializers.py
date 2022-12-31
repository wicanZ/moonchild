from rest_framework import serializers
from moonch3api.models import Note , User ,UserDetail


class LikeSerializer ( serializers.ModelSerializer ) :
    class Meta:
        model = User 
        fields = ['email']

class NoteSerializer( serializers.ModelSerializer  ) :
    likes = LikeSerializer( many=True , read_only=True)
    creator = serializers.ReadOnlyField(source='creator.email')
    
    class Meta :
        model = Note

        #fields = '__all__' #['id' , 'title' , 'likes']
        exclude = ['image']

class UserInfoSerializer( serializers.ModelSerializer  ) :
    class Meta :
        model = UserDetail
        fields = '__all__' #['id' , 'title' , 'likes']