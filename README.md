# DailyReport-SAU    沈航每日疫情填报
~~只是一个会一点辣鸡代码的废宅不想日报罢了~~
### 2022.7.31
忽然发现不需要Cookies也能正常填报，目前需要抓包的只有个人UID（不知道哪来的，没有解决的头绪）
## 如何使用
### 
- **前置操作**
   1. 利用软件对`https://yqdwxx.sau.edu.cn/ADDJKTB`进行抓包，获取请求数据中的`"uid"`所对应的值（方法不提供）
   2. Clone本项目到本地，进入文件夹
   3. 打开`config.ini`，按照个人实际信息填写，填入刚刚获取的`"uid"`并保存，遇到问题可以参考[config.demo.ini](https://github.com/ShanshanHY/DailyReport-SAU/blob/main/config.demo.ini)
###  
- **本地运行（二选一）**
   1. 安装`python3`，并配置环境
   2. 运行`main.py`
###  
- **利用Github Actions云端定时运行（二选一&推荐）**
   1. 首先登陆Github账户，并且[Fork](https://github.com/ShanshanHY/DailyReport-SAU/fork)本项目到你的仓库
   2. 依次打开`Settings`-`Secrets`-`Actions`-`New repository secret`![屏幕截图 2022-08-05 074444](https://user-images.githubusercontent.com/29966961/182973743-8ad295bb-a220-4487-b0fc-8b5a9873e097.png)
   3. 在`Name`栏中填入`CONFIG`,复制前面提到的`config.ini`中的全部内容并粘贴到`Value`中并保存![屏幕截图 2022-08-05 075140](https://user-images.githubusercontent.com/29966961/182974144-eb353697-df5b-4d3e-9b99-304a8d1cc9c0.png)
   4. 打开`Actions`选项卡，并同意启用`Workflows`![image](https://user-images.githubusercontent.com/29966961/182974440-b6c46243-8214-4b66-9893-80b7f3b7a8b3.png)
   5. 依次点击`Daily Report`-`Run workflow`-`Run workflow`测试填报是否正常![image](https://user-images.githubusercontent.com/29966961/182975156-50c6d79d-fb72-4c8f-bcd7-ed3a1f426b65.png)
   6. 若出现异常，请确保`pushkey`正确填写，并前往`PushDeer`检查填报内容
   7. Github Actions会自动在每日的`凌晨00：05`自动运行
###  
- **如果遇到任何问题，可以通过issue向我提出**
### 本人不对使用此脚本造成的任何后果负责！！！
