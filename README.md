<h1 align=center >PERSONAL DEVELOPER BLOG</h1>

<p align=center >Created by Keith James on the 22nd of September 2021</p>

<p align="center"> This project was created with Python version 3 </p>

===============================================================================================================
<p align="left"> <a href="https://github.com/ryo-ma/github-profile-trophy"><img src="https://github-profile-trophy.vercel.app/?username=freestyletear" alt="freestyletear github profile trophy's" /></a> </p>

[![GitHub Issues](https://img.shields.io/github/issues/freestyletear/personal-developer-blog)](https://freestyletear.github.io/personal-developer-blog/issues)

## Description

This application shows random quotes and it's authors to the users. The users can register to the app and log in to post their quotes or blogs on the website. They can also comment on other user's post, comment on their own or delete their comments if they found innapropriate.
The application shows the date when the post was posted and also when the comment was posted.

## User Story

1. As a user, I would like to see the blogs other people have posted.
2. As a user, I would like to be signed in for me to leave a comment
3. As a user, I would like to receive a welcoming email once I sign up.
4. As a user, I would like to comment on the different blogs and leave feedback.   



## Languages and Tools

[<img src="https://www.python.org/static/opengraph-icon-200x200.png" alt="python" width="100" height="70"/>](https://www.w3schools.com/python/default.asp "python 3")
[<img src="https://e7.pngegg.com/pngimages/654/56/png-clipart-flask-web-framework-python-software-framework-jinja-flask-miscellaneous-monochrome-thumbnail.png" alt="flask" width="100" height="70"/>](https://flask.palletsprojects.com/en/2.0.x/ "flask")
[<img src="https://cdn-images-1.medium.com/max/1200/1*Zkhl4Zz43z2_iR_ADlP-rg.png" alt="google" width="70" height="70"/>](https://www.google.com/ "google")
[<img src="https://github.githubassets.com/images/modules/open_graph/github-octocat.png" alt="github" width="100" height="70"/>](https://docs.github.com/en "github")
[<img src="https://uploads.sitepoint.com/wp-content/uploads/2016/04/1461122387heroku-logo.jpg" alt="flask" width="100" height="70"/>](https://www.heroku.com/about "heroku")
[<img src="https://www.opensourceagenda.com/projects/flask-bootstrap/image.png" alt="flask" width="100" height="70"/>](https://pythonhosted.org/Flask-Bootstrap/ "flask_bootstrap")
[<img src="https://d1nhio0ox7pgb.cloudfront.net/_img/g_collection_png/standard/512x512/html_tag.png" alt="github" width="100" height="70"/>](https://www.w3schools.com/html/html_intro.asp "html")
[<p>Fake email account</p>](https://emailfake.com/)
[<p>CSS</p>](https://www.w3schools.com/css/)
[<p>Postgressql</p>](https://www.postgresql.org/)


## Features


<p><img align="center" src="https://github-readme-stats.vercel.app/api/top-langs?username=freestyletear&show_icons=true&locale=en&layout=compact&theme=cobalt" alt="freestyletear github status on top languages used" /></p>

<p>&nbsp;<img align="center" src="https://github-readme-stats.vercel.app/api?username=freestyletear&show_icons=true&locale=en&theme=cobalt" alt="freestyletear github status on extra pins" /></p>

<p><img align="center" src="https://github-readme-streak-stats.herokuapp.com/?user=freestyletear&show_icons=true&theme=cobalt" /></p>

## SetUp / Installation Requirements

- Clone this repository to a location in your file system. `git clone https://github.com/freestyletear/personal-developer-blog.git`
- Open terminal command line then navigate to the root folder of the application. `cd personal-developer-blog`

  - On the terminal enter
      ```
      $ git init
      ```
  - Then create a virtual enviroment depending with the python version you have it has to be above 3.0.0
      ```
      $ python3 -m venv --without-pip venv
      ```
      - Or
        ```
        $ python3 -m venv venv
        ```
  - Lets activate the enviroment (_venv_ is just a word you can use any as long as you remember)
      ```
      $ source venv/bin/ativate
      ```
  - Read the specs and requirements files and Install all the requirements.
  - Install dependancies that will create an environment for the app to run:
       ```
       $ pip install -r requirements
  - Create you database
    - open python shell
        ```
        $ python3
        ```
        - Then
        ```
        >>> from app import db
        ```

        ```
        >>> db.create_all()
        ```
  - Run 
    ```
    python3 run.py
    ```
  - Note this will work if you've properly configured your app with the required dependencies 
  - Access the application through `localhost:5000`


  ## Behavior Driven Development

## Additional Requirements

- Git
- Web-browser or your choice
- Github
- Pip
- Python 3+


- Navigate to `http://localhost:5000/` in your browser.

- Live link to view the project <a target="_blank" href="https://personal-developer-blog.herokuapp.com/">PERSONAL DEVELOPER BLOG</a>

>Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo reach out to (https://github.com/freestyletear/personal-dev-blog/fork)
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request

## Known Bugs / Feature Request

* At the date of build, at the comment section deleting comment was not fully functional instade it was deleting the entire post.
* If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/freestyletear/personal-dev-blog/issues/new) by including your search query and the expected result.
* If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/freestyletear/personal-dev-blog/issues/new) Please include sample queries and their corresponding result.

## Further help

* To get more help on the Python CLI use ng help or go check out the Python CLI README and Python documentation.

## Sources

- 👨‍💻<p align="left"> <img width="800" height="300" src="" alt="" /> </p>


---

## To-do
1. Add fuctionality and styling.

## 📫 Support and contact details

- portfolio https://keithjames-portfolio-version-two-2a6267.netlify.app/
- Assist-email addressess **_keithjame@gmail.com_** <br>  **_freestyletear@gmail.com_**
- phone: _Airtel-Kenya_ :- ~+254788507559~

| [Linkedin](https://www.linkedin.com/in/keith-james-34a3041ba/) |
[Facebook](https://web.facebook.com/keithjamesmerchantmagnifico/) |
[Instagram](https://www.instagram.com/freestyletear/) |
[Twitter](https://twitter.com/KeithJa90059609) |
[Tik-tok](https://www.tiktok.com/@keithjames_themerchant?lang=en) |

---
### License

*MIT*
Copyright (c) 2021 **Keith James**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---
