from rest_framework import serializers 
from .models import Project, Links ,Tech , Image , Video , DeployedLinks




class ImageSerializer(serializers.ModelSerializer):

    class Meta():
        model=Image
        fields='__all__'

class VideoSerializer(serializers.ModelSerializer):
    
    class Meta():
        model=Video
        fields='__all__'

class TechSerializer(serializers.ModelSerializer):

    class Meta():
        model=Tech
        fields='__all__'


class DeployedLinksSerializer(serializers.ModelSerializer):
   
    class Meta():
        model =DeployedLinks 
        fields='__all__'  


class LinksSerialzer(serializers.ModelSerializer):
   
    deployedlinks_set =DeployedLinksSerializer(many=True)
    class Meta():
        model =Links 
        fields='__all__'

class ProjectSerializer(serializers.ModelSerializer):
    
    links = LinksSerialzer(many=False)
    technologies = TechSerializer(many=True)
    image_set =ImageSerializer(many=True)
    video_set=VideoSerializer(many=True)


    class Meta():
        model =Project 
        fields='__all__'