from flask import Flask, redirect, render_template, request
# import the class from friend.py
from user import Users


app = Flask(__name__)


# main page
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = Users.get_all()
    print(users)
    return render_template("index.html", all_users = Users.get_all())


# new user page
@app.route('/create_user')
def create_user():
    return render_template('create.html')

# new user saved
@app.route('/user_complete', methods=['Post'])
def user_saved():
    Users.create_user(request.form)
    return redirect ('/')


# edit display page
@app.route('/user_update/<int:id>')
def user_updated(id):
    data = {
        "id": id
    }
    return render_template('update.html', user = Users.single_user(data))


@app.route('/update_complete', methods=['POST'])
def update_complete():
    Users.update_user(request.form)
    return redirect ('/')



# delete
@app.route('/delete_user/<int:id>')
def delete_user(id):
    data = {
        "id":id
    }
    Users.delete_user(data)
    return redirect ('/') 



@app.route('/show_user/<int:id>')
def show(id):
    data ={
        "id":id
    }
    return render_template("show.html", user = Users.single_user(data))



if __name__ == "__main__":
    app.run(debug=True)