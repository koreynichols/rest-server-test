# rest-server-test

Django backend hosted on Heroku: https://korey-django-vehicle-test.herokuapp.com/

Test using postman:

### 1. Obtain auth token

To get auth token you can use a POST request to https://korey-django-vehicle-test.herokuapp.com/api/token/

username: admin

password: admin

![Screenshot 2021-03-07 235242](https://user-images.githubusercontent.com/26910936/110293362-52c57080-7fa3-11eb-8dfb-0a8c28ffccbb.png)

The result will give you 2 tokens. We will be using the access token

![Screenshot 2021-03-07 235323](https://user-images.githubusercontent.com/26910936/110293545-8f916780-7fa3-11eb-9ecb-c74700e87cd4.png)


### 2. Testing the api routes

In this we will go through a few of the api calls avaliable with the cars resource.

/cars GET\
/cars/:id GET\
/cars POST\
/cars/:id PUT\
/cars/:id DELETE

All of these can be appended to the end of https://korey-django-vehicle-test.herokuapp.com
They will all need the access token that we got in step 1.

The first one /cars GET request will return a list of the cars in the database. Under headers we will add a key/value pairing. The key will be 'Authorization' (no quotes) and the value will be 'Bearer' (again, no quotes) followed by a space and then the access token from step 1. All the api requests will require this key/value pairing

![Screenshot 2021-03-08 000748](https://user-images.githubusercontent.com/26910936/110294527-d3d13780-7fa4-11eb-8bc8-16b37079fed1.png)

When run the result should show a list of all the cars

![Screenshot 2021-03-08 000816](https://user-images.githubusercontent.com/26910936/110294635-f2cfc980-7fa4-11eb-8cde-eb7714491489.png)

/cars/:id is simular, but only returns a car with the matching id

/cars POST request will create a new car. We just need to add the information. To do this we will select the body tab and select form-data, then input the data using the kev/value pairings.

make - string\
model - string\
year - integer\
seats - integer\
color - string\
vin - string\
current_mileage - integer\
service_interval - integer\
next_service - date

![Screenshot 2021-03-08 000609](https://user-images.githubusercontent.com/26910936/110295464-fdd72980-7fa5-11eb-8fe2-c03cb05aefdd.png)

If successful, we will get a return of the new car

![Screenshot 2021-03-08 000628](https://user-images.githubusercontent.com/26910936/110295589-23643300-7fa6-11eb-81ec-35aad84de2fb.png)

/cars/:id PUT request is simular, but update an existing car\
/cars/:id DELETE request will delete listing of car with id chosen.

Trucks and Boats have the same api urls as cars.\
Truck model data needed will be:

make - string\
model - string\
year - integer\
seats - integer\
bed_length - integer\
color - string\
vin - string\
current_mileage - integer\
service_interval - integer\
next_service - date

Boat model data needed will be:

make - string\
model - string\
year - integer\
length - integer\
width - integer\
hin - string\
current_hours - integer\
service_interval - integer\
next_service - date
