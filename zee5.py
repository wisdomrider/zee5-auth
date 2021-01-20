from colorama.initialise import deinit
import requests, json
from requests.sessions import session
#import urllib.parse
from colorama import init, Fore, Back, Style
init()

def modified_url(value):
        if value == "drm":
            return "hls/"
        else:
            return "hls1/"

def zee5(official_link):
    
    session = requests.Session()


    official_link_trim = official_link.split("/")[-1]

    res = session.get("https://gwapi.zee5.com/content/details/"+ official_link_trim +"?translation=en&country=IN&version=2")
    res_json = json.loads(res.text)

    try:
        res_customization = res_json["video_details"]["hls_url"].split('/')
    except:
        print("\n")
        print(Fore.LIGHTRED_EX + "XXXX--Invalid Url or playlist provided!--XXXX")
        deinit()
        exit()

    hls_value = modified_url(res_customization[1])
    finalizing_link = "/".join(res_customization[2:])


    #res2 = session.get("https://useraction.zee5.com/token/platform_tokens.php?platform_name=web_app")
    #print(res2.text)   #prints the authorization token without any authorization.

    res3 = session.get("http://useraction.zee5.com/tokennd/")
    #print(res3.text)   #returns valid hmac token with timestamp
    res3_text = res3.json()
    video_token = res3_text["video_token"]
    print("\n")
    print(Fore.LIGHTGREEN_EX + "Authorized URL to stream:")
    link = "https://zee5vodnd.akamaized.net/" + hls_value + finalizing_link + video_token
    print(Fore.LIGHTBLUE_EX + link)
    print("\n")
    print(Fore.LIGHTRED_EX + 'Give damn credit to https://ttttt.me/believerseller Remember!!! ;)')
    print(Style.RESET_ALL)
    #print(urllib.parse.quote_plus(link))

def intro():
    info = """

    ====================================================================================
    |     !!! Provide movie or Episode URL only, not the playlist !!!                  |
    |                                                                                  | 
    |    Stream Online Open link https://www.hlsplayer.net                             |
    |                                                                                  | 
    |    For local media stream use any open source software as VLC, mpv and similar.  |
    |                                                                                  |
    |    Grab this link below to stream.                                               |
    ====================================================================================

    """

    print(Fore.LIGHTGREEN_EX + info)

    print(Fore.LIGHTBLUE_EX + "Enter official zee5 URL here:" )
    zee5(input())

while True:
    print(Fore.LIGHTWHITE_EX + "Press ENTER to Countinue or N to exit > ")
    x = input()
    if x == "":
        intro()
    else:
        exit()