import starryrequest as req
import json
import configparser
import random

# 加载配置文件
file = 'config.ini'
con = configparser.ConfigParser()
con.read(file, encoding='utf-8')
body = dict(con.items('Info'))
# cookies = dict(con.items('Cookies'))
temp = dict(con.items('Temp'))['temp']
temp = temp.split(',')
pushkey = dict(con.items('Push'))['pushkey']

# 随机体温
if not body['tiwen']:
        body['tiwen'] = random.choice(temp).strip()
if not body['tiwen1']:
        body['tiwen1'] = random.choice(temp).strip()
if not body['tiwen2']:
        body['tiwen2'] = random.choice(temp).strip()

# 发送日报信息
url = "https://yqdwxx.sau.edu.cn/"
res = req.sreq( f'{url}ADDJKTB', "", 'json', body, '')

#推送通知
pushbody = f'学工号: {body["userid"]}\n姓名: {body["xingming"]}\n手机号: {body["shoujihao"]}\n单位院系: {body["dwyx"]}\n当前所在省份: {body["shengfen"]}\n所在城市: {body["chengshi"]}\n14日内是否有中高风险地区旅居史、接触史: {body["ljsjcs"]}\n是否按照要求向学校、社区及时上报: {body["sqsb"]}\n是否离沈: {body["sfls"]}\n离沈去向: {body["lsqx"]}\n是否隔离观察: {body["sfgl"]}\n是否身体有疑似典型症状: {body["sfys"]}\n是否发热: {body["sffr"]}\n其他信息: {body["other"]}\n体温(早): {body["tiwen"]}\n体温(中): {body["tiwen1"]}\n体温(晚): {body["tiwen2"]}'
code = res.status_code
if code == 200:
        resbody = json.loads(res.text)
        if resbody['status'] == 'OK':
                pushmessage = ["疫情填报成功！", f"**填报信息**\n---\n```\n{pushbody}\n```"]
                exit_code = 0
        else:
                pushmessage = ["疫情填报失败！", f"**请检查配置并手动填报！**\n\n**服务器返回信息：{res.text}**\n\n**填报信息**\n---\n```\n{pushbody}\n```"]
                exit_code = -1
else:
        pushmessage = ["疫情填报失败！服务器连接错误！", "**请检查服务器地址！**"]
        exit_code = -1
print(pushmessage[0],'\n',res.text)
req.pushdeer('', pushkey, pushmessage[0], pushmessage[1])
exit(exit_code)
