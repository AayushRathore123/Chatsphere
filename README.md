# Chatsphere
This project is a web based application on Django framework. Chatsphere is a web app designed to facilitate online discussions and debates. 

+ Users have to login to create a room or join one.
+ User can create a profile, if not already having an account, and this profile information in stored in sqlite3 database.
+ Users can search for existing rooms and start discussing
+ Users can create a room of their own and can edit or delete it.
+ Users can browse all the rooms based on a certain topic in the "Browse Topics" section.
+ Users can see the most recent activities on the site like who messaged in which room and what was the message in the "Recent Activities" section.
+ Users can view their or other's profile.
+ Users can enter details and schedule a meeting
+ Users can see all the scheduled meet

## Getting Started
### Environment Development
In the project directory-
+ Open Terminal
  + pip install virtualenv
  + virtualenv envname
  + Get-ExecutionPolicy
     - if restricted, then 
     - Set-ExecutionPolicy -ExecutionPolicy Unr
     - set-executionpolicy remotesigned
  + envname\scripts\activate
  + pip install -r requirements.txt
  + python manage.py runserver
#### <br/> open http://127.0.0.1:8000/ to see it in your browser

## Screenshots
Home page
![minor2 1](https://github.com/AayushRathore123/Chatsphere/assets/110801658/1c17367a-9c44-4f18-99bf-18d92124a579)

Login Page
![minor2 2](https://github.com/AayushRathore123/Chatsphere/assets/110801658/97be3b53-5651-4914-b98f-b8c3509e4e95)

After login, user is able to see recent activities of the room he/she has joined
![minor2 5](https://github.com/AayushRathore123/Chatsphere/assets/110801658/ff203dcd-bc3b-427e-9ddc-c09454137b1d)

User can browse rooms on the basis of topics
![minor2 8](https://github.com/AayushRathore123/Chatsphere/assets/110801658/f43a81ff-0904-471a-a539-c89c804a4128)

User can create its own room
![minor2 4](https://github.com/AayushRathore123/Chatsphere/assets/110801658/a7b2ad9b-b766-4606-9a4e-c4639db45cea)

User can start discussion
![minor2 11](https://github.com/AayushRathore123/Chatsphere/assets/110801658/4d5dad81-4aa4-4c30-acd1-20205d6e4b4c)

User can see all the scheduled meet
![minor2 6](https://github.com/AayushRathore123/Chatsphere/assets/110801658/44d084d5-5b0f-4f48-8d0c-5dde89abf51f)

User can enter details and schedule a meeting
![minor2 7](https://github.com/AayushRathore123/Chatsphere/assets/110801658/8c0a4a95-62c6-409e-82d9-070309dc90b6)

User's Profile page
![minor2 10](https://github.com/AayushRathore123/Chatsphere/assets/110801658/9bb3cfe1-6300-4e89-a8fb-4894a79b1bec)

User can edit his/her profile
![minor2 9](https://github.com/AayushRathore123/Chatsphere/assets/110801658/a6b8dfae-d308-4793-938c-37a4f0c954a7)

## Learn More
To learn more about tools and technologies, you can refer this following resources:
+ [SQLite3](https://www.sqlite.org/index.html)
+ [Python](https://www.python.org/)
+ [Django](https://www.djangoproject.com/)



