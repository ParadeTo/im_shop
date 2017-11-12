# migration
django_migrations 这张表记录了已执行过的命令

# 问题
* 使用pymysql
```python
__init__.py
import pymysql
pymysql.install_as_MySQLdb()
```

* python 包地址
www.lfd.uci.edu/~gohlke/pythonlibs/

* 创建innodb的表
settings.py

'OPTIONS': { 'init_command': 'SET default_storage_engine=INNODB' },
