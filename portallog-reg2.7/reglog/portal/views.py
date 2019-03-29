from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse 
from django.views.generic import TemplateView 
# Create your views here.
class HomePageView(TemplateView): 
     def get(self, request, **kwargs): 
 	 
         return render(request, 'index.html', context=None) 

class login(TemplateView): 
     def get(self, request, **kwargs): 
          
         return render(request, 'login.html', context=None) 

def load(request):
     return render(request, 'load.html', context=None)

class reg(TemplateView): 
     def get(self, request, **kwargs): 
          
         return render(request, 'reg.html', context=None)

class jdata(TemplateView): 
     def get(self, request, **kwargs): 
          
         return render(request, 'json.json', context=None)
def register(request):
    import mysql.connector
    from passlib.hash import sha256_crypt
    uname= request.GET.get('name')
    umobile= request.GET.get('mobile')
    uemail= request.GET.get('email')
    upasswd= request.GET.get('passwd')
    ucpasswd= request.GET.get('cpasswd')
    if(upasswd == ucpasswd):
        mydb = mysql.connector.connect(
        host="localhost",
        user="dbuser",
        passwd="Vivmishra3678 @ 8750824959MMLP",
        database="user_db"
        )
        password = sha256_crypt.encrypt(upasswd)
        mycursor = mydb.cursor()
        try:
           sql = "INSERT INTO user VALUES (%s, %s, %s, %s)"
           val = (uname, umobile, uemail, password)
           mycursor.execute(sql, val)
        
           mydb.commit()
        except mysql.connector.IntegrityError as err:
             html = """<html><head><script>
var redirect = function() {
  if (confirm("Email already exists")) {
      window.location.href="http://18.188.166.163:3678/portal/registration/";
   }
}
</script></head><body onLoad="redirect()">
</body></html>"""
             return HttpResponse(html)
 
        return render(request, 'login.html', context=None)
    else:
        html = """<html><head><script>
var redirect = function() {
  if (confirm("Password does not match")) {
      window.location.href="http://18.188.166.163:3678/portal/registration/";
   }
}
</script></head><body onLoad="redirect()">
</body></html>"""
        return HttpResponse(html)


def logging(request):
   import mysql.connector
   from passlib.hash import sha256_crypt 
   uemail= request.GET.get('email')
   upasswd=request.GET.get('passwd')
   mydb = mysql.connector.connect(
   host="localhost",
   user="dbuser",
   passwd="Vivmishra3678 @ 8750824959MMLP",
   database="user_db"
   )
   mycursor = mydb.cursor()
   mycursor.execute("SELECT passwd FROM user where email=%s",[uemail])
   myresult = mycursor.fetchall()
   tup1=myresult[0]
   verify = sha256_crypt.verify(upasswd, tup1[0])
   if(verify == True):
     return HttpResponse('Welcome user {}'.format(uemail))
   else:
     html = """<html><head><script>
var redirect = function() {
  if (confirm("Incorrect username or password")) {
      window.location.href="http://18.188.166.163:3678/portal/login/";
   }
}
</script></head><body onLoad="redirect()">
</body></html>"""
     return HttpResponse(html)











