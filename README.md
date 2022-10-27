# ELEC9609-Group10

# Welcome to MovieHub

This is a  booking system of Movie ticket.  This system can always provide ticket of the latest and hottest movie for you to enjoy.
You can choose to login in the system as different roles including Customer, staff and administrator in the home page.

![在这里插入图片描述](https://img-blog.csdnimg.cn/535ef6833d2b4f8b8007f60c51f5f3e4.png)
## Login as a Customer
In the login page you can input your user name and password to login the system. If you do not have an account, you can click the register button and create your own account!!!
Then you enter the home page of Customer, where you can check the number of movies, your orders, your notification as well as Personal Profile. And on the right side of your page you, the menu bar will help to find what you want quickly.
![在这里插入图片描述](https://img-blog.csdnimg.cn/dfa7f9fe568c4324955af5d65d9722ff.png)
##### Book your favorate movie
 In the movie booking page, you can find out what movies are showing and book the movie ticket. Click the "book" button and then choose the seat. 
![在这里插入图片描述](https://img-blog.csdnimg.cn/25b42d98d94e45c49824d43d454ff48e.png)
You can reserve up to four seats at a time. Be sure that you have **bind your bank account** in your Profile page before you pay the bill. And you can check the order in Order History.
![在这里插入图片描述](https://img-blog.csdnimg.cn/b3e1a05421af402f9b8ef0aae0b3ed4b.png)



## Login as an administrator
##### Insert a staff
As an administrator, you can not only check the staff list but can also insert new staff in your system.
 ![在这里插入图片描述](https://img-blog.csdnimg.cn/c60d06efe0fb4e6daf9c1eeba3dc756f.png)
The system will automatically create the staff account number and password. Please remember them, and the staff can change the password in Profile. 
##### Insert a movie
In the page of movie information Manangement you can find out what movie are showing and add new movie.
![在这里插入图片描述](https://img-blog.csdnimg.cn/597c551efee048a18e7820f5bcdc43ac.png)
You just need to need input the basic information including the name, duration, cast and so on, and then you can insert a new movie.<br>**Be careful: The maximum duration is 3 hours.**
![在这里插入图片描述](https://img-blog.csdnimg.cn/1ca75be014d1444bb5af9bb00ad1b6eb.png)






## Login as a Staff
As a staff, you can insert movie.

##### Release a new movie
In the release information page you can release a new session.![在这里插入图片描述](https://img-blog.csdnimg.cn/22c30581b29d4d1b822b77e1dd795710.png)
Before that, you need to **create a new room**. In the Room management page, you can insert the room id and room size, and then insert a new room.![在这里插入图片描述](https://img-blog.csdnimg.cn/6a48a03406684301bc8c402292e41ff6.png)
To release a new movie, just insert the movie name, room ID, price and release time.<br> **Be careful: Release Time cannot be previous time.  There can be no other films in the three hours before and three hours after the release of the film**
![在这里插入图片描述](https://img-blog.csdnimg.cn/c6893f8de7174497a3a44671da09e20e.png)
##### Post an Announcement 
To inform your clients the latest release or other information, you can post an announcement. This announcement will be sent to all clients.
![在这里插入图片描述](https://img-blog.csdnimg.cn/6ee9a8cce243467d9a14db5968dbf816.png)
 
<br><br>
You can also check the list of the staff and orders, however as a staff, you do not have right to modify them.

##  How to use the code in your computer
Please clone the code using: git clone https://github.sydney.edu.au/2022-INTERNET-SOFTWARE-PLATFORM/ELEC9609-Group10.git
##### Create table in your database.
Firstly in settings.py check the database name and the password, change that to your password and account.<br>
There are two way to init the database.<br>
The first way is: running the sql code in sql file.<br><br>
The second way is: <br>
<kbd>python manage.py makemigrations</kbd> <br>
<kbd>python manage.py migrate </kbd>


###### Install Dependency
Please ensure that you has install python3 and have upated your pip to the latest version.

<kbd>pip install django</kbd> <br>
<kbd>pip install pymysql</kbd> <br>
<kbd>pip install PIL</kbd> <br>
<kbd>pip install pillow</kbd> <br>

##### Running code
Run  <kbd>python manage.py migrate</kbd> in your terminal.<kbd>cmd</kbd> 
