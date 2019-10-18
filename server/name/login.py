from flask import request, jsonify
import bcrypt
from name import app
from name import conn

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    # salt = bcrypt.gensalt()

    # encryptedPassword = bcrypt.hashpw(password.encode('utf-8'), salt)
    # print(encryptedPassword)
    cursor = conn.cursor()
    row_count = cursor.execute("SELECT * from user_db WHERE id = %s", username)
    
    if row_count > 0:
        result = cursor.fetchall()
        for r in result:
            if(r[1] == password):
                return jsonify(data), 200
            else:
                return jsonify(''), 401
    else:
        return jsonify(''), 401
        