Supermarket Management System

1 -> py -3.8 -m venv sms-mth-venv

2 -> .\sms-mth-venv\Scripts\activate

3 -> python -m pip install django==2

4 -> python -m django startproject sms

5 -> python manage.py runserver

6 -> create DB 

7 -> connect DB (setting.py) 

'default': { 
 'ENGINE': 'django.db.backends.mysql', 
 'NAME': 'sms_mthdb', 
 'USER': 'root', 
 'PASSWORD': '', 
 'HOST': 'localhost', 
 'PORT': '3306' 
 } 

8 -> python manage.py migrate

9 -> [If Error] did u install mysql client?

[Type this] python -m pip install mysqlclient

10 ->  python manage.py createsuperuser

Username : admin
Email : admin@gmail.com
Password : superuser

11 -> localhost:8000/admin/

12 -> python manage.py startapp sms_employees

--------------------------------------------

python manage.py migrate

python manage.py makemigrations sms_employees

python -m pip install django-bootstrap4

python -m pip install django-bootstrap4==0.0.8

python -m pip install django-braces==1.13.0

<div
    class="p-5 text-center bg-image"
    style="
      background-image: url('https://images.alphacoders.com/752/752588.png');
      height: 400px;
      margin-top: 2px;
    "
  >
    <div class="mask" style="background-color: rgba(0, 0, 0, .5);">
      <div class="d-flex justify-content-center align-items-center h-100">
        <div class="text-white">
          <h1 class="mb-3">Create Employees</h1>
          <h4 class="mb-3">You are here at adding new employee</h4>
          <a class="btn btn-outline-light btn-lg" href="javascript:history.back()" role="button">Back to List</a>
        </div>
      </div>
    </div>
  </div>
