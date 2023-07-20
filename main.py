from sanic import Sanic
from sanic.response import text
from sanic import response

app = Sanic(__name__)
in_memory_student_db = [
  {
      "name" :"Manoj Kumar",
       "dept":"Front End Developer",
       "empId":124,
       "friends" :[
      "your friend A",
      "your friend B",
      "your friend C",
      "your friend D",
      "your friend E",
  ]
  },
   {
      "name" :"Prabath",
       "dept":"Front End Developer",
       "empId":119,
       "friends" :[
      "your friend A",
      "your friend B",
      "your friend C",
      "your friend D",
      "your friend E",
  ]
  }, 
  {
      "name" :"pooja",
       "dept":"Front End Developer",
       "empId":129,
       "friends" :[
      "your friend A",
      "your friend B",
      "your friend C",
      "your friend D",
      "your friend E",
  ]
  }
]
@app.get("/")
async def get_student(request):
    return response.json (in_memory_student_db)

@app.post("/")
async def post_student(request):
    student = request.json
    in_memory_student_db.append(student)
    return response.json(student)
@app.put("/")
async def put_student(request,id) :
    student = request.json
    in_memory_student_db[id] = student 
    return response.json(student)

@app.delete("/<id_:int>")
async def delete_student(request,id_):
    del in_memory_student_db[id_]
    return response.json({"message":"Deleted student successfully"})

if __name__ == "__main__" :
    app.run(host="0.0.0.0", port=8000, debug=True, auto_reload=True)


