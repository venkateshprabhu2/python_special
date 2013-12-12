import sys
import urllib
import urllib2
import time
import datetime
import json
import webbrowser
import requests
ACCESS_URL = "https://graph.facebook.com/"
def main1():
    k=0	
    webbrowser.open("https://www.facebook.com/dialog/oauth?"
                    "response_type=token&client_id=145634995501895&"
                    "redirect_uri=http://developers.facebook.com/tools/"
                    "explorer/callback&scope=user_birthday,user_friends,publish_actions"
                    ",read_stream")
    webbrowser.open("http://developers.facebook.com/tools/explorer")
    ACCESS_TOKEN = raw_input("\nEnter the TOKEN string obtained from API "
                           "explorer page: \n")
    print "\n\n\n"
    print "-----------------------------------------------------------------------------------------------------------------------------------------------------------"
    print " # Downloading Images from Facebook # "
    print "\n \n"
    while(k<10):
       l=""
       datafile = urllib2.urlopen(ACCESS_URL + 'me?fields=friends.fields(picture)&access_token='+ACCESS_TOKEN)
       g=json.loads(datafile.read())['friends']['data'][k]['picture']['data']['url']
       datafile.close()
       datafilee = urllib2.urlopen(ACCESS_URL + 'me?fields=friends&access_token='+ACCESS_TOKEN)	 
       m=json.loads(datafilee.read())['friends']['data'][k]['name']
       datafilee.close()      
       urllib.urlretrieve(g,"%s.jpg"%m)
       l="Downloading the profile picture of "
       l+=" %25s"%m
       l+="                %s "%g
       print l
       k=k+1       
    raw_input("")   
if __name__ == "__main__":
   main1()   
