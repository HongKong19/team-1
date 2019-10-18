import pymysql
import pymysql.cursors

class DbHelper:
    def __init__(self):
        self.db_config = {'host':'root', 'user': 'user', 'password':'password', 'database':'example'}

    def login(self, username, password):
        try:
            conn = pymysql.connect(host=self.db_config['host'],
                                   user=self.db_config['user'],
                                   password=self.db_config['password'], database=self.db_config['dbname'])
            cur = conn.cursor()
            query = "select username, password from login where user_name='%s' and password='%s';" % (username, password)
            cur.execute(query)
            result = cur.fetchall()
            cur.close()
            if not result:
                return {'isAuth': False}
            else:
                if result[1] == password:
                    return {'isAuth': True}
            return {'isAuth': False}
        except Exception as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def sign_up(self,username,password, height, weight, bp, sugar, smoke, alcohol, foodpref ):
        conn = None
        try:
            conn = pymysql.connect(host=self.db_config['host'],
                                   user=self.db_config['user'],
                                   password=self.db_config['password'], database=self.db_config['dbname'])
            cur = conn.cursor()
            query = "insert into login (user_name,password) values('%s', '%s') " % (username, password)
            cur.execute(query)
            conn.commit()
            query = "INSERT INTO personal_info (height, weight, blood_pressure, blood_sugar,smoking, alocoholic, preferences) values ('%s', '%s', '%s','%s','%s','%s','%s');" % (height, weight, bp, sugar, smoke, alcohol, foodpref)
            cur.execute(query)
            conn.commit()
        except Exception as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
            self.disease_table(username)

    def suggestions(self, username):
        conn = None
        try:
            conn = pymysql.connect(host=self.db_config['host'],
                                   user=self.db_config['user'],
                                   password=self.db_config['password'], database=self.db_config['dbname'])
            cur = conn.cursor()
            query = "Select obesity, diabetes from disease where username = '%s' " % username
            cur.execute(query)

            result = cur.fetchone()
            res={'food':[],'exercise':[],'goal':[]}

            if result[0]:
                query = "select food,exercise,goal from suggestion where disease='obesity'"
                cur.execute(query)
                r = cur.fetchone()
                res['food'].append(r[0])
                res['exercise'].append(r[1])
                res['goal'].append(r[2])

            if result[1]:
                query = "select food,exercise,goal from suggestion where disease='diabetes'"
                cur.execute(query)
                r = cur.fetchone()
                res['food'].append(r[0])
                res['exercise'].append(r[1])
                res['goal'].append(r[2])

            return {"result":res}
        except Exception as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def schedule(self):
        conn = None
        try:
            conn = pymysql.connect(host=self.db_config['host'],
                                   user=self.db_config['user'],
                                   password=self.db_config['password'], database=self.db_config['dbname'])
            cur = conn.cursor()
            query = "select user_name from  appointment order by priority DESC;"
            cur.execute(query)
            return cur.fetchall()
        except Exception as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def appointment(self,username):
        conn = None
        try:
            conn = pymysql.connect(host=self.db_config['host'],
                                   user=self.db_config['user'],
                                   password=self.db_config['password'], database=self.db_config['dbname'])
            cur = conn.cursor()

            query = "select height,weight,blood_pressure from  personal_info where username='%s';" % username

            cur.execute(query)
            result = cur.fetchone()

            bmi = result[1] / result[0] ** 2

            if bmi >= 30:
                query = "insert into appointment (user_name,priority) values('%s', 70) " % username

            else:
                query = "insert into appointment (user_name,priority) values('%s', 10) " % username

            cur.execute(query)
            conn.commit()

        except Exception as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()



    def disease_table(self, username):
        conn = None
        try:
            conn = pymysql.connect(host=self.db_config['host'],
                                   user=self.db_config['user'],
                                   password=self.db_config['password'], database=self.db_config['dbname'])
            cur = conn.cursor()

            query = "select height,weight,blood_pressure from  personal_info where username='%s';" % username

            cur.execute(query)
            result = cur.fetchone()

            bmi = result[1]/result[0]**2

            if bmi >= 30:
                query = "insert into disease('obesity') values (1) where username='%s';" % username
            else:
                query = "insert into disease('obesity') values (0) where username='%s';" % username

            cur.execute(query)
            conn.commit()
            if result[2] >= 130:
                query = "insert into disease('diabetes') values (1) where username='%s';" % username
            else:
                query = "insert into disease('diabetes') values (0) where username='%s';" % username
            cur.execute(query)
            conn.commit()

        except Exception as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


