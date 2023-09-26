from flask import Flask, request, render_template, redirect, jsonify
from waitress import serve
from connect_database import select_database, execute_database
app = Flask(__name__)

sport = [
    "basketball",
    "Walk",
    "swim"
]


# home
@app.route('/')
def home_regisert():
    return render_template("index.html", sports = sport)

# success
@app.route('/register', methods = ["POST"])
def register():
    name = request.form.get("name")
    if not name:
        return redirect('/fault')
    sp = request.form.get("Sport")
    if sp is None or sp not in sport:
        return redirect('/fault')
    sqllite = "insert into register values ( ? , ? )"
    execute_database(sqllite, (name,sp))
    return render_template("success.html")

# list of registants
@app.route('/registants')
def registants():
    list_registants = select_database("select * from register")
    return render_template("register.html", register = list_registants)

# delete list
@app.route("/informdelete")
def delete_list():
    execute_database("delete from register")
    return render_template("delete_list.html")

# falut
@app.route("/fault")
def display_fauls():
    return render_template("fault.html")

# delete one registant
@app.route("/delete_one_registrant", methods = ["POST"])
def delete_one_person():
    name = request.form.get("name")
    execute_database("delete from register where name = ? ",(name,))
    return redirect("/registants")

# search
@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/tool_search")
def tool_search():
    name = request.args.get("name")
    if not name:
        list_name = []
    else:
        list_name = select_database("select * from register where name like (?) ", ("%" +name+"%",))
    json_data = jsonify(list_name)
    return json_data

mode = 'dev'
if __name__ == '__main__':
    if mode == 'dev':
        app.run(host= '0.0.0.0', port = 50100, debug = True)
    else:
        serve(app,host= '0.0.0.0', port = 50100, Threads = 2)