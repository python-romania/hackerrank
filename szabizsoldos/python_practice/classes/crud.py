import mysql.connector
from mysql.connector import errorcode
import datetime

config = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'employees',
  'raise_on_warnings': True
}

DB_NAME = 'employees'

TABLES = {}
TABLES['employees'] = (
    "CREATE TABLE `employees` ("
    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ") ENGINE=InnoDB")

TABLES['departments'] = (
    "CREATE TABLE `departments` ("
    "  `dept_no` char(4) NOT NULL,"
    "  `dept_name` varchar(40) NOT NULL,"
    "  PRIMARY KEY (`dept_no`), UNIQUE KEY `dept_name` (`dept_name`)"
    ") ENGINE=InnoDB")

TABLES['salaries'] = (
    "CREATE TABLE `salaries` ("
    "  `emp_no` int(11) NOT NULL,"
    "  `salary` int(11) NOT NULL,"
    "  `from_date` date NOT NULL,"
    "  `to_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`,`from_date`), KEY `emp_no` (`emp_no`),"
    "  CONSTRAINT `salaries_ibfk_1` FOREIGN KEY (`emp_no`) "
    "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['dept_emp'] = (
    "CREATE TABLE `dept_emp` ("
    "  `emp_no` int(11) NOT NULL,"
    "  `dept_no` char(4) NOT NULL,"
    "  `from_date` date NOT NULL,"
    "  `to_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`,`dept_no`), KEY `emp_no` (`emp_no`),"
    "  KEY `dept_no` (`dept_no`),"
    "  CONSTRAINT `dept_emp_ibfk_1` FOREIGN KEY (`emp_no`) "
    "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
    "  CONSTRAINT `dept_emp_ibfk_2` FOREIGN KEY (`dept_no`) "
    "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['dept_manager'] = (
    "  CREATE TABLE `dept_manager` ("
    "  `dept_no` char(4) NOT NULL,"
    "  `emp_no` int(11) NOT NULL,"
    "  `from_date` date NOT NULL,"
    "  `to_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`,`dept_no`),"
    "  KEY `emp_no` (`emp_no`),"
    "  KEY `dept_no` (`dept_no`),"
    "  CONSTRAINT `dept_manager_ibfk_1` FOREIGN KEY (`emp_no`) "
    "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
    "  CONSTRAINT `dept_manager_ibfk_2` FOREIGN KEY (`dept_no`) "
    "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['titles'] = (
    "CREATE TABLE `titles` ("
    "  `emp_no` int(11) NOT NULL,"
    "  `title` varchar(50) NOT NULL,"
    "  `from_date` date NOT NULL,"
    "  `to_date` date DEFAULT NULL,"
    "  PRIMARY KEY (`emp_no`,`title`,`from_date`), KEY `emp_no` (`emp_no`),"
    "  CONSTRAINT `titles_ibfk_1` FOREIGN KEY (`emp_no`)"
    "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

class CustomDb():
    def db_connect(self):
        cnx = mysql.connector.connect(**config)
        return cnx

    def create_database(self, cursor_):
        try:
            cursor_.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

    def create_tables(self, cursor_, cnx_):
        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
                print("Creating table {}: ".format(table_name), end='')
                cursor_.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")

        cursor_.close()
        cnx_.close()

    def init_tables(self):
        cnx = self.db_connect()
        cursor = cnx.cursor()

        try:
            cursor.execute("USE {}".format(DB_NAME))
            self.create_tables(cursor, cnx)
        except mysql.connector.Error as err:
            print("Database {} does not exists.".format(DB_NAME))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.create_database(cursor)
                print("Database {} created successfully.".format(DB_NAME))
                cnx.database = DB_NAME
                self.create_tables(cursor, cnx)
            else:
                print(err)
                exit(1)

    def db_close(self, cnx_):
        cnx_.close()

    def salaries_by_year(self):
        cnx = self.db_connect()
        cursor = cnx.cursor()

        query = ("SELECT SUM(salary) as `salary_sum`, COUNT(*) as `total_salaries_count`, YEAR(from_date) as `salary_year` FROM salaries WHERE YEAR(from_date) = %s")
        year = 2000

        cursor.execute(query, [year])

        for (salary_sum, total_salaries_count, salary_year) in cursor:
            print("A total of {} USD, from {} total salaries count in {}.".format(salary_sum, total_salaries_count, salary_year))
        cursor.close()
        cnx.close()

    def total_employees_by_gender(self):
        total_employees = 0
        cnx = self.db_connect()
        cursor = cnx.cursor()
        cursor_total = cnx.cursor()

        query_total = ("SELECT COUNT(*) as `total_gender_count` FROM employees")
        cursor_total.execute(query_total)

        for (total_gender_count) in cursor_total.fetchone():
            total_employees += total_gender_count

        query = ("SELECT gender, COUNT(*) as `gender_count` FROM employees GROUP BY gender")
        cursor.execute(query)

        for (gender, gender_count) in cursor:

            percent = gender_count * 100 / total_gender_count

            if gender == 'M':
                gender = 'Male'
            if gender == 'F':
                gender = 'Female'

            print('Total of {} {} employees, that is {}% of total({:1,.0f}) employees.'.format(gender, gender_count, round(percent, 2), total_gender_count))

db = CustomDb()
db.salaries_by_year()
db.total_employees_by_gender()
