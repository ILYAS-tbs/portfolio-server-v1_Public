import requests


#todo : GET 

i=0
while(True):

    response = requests.get('http://127.0.0.1:8000/api/project/2')
    i+=1

    if(response.status_code != 200):
        break
    


print(f"requests : {i}")



