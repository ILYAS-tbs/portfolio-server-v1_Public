from django.shortcuts import render ,HttpResponse

from rest_framework.decorators import api_view ,throttle_classes
from rest_framework.response import Response

from rest_framework.throttling import UserRateThrottle ,AnonRateThrottle

from .models import Project
from .serializers import ProjectSerializer
# Create your views here.


@api_view()
def ping_pong_view(request): 


    return Response({"message":'server is running ...'})


@api_view(['GET'])
@throttle_classes([UserRateThrottle,AnonRateThrottle])
def get_projects_view(request):

    projects_query_set= Project.objects.all()


    serializer = ProjectSerializer(projects_query_set , many =True)

    return Response(serializer.data , status=200)

@api_view(['GET'])
@throttle_classes([UserRateThrottle,AnonRateThrottle])
def get_project_view(request , pk ):

    try:
            project_instance = Project.objects.get(id=pk)

    except Project.DoesNotExist:
         return Response({"message":"ERROR NOT FOUND 404 "} , status=404)

    serializer = ProjectSerializer(project_instance)

    return Response(serializer.data , status=200)
