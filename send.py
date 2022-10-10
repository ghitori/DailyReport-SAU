import requests
import json
import config


def get_other():
    location = config.get_conf("location")
    if location["latitude"] and location["longitude"]:
        post_message = {}
        post_message.update(config.get_conf("userinfo"))
        post_message.update(location)
        if not post_message["latitude"]:
            post_message["latitude"] = 15
    else:
        return False

    res = requests.post(get_other_url, json.dumps(post_message))
    if res.status_code != 200:
        return False
    try:
        other = json.loads(res.text)
    except:
        return False
    return other


def report(report):
    res = requests.post(report_url, json.dumps(report))
    body = json.loads(res.text)
    if res.status_code != 200 or body["status"] != "OK":
        return False
    return True


report_system_url = "https://yqdwxx.sau.edu.cn/"
get_other_url = f"{report_system_url}YQDLWZ"
report_url = f"{report_system_url}ADDJKTB"
