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

def wxpusher(apptoken, content, summary, uids):
    url = "http://wxpusher.zjiecode.com/api/send/message"
    header = {'content-type': 'application/json'}
    j = {
        "appToken": apptoken,
        "content": content,
        "summary": summary,  # 消息摘要，显示在微信聊天页面或者模版消息卡片上，限制长度100，可以不传，不传默认截取content前面的内容。
        "contentType": 1,  # 内容类型 1表示文字  2表示html(只发送body标签内部的数据即可，不包括body标签) 3表示markdown
        # "topicIds": [  # 发送目标的topicId，是一个数组！！！，也就是群发，使用uids单发的时候， 可以不传。
        #     123
        # ],
        "uids": [  # 发送目标的UID，是一个数组。注意uids和topicIds可以同时填写，也可以只填写一个。
            uids
        ],
        # "url": "http://wxpusher.zjiecode.com",  # 原文链接，可选参数
        "verifyPay": False  # 是否验证订阅时间，true表示只推送给付费订阅用户，false表示推送的时候，不验证付费，不验证用户订阅到期时间，用户订阅过期了，也能收到。
    }

    r = requests.post(url, headers=header, json=j)

    return r
