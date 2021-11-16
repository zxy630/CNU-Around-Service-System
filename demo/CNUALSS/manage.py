from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import app, db
from app.import_data import ImportData

# 实例化Migrate，实现数据迁移
migrate = Migrate(app, db)
# 命令行解析
manager = Manager(app)
# 添加命令，替代migrate
manager.add_command('db', MigrateCommand)
manager.add_command('import_data', ImportData())

if __name__ == '__main__':
    manager.run()
    #db.create_all()

