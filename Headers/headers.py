# Headers i'll be importing every where using requests 
import os
from Authentification.auth import token


headers = {
    "Content-type" : "application/json",
    "Authrization":  f"Bearer{token}"
}