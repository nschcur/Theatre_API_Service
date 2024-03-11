# Theatre_API_Service

## Installing using GitHub

### Install PostgreSQL and create db

*Clone project from [GitHub](https://github.com/nschcur/Theatre_API_Service)*

git clone https://github.com/nschcur/Theatre_API_Service.git

> ### *Windows PowerShell / Mac Terminal*
> python -m venv venv
> 
> venv\Scripts\activate (Windows PowerShell)
> 
> sourse venv\bin\activate (Mac Terminal)
> 
> pip install -r requirements.txt
> 
> set DB_NAME=your db name
> 
> set DB_HOST=your db hostname 
> 
> set DB_USER=your db username
> 
> set DB_PASSWORD=your db user password
> 
> set SECRET_KEY=your secret key
> 
> python manage.py migrate
> 
> python manage.py runserver


> ### *Run with Docker*
> 
> Docker should be installed
> 
> docker-compose build
> 
> docker-compose up


> ### *Getting access*
> 
> Endpoint to create user:
> - api/user/register
> 
> Endpoints to get access token:
> - api/user/token
> - api/user/token/refresh
> - api/user/token/verify


> ### *Features*
> 
> JWT authenticated
> 
> Admin panel/admin/
> 
> Documentation is located:
> - api/doc/swagger/