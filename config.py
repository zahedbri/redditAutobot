

#i used two database schemes under mysql.  Change this to one in the future


MYSQL_USERNAME = 'username'
MYSQL_PW = 'password'
MYSQL_SERVER = 'localhost:3307'

MYSQL_DBNAME11 = 'dbname1'
MYSQL_DBNAME12 = 'dbname2'

SQLALCHEMY_DATABASE_URI ="mysql+pymysql://{}:{}@{}/{}".format(MYSQL_USERNAME,
        MYSQL_PW, MYSQL_SERVER, MYSQL_DBNAME11)
SQLALCHEMY_DATABASE_URI_2 ="mysql+pymysql://{}:{}@{}/{}".format(MYSQL_USERNAME,
        MYSQL_PW, MYSQL_SERVER, MYSQL_DBNAME12)



#-------------------------------------------------------------#
customlog = '/home/logs/'
SQLALCHEMY_TRACK_MODIFICATIONS = False
