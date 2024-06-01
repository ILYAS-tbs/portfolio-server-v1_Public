from django.db import models


#! a fucntion i didnt know about before
# todo : type will be : thumbnail/ , images/ , video
def img_upload_to(instance, filename):
    
    return f"{instance.project.name}/images/{filename}"

def vid_upload_to(instance, filename):
    
    return f"{instance.project.name}/videos/{filename}"

def thumnail_upload_to(instance, filename):
    
    return f"{instance.name}/thumnails/{filename}"

# Create your models here.

class Project(models.Model):
    name =models.CharField(max_length=255)
    desc =models.TextField()
    # todo : a downloadable file link
    system_design=models.URLField(max_length=255)
    thumnail=models.ImageField(upload_to=thumnail_upload_to)
    
    # todo :has 3 possible values {completed , incomplete , working_on_it}
    status=models.CharField(max_length=20)

    links=models.OneToOneField(
        'Links',
        on_delete=models.CASCADE
    )

    technologies = models.ManyToManyField(
        'Tech'
    )



    #! date 

    created=models.TimeField(auto_now_add=True)
    updated=models.TimeField(auto_now=True)

    #! str  
    def __str__(self):
        return self.name

class Links(models.Model):
    client_repo=models.URLField(max_length=255) 
    
    server_repo=models.URLField(max_length=255) 
   
    
    #! date 

    created=models.TimeField(auto_now_add=True)
    updated=models.TimeField(auto_now=True)

  

class DeployedLinks(models.Model):
    deployment_link=models.URLField(max_length=255)
    plateform = models.CharField(max_length=255)
    
    # todo : this model is a part of the links model
    links =models.ForeignKey( 
        Links , 
        on_delete=models.CASCADE 
    )
      #! date 

    created=models.TimeField(auto_now_add=True)
    updated=models.TimeField(auto_now=True)

  
class Tech(models.Model):
    color=models.CharField(max_length=7)
    name=models.CharField(max_length=255)

      #! date 

    created=models.TimeField(auto_now_add=True)
    updated=models.TimeField(auto_now=True)

     #! str 
    def __str__(self):
        return self.name




class Image(models.Model):
  
  
    name = models.CharField(max_length=50)
    project = models.ForeignKey( 
        Project ,
        on_delete=models.CASCADE
    )
    img = models.ImageField(upload_to=img_upload_to)

      #! date 

    created=models.TimeField(auto_now_add=True)
    updated=models.TimeField(auto_now=True)

 

 

class Video(models.Model):

    name = models.CharField(max_length=50)
    project = models.ForeignKey( 
        Project ,
        on_delete=models.CASCADE
    )
    video = models.FileField(upload_to=vid_upload_to)
      #! date 

    created=models.TimeField(auto_now_add=True)
    updated=models.TimeField(auto_now=True)
 

