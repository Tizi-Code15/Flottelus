# auth scripts to authentificat on swagger api 
import requests, os
from dotenv import load_dotenv
from hashpass import hashedpass

load_dotenv()

# create ur own url and login on .env file 
Base_Url = os.getenv("Base_Url")
login = os.getenv("login")

def authentification (login, hashedpass):

    Url = f"{Base_Url}/public/jwt/login"

    headers={
        "Content-Type" : "application/json" 
    }
    Data = {
    "login" : login,
    "password": hashedpass,
}
    response = requests.post(Url, json=Data, headers=headers)

    if response.status_code == 200:
        # show response statuts simple print 
        print (response)
        return response.json().get("id_token")
    else :
        # show error status 
        raise Exception (f"Erreur: {response.status_code} - {response.text}")
    

token = authentification(login, hashedpass)

print (token)