import random
import time
import send
import config


def make_report():
    for table in report_list:
        report.update(config.get_conf(table))
    other = send.get_other(config.get_conf("location"))
    if other:
        report.update(other)
        global location_statue
        location_statue = True
    return


def set_temperature():
    conf_daily = config.get_conf("daily")
    for i in temperature_list:
        if not conf_daily[i]:
            report[i] = random_temperature()
        elif str(conf_daily[i]) == "0":
            if i == "tiwen":
                report[i] = random_temperature()
            else:
                report[i] = ('%.1f' % int(conf_daily[i]))
    return


def random_temperature():
    temperature_range = config.get_conf("temperature")
    temperature = random.randint(
        temperature_range["min"] * 10, temperature_range["max"] * 10) / 10
    if temperature <= 36.0:
        return "0.0-36.0"
    elif temperature >= 37.4:
        print("警告！当前随机体温过高，请确保配置文件填写正确！")
        return "37.4-40.0"     # 不会真有人被判定进了这里吧？
    else:
        return ('%.1f' % temperature)


def leave_shen_set():
    if report["chengshi"] == "沈阳市":
        report["sfls"] = "否"
    else:
        report["sfls"] = "是"
        city = config.get_conf("others", "lsqx")
        if city:
            report["lsqx"] = city
        else:
            report["lsqx"] = report["chengshi"]


def check_conf_integrity():
    requests_list = list(report.keys())
    requests_list.remove("other")
    requests_list.remove("lsqx")
    for key in requests_list:
        if not report[key]:
            print(f"缺少有效的值【{key}】，请检查配置文件后重试！")
            exit(1)
    for key in yn_list:
        if report[key] != "是" and report[key] != "否":
            print(f"配置文件内【{key}】的值只允许为“是”/“否”，请修改配置文件")
            exit(1)


def start_report():
    sleep_time = 10
    try_times = config.get_conf("settings")["try_times"]
    for times in range(1, try_times + 1):
        print(f"正在尝试第{times}次填报")
        if send.report(report):
            print(
                f'【{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}】填报成功!具体信息请前往推送工具查看')
            return True
        if times < try_times:
            print(
                f'【{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}】填报失败！将于 {sleep_time} 分钟后再次尝试')
            time.sleep(sleep_time * 60)
            sleep_time = sleep_time + 20
        print(f'【{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}】填报失败！\n请检查填报信息后再次尝试！若仍无法填报请前往Github进行反馈！')
    return False


conf_path = "./config/config.toml"
report_list = ["userinfo", "daily", "other"]
temperature_list = ["tiwen", "tiwen1", "tiwen2"]
yn_list = ["ljsjcs", "sqsb", "sfgl", "sfys", "sffr", "sfls"]
report = {}
location_statue = False
print("初始化成功")


if __name__ == "__main__":
    config.load_conf()
    make_report()
    set_temperature()
    leave_shen_set()
    check_conf_integrity()
    report_result = start_report()
    # if report_result:
        # push_success()
    # else:
        # push_fail()
