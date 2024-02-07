from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
import csv

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes),"utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type" : "client_credentials"}
    result = post(url, headers = headers, data = data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers = headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print("No artist with this name exists.")
        return None
    
    return json_result[0]

# iterate through the list to get artist info
lineup=["Adam Ten x Mita Gami",
        "The Adicts",
        "Adriatique",
        "Âme x Marcel Dettmann",
        "Anotr",
        "Anti Up",
        "Anyma",
        "AP Dhillon",
        "The Aquabats",
        "Artbat",
        "Atarashii Gakko!",
        "Ateez",
        "Bar Italia",
        "Barry Can’t Swim",
        "Bb Trickz",
        "Bebe Rexha",
        "Ben Sterling",
        "The Beths",
        "Bicep",
        "Bizarrap",
        "Black Country, New Road",
        "Bleachers",
        "The Blessed Madonna",
        "Blond:ish",
        "Blur",
        "Blxst",
        "Boy Harsher",
        "Brittany Howard",
        "Brutalismus 3000",
        "Carin León",
        "Carlita",
        "Chappell Roan",
        "Charlotte de Witte",
        "Chlöe",
        "Cimafunk",
        "Cloonee",
        "Clown Core",
        "Coi Leray",
        "Deftones",
        "Depresión Sonora",
        "Destroy Lonely",
        "DJ Seinfeld",
        "DJ Snake",
        "Dom Dolla",
        "The Drums",
        "Eartheater",
        "Eddie Zuko",
        "Eli & Fur",
        "Erika de Casier",
        "Everything Always",
        "Faye Webster",
        "Feeble Little Horse",
        "Flight Facilities",
        "Flo",
        "Folamour",
        "Gesaffelstein",
        "Girl Ultra",
        "Gorgon City",
        "Grimes",
        "Hatsune Miko",
        "Hermanos Gutiérrez",
        "Ice Spice",
        "Innellea",
        "ISOxo & Knock2",
        "J Balvin",
        "The Japanese House",
        "Jhené Aiko",
        "Jjuujjuu",
        "Jockstrap",
        "John Summit",
        "Jon Batiste",
        "Joplyn",
        "Jungle",
        "Justice",
        "Ken Carson",
        "Kenya Grace",
        "Kevin Abstract",
        "Kevin de Vries x Kölsch",
        "Kevin Kaarl",
        "Keyspan",
        "Khruangbin",
        "Kimonos",
        "Kokoroko",
        "Lana Del Rey",
        "The Last Dinner Party",
        "Late Night Drive Home",
        "Latin Mafia",
        "Le Sserafim",
        "Lil Uzi Vert",
        "Lil Yachty",
        "L’Impératrice",
        "Lovejoy",
        "Ludmilla",
        "Mahmut Ohran",
        "Mall Grab",
        "Mandy, Indiana",
        "Maz",
        "Mdou Moctar",
        "Militarie Gun",
        "Miss Monique",
        "Narrow Head",
        "Nav",
        "Neil Frances",
        "No Doubt",
        "Olivia Dean",
        "Oneohtrix Point Never",
        "Orbital",
        "Palace",
        "Patrick Mason",
        "Peggy Gou",
        "Peso Pluma",
        "Purple Disco Machine",
        "Rainer Zonnweld",
        "Raye",
        "Rebüke",
        "The Red Pears",
        "Reneé Rapp",
        "The Rose",
        "Sabrina Carpenter",
        "Saint Levant",
        "Santa Fe Klan",
        "Sid Sriram",
        "Skepta",
        "Skin on Skin",
        "Skream & Benga",
        "Son Rompe Pera",
        "Spinall",
        "Steve Angello",
        "Sublime",
        "Suki Waterhouse",
        "Taking Back Sunday",
        "Tems",
        "Thuy",
        "Tinashe",
        "Tita Lau",
        "Two Shell",
        "Tyla",
        "Tyler, the Creator",
        "Upchuck",
        "Victoria Monét",
        "Will Clarke",
        "YG Marley",
        "Yoasobi",
        "Young Fathers",
        "Young Miko",
        "88rising Futures"]


# access tokens are only valid for one hour
token = get_token()
fields = ["name","id","genres","popularity","followers","external_urls","href","images","type","uri"]

with open("lineup.csv","w",newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fields)

    for artist in lineup:
        result = search_for_artist(token, artist)
        rows = [result["name"],result["id"],result["genres"],result["popularity"],result["followers"],
                result["external_urls"],result["href"],result["images"],result["type"],result["uri"]]
        writer.writerow(rows)
