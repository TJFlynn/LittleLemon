# LittleLemon
 
Static files are hosted at http://127.0.0.1:8000/api/restaurant/

In settings.py the name of the database, user, and password fields need to be updated to match your local mysql information.

If you already have a database called ‘restaurant’ drop and recreate it, then apply migrations.

Create a new super user of your choice and login with a POST at http://127.0.0.1:8000/auth/token/login/

using this as an example of the BODY in JSON format

{
    "username" : "your_super_admin",
    "password" : "your_password"
}

Use the token generated there for the remainder of the api tests.

The booking url is 127.0.0.1:8000/api/tables/

You can post to it with this format as the admin user:
{
    "name" : "Customer Name",
    "num_guests" : 3,
    "booking_date" : "2022-11-16"
}


The menu url is 127.0.0.1:8000/api/menu-items/

You can post to it with this format:
{
    "title" : "Ravioli",
    "price" : 10.99,
    "inventory" : 12
}
