from requests import Response
from sanic import Sanic
from sanic.response import json
from databse import db
from models import  User
from sqlalchemy import update
app = Sanic("my_app")

@app.route("/admin-users", methods=['POST'])
async def postingdata(request):
    Title = request.json.get('Title')
    FirstName =request.json.get('FirstName')
    LastName = request.json.get('LastName')
    Email = request.json.get('Email')
    Username = request.json.get('Username')
    DOB = request.json.get('DOB')
    user = User(Title = Title, FirstName = FirstName, LastName = LastName, Email = Email, Username = Username, DOB=DOB)
    db.add(user)
    db.commit()
    return json({'message': 'Record inserted successfully'})

 
@app.route("/admin-get", methods=['GET'])
async def get_students(request):
    try:
         users = db.query(User).all()
         user_list = [user.__dict__ for user in users]
         for user_data in user_list:
            user_data.pop('_sa_instance_state', None)
         return json(user_list)
    except Exception as e:
         print("Error:", e)
         return json({'error': 'Internal Server Error'}, status=500)


@app.route("/admin-update",methods=['PUT'])
async def update_students(request):
        db.query(User).filter(User.UserId == 19).update({"Title" : 'ManojDevarakonda'})
        db.commit()
        return json({'message': 'Record Updated successfully'})

@app.route("/admin-delete",methods={'DELETE'})
async def delete_students(request):
     db.query(User).filter(User.UserId == 2).delete()
     db.commit()
     return json({"message" : "Record Deleted Successfully !!!!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)