# PyEditorial
A free, open-source Blog CMS based on the "Django" and "Editorial" HTML5 theme.

![](https://img.shields.io/github/stars/mavenium/PyEditorial) ![](https://img.shields.io/github/forks/mavenium/PyEditorial) ![](https://img.shields.io/github/issues/mavenium/PyEditorial) ![](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Fmavenium%2FPyEditorial)

------------
### Features

- "Blog" section to create and edit a blog + Blog Category
- "Videocast" section to create and edit a videocast + Videocast Category
- "Podcast" section to create and edit a podcast + podcast Category
- "Skill" section to create and edit a skill
- "CONSTANCE" Section to manage dynamic Django settings (Blog title, Social Networks links and ...)
- Displays the list of Blog posts as paged in archive
- Displays the list of Videocast as paged in archive
- Displays the list of podcast as paged in archive
- Used "Django Admin" to manage all models
- Used "Editorial" theme by HTML5 UP
- Used "Sqlite" to create DB
- Used "CKEditor"
- Translation ready
- Auth system (login & logout and forget a password)
- Front-end forms to create new object
------------
[![](https://s16.picofile.com/file/8419124942/buy_me_a_coffee.png)](https://www.blockchain.com/btc/payment_request?address=1ChqZPGhxpn6HB1WuQh55S3Mf8RydxMiFk&amount=0.00018711 "Buy me a coffee")
- You can buy me a coffee so I can turn it into more open source projects :)
------------
### Special Thanks

| Python | Django | Pycharm |
| ------------- | ------------- | ------------- |
| [![](https://s17.picofile.com/file/8418101118/python.png)](https://www.python.org "Python")  | [![](https://s17.picofile.com/file/8418100976/django.png)](https://www.djangoproject.com "Django")  | [![](https://s17.picofile.com/file/8418101034/pycharm.png)](https://www.jetbrains.com/pycharm/ "Pycharm")  |

------------
### Screenshots

![](https://raw.githubusercontent.com/mavenium/PyEditorial/master/Screenshots/Index.png)
> Index Page

![](https://raw.githubusercontent.com/mavenium/PyEditorial/master/Screenshots/Archive.png)
> Archive Page

![](https://raw.githubusercontent.com/mavenium/PyEditorial/master/Screenshots/Blog-Single.png)
> Blog Single Page

![](https://raw.githubusercontent.com/mavenium/PyEditorial/master/Screenshots/Podcast-Single.png)
> Podcast Single Page

![](https://raw.githubusercontent.com/mavenium/PyEditorial/master/Screenshots/Videocast-Single.png)
> Videocast Single Page

![](https://raw.githubusercontent.com/mavenium/PyEditorial/master/Screenshots/Admin.png)
> Admin Area

![](https://raw.githubusercontent.com/mavenium/PyEditorial/master/Screenshots/Constance.png)
> Dynamic Django Settings

![](https://raw.githubusercontent.com/mavenium/PyEditorial/master/Screenshots/Blog-Admin.png)
> Blog Section

![](https://raw.githubusercontent.com/mavenium/PyEditorial/master/Screenshots/Add-Blog.png)
> Add Blog

![](https://raw.githubusercontent.com/mavenium/PyEditorial/master/Screenshots/Add-Videocast.png)
> Add Videocast

![](https://github.com/mavenium/PyEditorial/blob/master/Screenshots/Add-Skill.png)
> Add Skill

![](https://raw.githubusercontent.com/mavenium/PyEditorial/master/Screenshots/Add-Podcast.png)
> Add Podcast

------------
### How to install and run (GNU/Linux and Mac)
                
1. Install `git`,`python3`, `pip3`, `virtualenv` in your operating system
2. Create a development environment ready by using these commands
```
git clone https://github.com/mavenium/PyEditorial		# clone the project
cd PyEditorial		                                        # go to the project DIR
virtualenv -p python3 .venv		                        # Create virtualenv named .venv
source .venv/bin/activate		                        # Active virtualenv named .venv
pip install -r requirements.txt		                        # Install project requirements in .venv
python manage.py makemigrations		                        # Create migrations files
python manage.py migrate		                        # Create database tables
python manage.py collectstatic		                        # Create statics files
python manage.py runserver		                        # Run the project
```
3. Go to  `http://127.0.0.1:8000/` to use project
------------
### Notes
The Editorial template is released under license "Creative Commons Attribution 3.0 Unported".

------------
### TODO list

- [x] Create search section
- [x] Create user Login/Logout forms in front-end
- [x] Create dynamic forms to add contents in front-end
