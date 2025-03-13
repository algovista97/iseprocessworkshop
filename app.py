from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)
app.secret_key = "abc"

# Database connection function
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='computermysql',
        database='demodb',  # ✅ Ensure this database exists!
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/register', methods=['POST'])  
def register():
    name = request.form.get('name')
    email = request.form.get('email')
    mobile = request.form.get('mobile')
    password = request.form.get('password')
    
    print(f"Received: {name}, {email}, {mobile}, {password}")  # ✅ Debugging

    connection = get_db_connection()
    
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO users (name, email, mobile, password) VALUES (%s, %s, %s, %s)"  
            cursor.execute(sql, (name, email, mobile, password))  
        connection.commit()
        flash('Registration successful!', 'success')

    except Exception as e:
        flash(f"Error: {e}", 'danger')
        print(f"Database Error: {e}")  # ✅ Debugging error

    finally:
        connection.close()
    
    return redirect(url_for('signup'))

if __name__ == '__main__':
    print("Server running at: http://127.0.0.1:5000/")
    app.run(debug=True)
