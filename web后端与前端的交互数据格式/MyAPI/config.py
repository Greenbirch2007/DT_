
# 配置环境的基类
class Config(object):
    # 每次请求结束后，自动提交数据库中的变动，该字段在flask-sqlalchemy 2.0之后已经被删除了（有bug）

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


class DevelopmentConfig(Config):
    # 18
    # """
    # 19     配置文件中的所有的账号密码等敏感信息，应该避免出现在代码中，可以采用从环境变量中引用的方式，比如：
    # 20     username = os.environ.get('MYSQL_USER_NAME')
    # 21     password = os.environ.get('MYSQL_USER_PASSWORD')
    # 22
    # 23     本文为了便于理解，将用户信息直接写入了代码里
    DEBUG = True

    # 数据库URI
    # 28
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/cleven_development'

    # 也可如下来写，比较清晰
    31  # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{hostname}/{databasename}".format(username="xxxx", password="123456", hostname="172.17.180.2", databasename="cleven_development")

# 测试环境的配置
class TestingConfig(Config):
    TESTING = True
    QLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@172.17.180.3:3306/cleven_test'
    # 41
    # """
    # 42     测试环境也可以使用sqlite，默认指定为一个内存中的数据库，因为测试运行结束后无需保留任何数据
    # 43     也可使用  'sqlite://' + os.path.join(basedir, 'data.sqlite') ，指定完整默认数据库路径
    # 44     """
    # 45  # import os
    # 46  # basedir = os.path.abspath(os.path.dirname(__file__))
    # 47  # SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite://'
# 生产环境的配置

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@172.17.180.4:3306/cleven_production'
    config = {

    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'testing': TestingConfig,

    'default': DevelopmentConfig}