from doctest import debug

from flask import Flask,render_template,request,redirect,session,url_for
from flask_mysqldb import MySQL
import MySQLdb

app=Flask(__name__)
app.secret_key="12344321"
app.config["MYSQL_HOST"]="127.0.0.1"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="root"
app.config["MYSQL_DB"]="companyDet"
db=MySQL(app)

@app.route('/',methods=['GET','POST'])
def login():
    if request.method=="POST":
        if "username" in request.form and "empeid" in request.form and "empcmp" in request.form and "empeml" in request.form:
            global Name
            Name=request.form['username']
            global Employee_ID
            Employee_ID=request.form['empeid']
            global Company_Name
            Company_Name=request.form['empcmp']
            global Email
            Email=request.form['empeml']
            cur=db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("INSERT INTO companydet.companydetails(Name,Employee_ID,Company_Name,Email)VALUES(%s,%s,%s,%s)",(Name,Employee_ID,Company_Name,Email))
            db.connection.commit()
            return redirect(url_for('page2'))

    return render_template('login.html')

@app.route('/page2', methods=['GET'])
def page2():
    return render_template("page2.html",Name=Name,Eid=Employee_ID,Cname=Company_Name,Eml=Email)

if __name__=='__main__':
    app.run(debug==True)


