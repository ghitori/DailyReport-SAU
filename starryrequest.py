import requests



def sreq( url, headers, type, data, cookie):
    if headers :
        if type == "get" :
            r = requests.get(url , headers=headers, cookies=cookie)
        elif type == "json" :
            r = requests.post(url, json=data , headers=headers, cookies=cookie)
        elif type == "data" :
            r = requests.post(url, data=data , headers=headers, cookies=cookie)
    else :
        if type == "get" :
            r = requests.get(url, cookies=cookie)
        elif type == "json" :
            r = requests.post(url, json=data, cookies=cookie)
        elif type == "data" :
            r = requests.post(url, data=data, cookies=cookie)
    return r

def pushdeer( server, pushkey, text, desp):
    if server == "":
        server = "https://api2.pushdeer.com/"
    elif "https://" not in server :
        if "http://" not in server :
            server = "https://" + server
    if server[-1] != "/" :
        server = server + "/"
    message = {'pushkey' : pushkey,'text' : text,'desp' : desp}
    r = sreq( server + "message/push", "", "json", message,"")
    return r.status_code

 

