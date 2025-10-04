import os
import sys

os.environ['LANG'] = 'en_US.UTF-8'

sys.dont_write_bytecode = True

class Config:
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'ajax-db-server.mysql.database.azure.com')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'maria')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'Maria123')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'ajax_systems')
    MYSQL_PORT = 3306
