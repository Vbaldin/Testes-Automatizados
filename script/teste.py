import requests
import json

#Status 200 (sucesso)
def buscar_swapi_sucess():
    request = requests.get(f"https://swapi.dev/api/planets/1/")
    result= json.loads(request.content)
    print(result)
 

#Status 404(erro)
def buscar_swapi_error():
    request = requests.get(f"https://swapi.dev/api/planets/1878797/")
    result= json.loads(request.content)
    print(result)

#Status 200 (sucesso)
def buscar_swapi_people_sucess():
    request = requests.get(f"https://swapi.dev/api/people/1/")
    result= json.loads(request.content)
    print(result)
 

#Status 404(erro)
def buscar_swapi_people_error():
    request = requests.get(f"https://swapi.dev/api/people/1878797/")
    result= json.loads(request.content)
    print(result)

if __name__ == '__main__':
    buscar_swapi_sucess()
    buscar_swapi_error()
    buscar_swapi_people_sucess()
    buscar_swapi_people_error()