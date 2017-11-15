# restful 优点
* 轻量，不需要额外的协议，http method 本身有语义
* 面向资源，自解释性


# 为什么前后端分离
* pc，app，pad 多端适应
* SPA 开发流行
* 前后端开发职责不清
* 开发效率
* 模板与后端语言耦合

# 前后端分离的缺点
* 学习门槛增加
* 文档重要性增加
* SEO难度增加

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
