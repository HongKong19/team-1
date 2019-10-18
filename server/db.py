import mysql.connector

mydb = mysql.connector.connect(
  host="localForProjects",
  user="root",
  passwd="password12"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE HIAdatabase")

mycursor.execute("CREATE TABLE login ("
                 "user_name VARCHAR, "
                 "password VARCHAR,"
                 "PRIMARY KEY(user_name))")

mycursor.execute("CREATE TABLE personal_info ("
                 "user_name VARCHAR, "
                 "height FLOAT, "
                 "weight FLOAT,"
                 "blood_pressure INT,"
                 "blood_sugar INT,"
                 "smoking TINYINT(1)," #boolean
                 "alcoholic TINYINT(1),"
                 "point INT,"
                 "FOREIGN KEY (user_name) REFERENCES login(user_name),"
                 "PRIMARY KEY (user_name))")

mycursor.execute("CREATE TABLE disease ("
                 "user_name VARCHAR, "
                 "obesity TINYINT(1), "
                 "diabetes TINYINT(1),"
                 "FOREIGN KEY (user_name) REFERENCES login(user_name),"
                 "PRIMARY KEY (user_name))")

mycursor.execute("CREATE TABLE suggestion ("
                 "disease VARCHAR, "
                 "food VARCHAR, "
                 "exercise VARCHAR,"
                 "goal VARCHAR,"
                 "PRIMARY KEY (disease))")


mycursor.execute("CREATE TABLE appointment ("
                 "user_name VARCHAR(255), "
                 "priority INT, "
                 "PRIMARY KEY (user_name))")

#login
sql = "INSERT INTO login (user_name, password) VALUES (%s, %s)"
val = [
  ('Peter', '1234'),
  ('Amy', '2345'),
  ('Hannah', '3456')
]

mycursor.executemany(sql, val)

#personal_info
sql = "INSERT INTO personal_info (user_name, height, weight, blood_pressure," \
      "blood_sugar, smoking, alcoholic) VALUES (%s, %s)"
val = [
  ('Peter', '178', '80', '139', '120', '0', '0'), #high blood pressure, high blood sugar
  ('Amy', '163', '71', '101', '90', '1', '0'),
  ('Hannah', '157', '69', '99', '119', '0', '1') #high blood sugar
]
mycursor.executemany(sql, val)

#disease
sql = "INSERT INTO disease (user_name, obesity, diabetes) VALUES (%s, %s)"
val = [
  ('Peter', '1', '0'), #diabetes
  ('Amy', '0', '1'), #obesity
  ('Hannah', '0', '0') #both diabetes and obesity
]

mycursor.executemany(sql, val)

#suggestion
sql = "INSERT INTO suggestion (disease, food, exercise, goal) VALUES (%s, %s)"
val = [
    ('Obesity', 'less calories, more vegetables', 'run', 'walk 1km everyday'),
    ('Diabetes', 'less sugar, more yogurt', 'push-up', 'not eat sweet dessert for one week')
]

mycursor.executemany(sql, val)

#appointment
sql = "INSERT INTO appointment (user_name, priority) VALUES (%s, %s)"
val = [
  ('Peter', '89'),
  ('Amy', '45'),
  ('Hannah', '68')
]

mycursor.executemany(sql, val)