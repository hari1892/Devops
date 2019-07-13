#!/usr/bin/python3.5
import requests
import sys

urllist = sys.argv[1:]



def check_url():

    for url in urllist:
        try:
            r = requests.get(url)
            if r.status_code != "":
                print(url + '                    ' +    str(r.status_code))
        except Exception as e:
            print(str(url) +' ' +  '                                 ' +  str(e))
            pass

check_url()
