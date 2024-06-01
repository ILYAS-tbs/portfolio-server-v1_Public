### PRIVATE : 
    ## i'll later on put a public version of the server 
    ## with : .env in the setting.py

### Server is not yet deployment setup , it is development finished
```bash    
git rm -r --cached media
git rm -r --cached static
```

###

## API : 
 ## first endpoint : gets u all the projects 

- GET /api/projects/: 

``` json 
[
    {
        "id": 1,
        "links": {
            "id": 1,
            "deployedlinks_set": [
                {
                    "id": 1,
                    "deployment_link": "https://github.com/django",
                    "plateform": "web",
                    "created": "10:12:27.659759",
                    "updated": "10:12:27.659768",
                    "links": 1
                }
            ],
            "client_repo": "https://github.com/django",
            "server_repo": "https://github.com/django",
            "created": "10:09:48.061929",
            "updated": "10:09:48.061943"
        },
        "technologies": [
            {
                "id": 1,
                "color": "violet",
                "name": "Django",
                "created": "10:10:01.334865",
                "updated": "10:10:01.334875"
            }
        ],
        "image_set": [
            {
                "id": 1,
                "name": "first_screen",
                "img": "/media/portfolio/images/project2.jpeg",
                "created": "10:11:20.415746",
                "updated": "10:38:48.672035",
                "project": 1
            },
            {
                "id": 2,
                "name": "second screen",
                "img": "/media/portfolio/images/project1.jpeg",
                "created": "10:38:36.161348",
                "updated": "10:38:36.161362",
                "project": 1
            }
        ],
        "video_set": [
            {
                "id": 1,
                "name": "video on how to use",
                "video": "/media/portfolio/videos/duo.mp4",
                "created": "10:11:43.097427",
                "updated": "10:38:17.547517",
                "project": 1
            }
        ],
        "name": "portfolio",
        "desc": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        "system_design": "https://docs.djangoproject.com/en/5.0/contents/",
        "thumnail": "/media/portfolio/thumnails/project3.jpeg",
        "status": "working_on_it",
        "created": "10:10:36.376756",
        "updated": "10:37:56.231610"
    },
    {
        "id": 2,
        "links": {
            "id": 2,
            "deployedlinks_set": [],
            "client_repo": "https://github.com/djangohttps://github.com/django",
            "server_repo": "https://github.com/django",
            "created": "10:40:03.846535",
            "updated": "10:40:03.846550"
        },
        "technologies": [
            {
                "id": 1,
                "color": "violet",
                "name": "Django",
                "created": "10:10:01.334865",
                "updated": "10:10:01.334875"
            },
            {
                "id": 2,
                "color": "orange",
                "name": "git",
                "created": "10:10:18.620881",
                "updated": "10:10:18.620892"
            }
        ],
        "image_set": [],
        "video_set": [],
        "name": "another project",
        "desc": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        "system_design": "https://docs.djangoproject.com/en/5.0/contents/",
        "thumnail": "/media/another%20project/thumnails/python_64x64.png",
        "status": "working_on_it",
        "created": "10:40:25.156824",
        "updated": "10:40:25.156838"
    }
]
```

## second endpoint : gets u specific project ( filter by id )

- GET /api/project/ << projectid >>

``` json 

{
    "id": 2,
    "links": {
        "id": 2,
        "deployedlinks_set": [],
        "client_repo": "https://github.com/djangohttps://github.com/django",
        "server_repo": "https://github.com/django",
        "created": "10:40:03.846535",
        "updated": "10:40:03.846550"
    },
    "technologies": [
        {
            "id": 1,
            "color": "violet",
            "name": "Django",
            "created": "10:10:01.334865",
            "updated": "10:10:01.334875"
        },
        {
            "id": 2,
            "color": "orange",
            "name": "git",
            "created": "10:10:18.620881",
            "updated": "10:10:18.620892"
        }
    ],
    "image_set": [],
    "video_set": [],
    "name": "another project",
    "desc": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
    "system_design": "https://docs.djangoproject.com/en/5.0/contents/",
    "thumnail": "/media/another%20project/thumnails/python_64x64.png",
    "status": "working_on_it",
    "created": "10:40:25.156824",
    "updated": "10:40:25.156838"
}
```