import os

from flask import Flask


def create_app(test_config=None):
    # 创建并配置应用
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'webpy.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)

    # 保证实例所在的文件夹的存在
    try:
        os.mkdir(app.instance_path)
    except OSError:
        pass

    # 简单主页
    @app.route('/')
    def index():
        return 'Index Page'

    # 一个简单的欢迎页面
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app
