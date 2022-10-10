import toml
import os


def get_conf(table):
    value = conf[table]
    return value


def get_env(env):
    try:
        env_conf = toml.loads(os.environ[env])
    except:
        env_conf = False
    return env_conf


def load_conf():
    global conf
    conf = toml.load(conf_path)
    for env in env_list:
        env_conf = get_env(env)
        if env_conf:
            conf[env].update(env_conf)
            print(f"已从环境变量中读取【{env}】")
        else:
            print(f"已从配置文件中读取【{env}】")
    print("配置文件加载完成")


conf_path = "./config/config.toml"
env_list = ["userinfo", "location", "other"]
conf = ""
