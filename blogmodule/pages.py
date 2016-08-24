#!/usr/bin/env python3
"""Second page of website."""

import pymysql


class Posts(object):
    """funtion for posting."""

    def __init__(self):
        """init for blog."""
        self.connection = pymysql.connect(
            host='localhost', port=3306,
            user='root', passwd='Hello123?', db='blog')

    def read_all(self):
        """Add a post to blog."""
        cursor = self.connection.cursor()

        sql = (
            'select subject, image_url, link from flask_tbl'
            )

        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        self.connection.close()

        return result


def title():
    """Title page of website."""
    # Initialize key variables
    html = ''

    head = ("""\
<!DOCTYPE html>
<html>
<head>
    <style>
        html, body {
            display: flex;
            flex-direction: column;
}

        header {
            margin-bottom: 30px;
}

        body {
            background-image: url("http://www.scrollshow.net/asse\
ts/themes/plimse/Gradient_gray/GradientGray_web.png");
            background-position: center top;
            background-size: cover;
            margin: 0px;
}

        .dropbtn {
            border: none;
            cursor: pointer;
            background-color: transparent;
            color: dimgrey;
}

        .dropbtn p:hoover {
            color: olivedrab;
}

        .dropdown {
            position: relative;
            display: inline-block;
}

        .dropdown-content {
            display: none;
            position: absolute;
            background-color: #f9f9f9;
            min-width: 160px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
}

        .dropdown-content a {
            color: dimgrey;
            padding: 12px 16px;
            text-decoration: none;
            display: block;
}

        .dropdown-content a:hover {
            background-color: #f1f1f1;
            color: olivedrab;
            text-decoration: none;
}

        .dropdown:hover .dropdown-content {
            display: block;
}

        a p:hover {
            color: olivedrab;
            text-decoration: none;
}

        div nav a p {
            font-size: 16px;
            display: inline;
            text-decoration:none;
            margin-top: 40px;
}

        .gallery {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
}

        .gallery-item {
            display: inline;
}

        .thumbnail {
            height: 250px;
            width: 450px;
}

        p {
            font-size: 18px;
            font-family: Verdana, Georgia, Serif;
}

        footer ul {
            list-style: none;
}

        footer .col-sm-8 {
            display: flex;
            justify-content: flex-end;
}

        section .row img {
            margin: 0 0 30 0px;
            width: 100%;
}

        footer li a img {
            width: 33px;
            height: 33px;
            display: inline;
            position: right;
            display: flex;
            flex-wrap: wrap;
            margin-bottom: 15px;
}
   </style>
    <meta charset="utf-8"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/\
3.3.6/css/bootstrap.min.css"/>
</head>
""")

    body_start = ("""\
<body>
    <header class="container">
        <div class="row" display="flex" align-items: right>
            <h1 class="col-sm-8" style="font-size: 50px; font-family: cursive">
                <a style="color: black" href="http://localhost:5000/">
                    <b><em>Hello World!</em></b>
                </a>
            </h1>
            <nav class="col-sm-4" style="margin-top: 30px">
                <div class="dropdown">
                    <button class="dropbtn">
                            <p style="font-size: 16px">menu</p>
                    </button>
                    <div class="dropdown-content">
                        <a href="http://localhost:5000/cooking">
                            Cooking
                        </a>
                        <a href="http://localhost:5000/travel">
                            Travel
                        </a>
                        <a href="http://localhost:5000/plants">
                            Plants
                        </a>
                        <a href="http://localhost:5000/photography">
                            Photography
                        </a>
                        <a href="http://localhost:5000/decorating">
                            Decorating
                        </a>
                        <a href="http://localhost:5000/books">
                            Books
                        </a>
                        <a href="http://localhost:5000/blog">
                            Blog
                        </a>
                    </div>
                </div>
                <a href="#" style="text-decoration:none; color:dimgrey">
                    <p style="margin:0 0 0 20px">about me</p>
                </a>
                <a href="#" style="text-decoration:none; color:dimgrey">
                    <p style="margin:0 0 0 20px">contact</p>
                </a>
            </nav>
        </div>
    </header>
    <section class="container">
        <div class="row, gallery">
""")

    body_end = ("""\
        </div>
    </section>
    <footer class="container">
        <div class="row">
            <p class="col-sm-4" style="font-size: 12px">&copy \
2016 Hello World!</p>
            <ul class="col-sm-8">
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_LinkedIn-128.png"/>
                    </a>
                </li>
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_Facebook-128.png"/>
                    </a>
                </li>
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_Google-128.png"/>
                    </a>
                </li>
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_SoundCloud-128.png"/>
                    </a>
                </li>
            </ul>
        </div>
    </footer>
</body>
""")

    html = ('%s%s') % (html, head)
    html = ('%s%s') % (html, body_start)

    database = Posts()
    posts = database.read_all()

    for row in posts:
        subject = row[0]
        url = row[1]
        link = row[2]
        post_html = ("""\
            <figure class="gallery-item, col-sm-6">
                <p>%s</p>
                <a href="%s">
                    <img class="thumbnail" src="%s"/>
                </a>
            </figure>
""") % (subject, link, url)
        html = ('%s%s') % (html, post_html)

    html = ('%s%s') % (html, body_end)
    return html


class Cook(object):
    """funtion for posting."""

    def __init__(self, body, subject, image_url, link):
        """init for blog."""
        self.body = body
        self.subject = subject
        self.image_url = image_url
        self.link = link

        self.conn = pymysql.connect(host='localhost', port=3306,
                                    user='root', passwd='Hello123?', db='blog')

    def post(self):
        """Add a post to blog."""
        cur = self.conn.cursor()

        sql = (
            'INSERT INTO writingcook (subject, body, image_url, link) '
            'VALUES ("%s", "%s", "%s", "%s")') % (
                self.subject, self.body, self.image_url, self.link)

        cur.execute(sql)
        self.conn.commit()
        cur.close()
        self.conn.close()


def cooking():
    """Create web page."""
    output = ''

    head = ("""\
<!DOCTYPE html>
<html>
<head>
    <style>
        html, body {
            display: flex;
            flex-direction: column;
}

        header {
            margin-bottom: 30px;
}

        body {
            background-image: url("http://www.scrollshow.net/asse\
ts/themes/plimse/Gradient_gray/GradientGray_web.png");
            background-position: center top;
            background-size: cover;
            margin: 0px;
}

        .dropbtn {
            border: none;
            cursor: pointer;
            background-color: transparent;
            color: dimgrey;
}

        .dropbtn p:hoover {
            color: olivedrab;
}

        .dropdown {
            position: relative;
            display: inline-block;
}

        .dropdown-content {
            display: none;
            position: absolute;
            background-color: #f9f9f9;
            min-width: 160px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
}

        .dropdown-content a {
            color: dimgrey;
            padding: 12px 16px;
            text-decoration: none;
            display: block;
}

        .dropdown-content a:hover {
            background-color: #f1f1f1;
            color: olivedrab;
            text-decoration: none;
}

        .dropdown:hover .dropdown-content {
            display: block;
}

        a p:hover {
            color: olivedrab;
            text-decoration: none;
}

        p {
            font-size: 18px;
            font-family: Verdana, Georgia, Serif;
}

        div nav a p {
            font-size: 16px;
            display: inline;
            text-decoration:none;
            margin-top: 40px;
}

        .jumbotron {
            display: flex;
            align-items: center;
            background-image: url("http://www.incimages.com/uploaded_fil\
es/image/970x450/maple_55164.jpg");
            background-size: cover;
            height: 400px;
            text-shadow:
                -1.75px -1.75px 0 #696969,
                1.75px -1.75px 0 #696969,
                -1.75px 1.75px 0 #696969,
                1.75px 1.75px 0 #696969;
            color: #ffffff;
}

        .jumbotron h2 {
            font-size: 60px;
            font-weight: 700;
            margin: 0;
            color: #FFFAF0;
}

        footer ul {
            list-style: none;
}

        footer .col-sm-8 {
            display: flex;
            justify-content: flex-end;
}

        section .row img {
            margin: 0 0 30 0px;
            width: 100%;
}

        footer li a img {
            width: 33px;
            height: 33px;
            display: inline;
            position: right;
            display: flex;
            flex-wrap: wrap;
            margin-bottom: 15px;
}
    </style>
    <meta charset="utf-8"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/\
3.3.6/css/bootstrap.min.css"/>
</head>
""")

    body_start = ("""\
<body>
    <header class="container">
        <div class="row" display="flex" align-items: right>
            <h1 class="col-sm-8" style="font-size: 50px; font-family: cursive">
                <a style="color: black" href="http://localhost:5000/">
                    <b><em>Hello World!</em></b>
                </a>
            </h1>
            <nav class="col-sm-4" style="margin-top: 30px">
                <div class="dropdown">
                    <button class="dropbtn">
                            <p style="font-size: 16px">menu</p>
                    </button>
                    <div class="dropdown-content">
                        <a href="http://localhost:5000/cooking.py">
                            Cooking
                        </a>
                        <a href="http://localhost:5000/travel.py">
                            Travel
                        </a>
                        <a href="http://localhost:5000/plants.py">
                            Plants
                        </a>
                        <a href="http://localhost:5000/photography.py">
                            Photography
                        </a>
                        <a href="http://localhost:5000/decorating.py">
                            Decorating
                        </a>
                        <a href="http://localhost:5000/books.py">
                            Books
                        </a>
                        <a href="http://localhost:5000/blog.py">
                            Blog
                        </a>
                    </div>
                </div>
                <a href="#" style="text-decoration:none; color:dimgrey">
                    <p style="margin:0 0 0 20px">about me</p>
                </a>
                <a href="#" style="text-decoration:none; color:dimgrey">
                    <p style="margin:0 0 0 20px">contact</p>
                </a>
            </nav>
        </div>
    </header>
""")

    body_middle = ("""\
    <section class="jumbotron">
        <div class="container">
            <div class="row text-center">
                <h2>Cooking</h2>
            </div>
        </div>
    </section>
""")

    body_end = ("""\
    <footer class="container">
        <div class="row">
            <p class="col-sm-4" style="font-size: 12px">&copy \
2016 Hello World!</p>
            <ul class="col-sm-8">
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_LinkedIn-128.png"/>
                    </a>
                </li>
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_Facebook-128.png"/>
                    </a>
                </li>
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_Google-128.png"/>
                    </a>
                </li>
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_SoundCloud-128.png"/>
                    </a>
                </li>
            </ul>
        </div>
    </footer>
</body>
""")

    output = ('%s%s') % (output, head)
    output = ('%s%s') % (output, body_start)
    output = ('%s%s') % (output, body_middle)
    output = ('%s%s') % (output, body_end)

    return output


class Travel(object):
    """funtion for posting."""

    def __init__(self, body, subject, image_url, link):
        """init for blog."""
        self.body = body
        self.subject = subject
        self.image_url = image_url
        self.link = link

        self.conn = pymysql.connect(host='localhost', port=3306,
                                    user='root', passwd='Hello123?', db='blog')

    def post(self):
        """Add a post to blog."""
        cur = self.conn.cursor()

        sql = (
            'INSERT INTO writingtravel (subject, body, image_url, link) '
            'VALUES ("%s", "%s", "%s", "%s")') % (
                self.subject, self.body, self.image_url, self.link)

        cur.execute(sql)
        self.conn.commit()
        cur.close()
        self.conn.close()


def travel():
    """Create web page."""
    output = ''

    head = ("""\
<!DOCTYPE html>
<html>
<head>
    <style>
        html, body {
            display: flex;
            flex-direction: column;
}

        header {
            margin-bottom: 30px;
}

        body {
            background-image: url("http://www.scrollshow.net/asse\
ts/themes/plimse/Gradient_gray/GradientGray_web.png");
            background-position: center top;
            background-size: cover;
            margin: 0px;
}

        .dropbtn {
            border: none;
            cursor: pointer;
            background-color: transparent;
            color: dimgrey;
}

        .dropbtn p:hoover {
            color: olivedrab;
}

        .dropdown {
            position: relative;
            display: inline-block;
}

        .dropdown-content {
            display: none;
            position: absolute;
            background-color: #f9f9f9;
            min-width: 160px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
}

        .dropdown-content a {
            color: dimgrey;
            padding: 12px 16px;
            text-decoration: none;
            display: block;
}

        .dropdown-content a:hover {
            background-color: #f1f1f1;
            color: olivedrab;
            text-decoration: none;
}

        .dropdown:hover .dropdown-content {
            display: block;
}

        a p:hover {
            color: olivedrab;
            text-decoration: none;
}

        p {
            font-size: 18px;
            font-family: Verdana, Georgia, Serif;
}

        div nav a p {
            font-size: 16px;
            display: inline;
            text-decoration:none;
            margin-top: 40px;
}

        .jumbotron {
            display: flex;
            align-items: center;
            background-image: url("https://static.pexels.com/photos/2324/sk\
yline-buildings-new-york-skyscrapers.jpg");
            background-size: cover;
            height: 400px;
            text-shadow:
                -1.75px -1.75px 0 #2F4F4F,
                1.75px -1.75px 0 #2F4F4F,
                -1.75px 1.75px 0 #2F4F4F,
                1.75px 1.75px 0 #2F4F4F;
            color: #ffffff;
}

        .jumbotron h2 {
            font-size: 60px;
            font-weight: 700;
            margin: 0;
            color: #FFFAF0;
}

        footer ul {
            list-style: none;
}

        footer .col-sm-8 {
            display: flex;
            justify-content: flex-end;
}

        section .row img {
            margin: 0 0 30 0px;
            width: 100%;
}

        footer li a img {
            width: 33px;
            height: 33px;
            display: inline;
            position: right;
            display: flex;
            flex-wrap: wrap;
            margin-bottom: 15px;
}
    </style>
    <meta charset="utf-8"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/\
3.3.6/css/bootstrap.min.css"/>
</head>
""")

    body_start = ("""\
<body>
    <header class="container">
        <div class="row" display="flex" align-items: right>
            <h1 class="col-sm-8" style="font-size: 50px; font-family: cursive">
                <a style="color: black" href="http://localhost:5000/">
                    <b><em>Hello World!</em></b>
                </a>
            </h1>
            <nav class="col-sm-4" style="margin-top: 30px">
                <div class="dropdown">
                    <button class="dropbtn">
                            <p style="font-size: 16px">menu</p>
                    </button>
                    <div class="dropdown-content">
                        <a href="http://localhost:5000/cooking">
                            Cooking
                        </a>
                        <a href="http://localhost:5000/travel">
                            Travel
                        </a>
                        <a href="http://localhost:5000/plants">
                            Plants
                        </a>
                        <a href="http://localhost:5000/photography">
                            Photography
                        </a>
                        <a href="http://localhost:5000/decorating">
                            Decorating
                        </a>
                        <a href="http://localhost:5000/books">
                            Books
                        </a>
                        <a href="http://localhost:5000/blog">
                            Blog
                        </a>
                    </div>
                </div>
                <a href="#" style="text-decoration:none; color:dimgrey">
                    <p style="margin:0 0 0 20px">about me</p>
                </a>
                <a href="#" style="text-decoration:none; color:dimgrey">
                    <p style="margin:0 0 0 20px">contact</p>
                </a>
            </nav>
        </div>
    </header>
""")

    body_middle = ("""\
    <section class="jumbotron">
        <div class="container">
            <div class="row text-center">
                <h2>Travel</h2>
            </div>
        </div>
    </section>
""")

    body_end = ("""\
    <footer class="container">
        <div class="row">
            <p class="col-sm-4" style="font-size: 12px">&copy \
2016 Hello World!</p>
            <ul class="col-sm-8">
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_LinkedIn-128.png"/>
                    </a>
                </li>
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_Facebook-128.png"/>
                    </a>
                </li>
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_Google-128.png"/>
                    </a>
                </li>
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_SoundCloud-128.png"/>
                    </a>
                </li>
            </ul>
        </div>
    </footer>
</body>
""")

    output = ('%s%s') % (output, head)
    output = ('%s%s') % (output, body_start)
    output = ('%s%s') % (output, body_middle)
    output = ('%s%s') % (output, body_end)

    return output


class Plant(object):
    """funtion for posting."""

    def __init__(self, body, subject, image_url, link):
        """init for blog."""
        self.body = body
        self.subject = subject
        self.image_url = image_url
        self.link = link

        self.conn = pymysql.connect(host='localhost', port=3306,
                                    user='root', passwd='Hello123?', db='blog')

    def post(self):
        """Add a post to blog."""
        cur = self.conn.cursor()

        sql = (
            'INSERT INTO writingplant (subject, body, image_url, link) '
            'VALUES ("%s", "%s", "%s", "%s")') % (
                self.subject, self.body, self.image_url, self.link)

        cur.execute(sql)
        self.conn.commit()
        cur.close()
        self.conn.close()


def plants():
    """Create web page."""
    output = ''

    head = ("""\
<!DOCTYPE html>
<html>
<head>
    <style>
        html, body {
            display: flex;
            flex-direction: column;
}

        header {
            margin-bottom: 30px;
}

        body {
            background-image: url("http://www.scrollshow.net/asse\
ts/themes/plimse/Gradient_gray/GradientGray_web.png");
            background-position: center top;
            background-size: cover;
            margin: 0px;
}

        .dropbtn {
            border: none;
            cursor: pointer;
            background-color: transparent;
            color: dimgrey;
}

        .dropbtn p:hoover {
            color: olivedrab;
}

        .dropdown {
            position: relative;
            display: inline-block;
}

        .dropdown-content {
            display: none;
        position: absolute;
            background-color: #f9f9f9;
            min-width: 160px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
}

        .dropdown-content a {
            color: dimgrey;
            padding: 12px 16px;
            text-decoration: none;
            display: block;
}

        .dropdown-content a:hover {
            background-color: #f1f1f1;
            color: olivedrab;
            text-decoration: none;
}

        .dropdown:hover .dropdown-content {
            display: block;
}

        a p:hover {
            color: olivedrab;
            text-decoration: none;
}

        p {
            font-size: 18px;
            font-family: Verdana, Georgia, Serif;
}

        div nav a p {
            font-size: 16px;
            display: inline;
            text-decoration:none;
            margin-top: 40px;
}

        .jumbotron {
            display: flex;
            align-items: center;
            background-image: url("http://allpicts.in/wp-content/uploads/20\
14/10/LushBlueHydrangeas.jpg");
            background-size: cover;
            height: 400px;
            text-shadow:
                -1.75px -1.75px 0 #663399,
                1.75px -1.75px 0 #663399,
                -1.75px 1.75px 0 #663399,
                1.75px 1.75px 0 #663399;
            color: #ffffff;
}

        .jumbotron h2 {
            font-size: 60px;
            font-weight: 700;
            margin: 0;
            color: #FFFAF0;
}

        footer ul {
            list-style: none;
}

        footer .col-sm-8 {
            display: flex;
            justify-content: flex-end;
}

        section .row img {
            margin: 0 0 30 0px;
            width: 100%;
}

    footer li a img {
            width: 33px;
            height: 33px;
            display: inline;
            position: right;
            display: flex;
            flex-wrap: wrap;
            margin-bottom: 15px;
}
    </style>
    <meta charset="utf-8"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/\
3.3.6/css/bootstrap.min.css"/>
</head>
""")

    body_start = ("""\
<body>
    <header class="container">
        <div class="row" display="flex" align-items: right>
            <h1 class="col-sm-8" style="font-size: 50px; font-family: cursive">
                <a style="color: black" href="http://localhost:5000/">
                    <b><em>Hello World!</em></b>
                </a>
            </h1>
            <nav class="col-sm-4" style="margin-top: 30px">
                <div class="dropdown">
                    <button class="dropbtn">
                            <p style="font-size: 16px">menu</p>
                    </button>
                    <div class="dropdown-content">
                        <a href="http://localhost:5000/cooking">
                            Cooking
                        </a>
                        <a href="http://localhost:5000/travel">
                            Travel
                        </a>
                        <a href="http://localhost:5000/plants">
                            Plants
                        </a>
                        <a href="http://localhost:5000/photography">
                            Photography
                        </a>
                        <a href="http://localhost:5000/decorating">
                            Decorating
                        </a>
                        <a href="http://localhost:5000/books">
                            Books
                        </a>
                        <a href="http://localhost:5000/blog">
                            Blog
                        </a>
                    </div>
                </div>
                <a href="#" style="text-decoration:none; color:dimgrey">
                    <p style="margin:0 0 0 20px">about me</p>
                </a>
                <a href="#" style="text-decoration:none; color:dimgrey">
                    <p style="margin:0 0 0 20px">contact</p>
                </a>
            </nav>
        </div>
    </header>
""")

    body_middle = ("""\
    <section class="jumbotron">
        <div class="container">
            <div class="row text-center">
                <h2>Plants</h2>
            </div>
        </div>
    </section>
""")

    body_end = ("""\
    <footer class="container">
        <div class="row">
            <p class="col-sm-4" style="font-size: 12px">&copy \
2016 Hello World!</p>
            <ul class="col-sm-8">
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_LinkedIn-128.png"/>
                    </a>
                </li>
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_Facebook-128.png"/>
                    </a>
                </li>
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_Google-128.png"/>
                    </a>
                </li>
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_SoundCloud-128.png"/>
                    </a>
                </li>
            </ul>
        </div>
    </footer>
</body>
""")

    output = ('%s%s') % (output, head)
    output = ('%s%s') % (output, body_start)
    output = ('%s%s') % (output, body_middle)
    output = ('%s%s') % (output, body_end)

    return output


class Photo(object):
    """funtion for posting."""

    def __init__(self, body, subject, image_url, link):
        """init for blog."""
        self.body = body
        self.subject = subject
        self.image_url = image_url
        self.link = link

        self.conn = pymysql.connect(host='localhost', port=3306,
                                    user='root', passwd='Hello123?', db='blog')

    def post(self):
        """Add a post to blog."""
        cur = self.conn.cursor()

        sql = (
            'INSERT INTO writingphoto (subject, body, image_url, link) '
            'VALUES ("%s", "%s", "%s", "%s")') % (
                self.subject, self.body, self.image_url, self.link)

        cur.execute(sql)
        self.conn.commit()
        cur.close()
        self.conn.close()

def photography():
    """Create web page."""
    output = ''

    head = ("""\
<!DOCTYPE html>
<html>
<head>
    <style>
        html, body {
            display: flex;
            flex-direction: column;
}

        header {
            margin-bottom: 30px;
}

        body {
            background-image: url("http://www.scrollshow.net/asse\
ts/themes/plimse/Gradient_gray/GradientGray_web.png");
            background-position: center top;
            background-size: cover;
            margin: 0px;
}

        .dropbtn {
            border: none;
            cursor: pointer;
            background-color: transparent;
            color: dimgrey;
}

        .dropbtn p:hoover {
            color: olivedrab;
}

        .dropdown {
            position: relative;
            display: inline-block;
}

        .dropdown-content {
            display: none;
        position: absolute;
            background-color: #f9f9f9;
            min-width: 160px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
}

        .dropdown-content a {
            color: dimgrey;
            padding: 12px 16px;
            text-decoration: none;
            display: block;
}

        .dropdown-content a:hover {
            background-color: #f1f1f1;
            color: olivedrab;
            text-decoration: none;
}

        .dropdown:hover .dropdown-content {
            display: block;
}

        a p:hover {
            color: olivedrab;
            text-decoration: none;
}

        p {
            font-size: 18px;
            font-family: Verdana, Georgia, Serif;
}

        div nav a p {
            font-size: 16px;
            display: inline;
            text-decoration:none;
            margin-top: 40px;
}

        .jumbotron {
            display: flex;
            align-items: center;
            background-image: url("https://wallpaperscraft.com/image/camera_\
lens_glare_54758_2560x1600.jpg");
            background-size: cover;
            height: 400px;
            text-shadow:
                -1.75px -1.75px 0 #4682B4,
                1.75px -1.75px 0 #4682B4,
                -1.75px 1.75px 0 #4682B4,
                1.75px 1.75px 0 #4682B4;
            color: #ffffff;
}

        .jumbotron h2 {
            font-size: 60px;
            font-weight: 700;
            margin: 0;
            color: #FFFAF0;
}

        footer ul {
            list-style: none;
}

        footer .col-sm-8 {
            display: flex;
            justify-content: flex-end;
}

        section .row img {
            margin: 0 0 30 0px;
            width: 100%;
}

    footer li a img {
            width: 33px;
            height: 33px;
            display: inline;
            position: right;
            display: flex;
            flex-wrap: wrap;
            margin-bottom: 15px;
}
    </style>
    <meta charset="utf-8"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/\
3.3.6/css/bootstrap.min.css"/>
</head>
""")

    body_start = ("""\
<body>
    <header class="container">
        <div class="row" display="flex" align-items: right>
            <h1 class="col-sm-8" style="font-size: 50px; font-family: cursive">
                <a style="color: black" href="http://localhost:5000/">
                    <b><em>Hello World!</em></b>
                </a>
            </h1>
            <nav class="col-sm-4" style="margin-top: 30px">
                <div class="dropdown">
                    <button class="dropbtn">
                            <p style="font-size: 16px">menu</p>
                    </button>
                    <div class="dropdown-content">
                        <a href="http://localhost:5000/cooking">
                            Cooking
                        </a>
                        <a href="http://localhost:5000/travel">
                            Travel
                        </a>
                        <a href="http://localhost:5000/plants">
                            Plants
                        </a>
                        <a href="http://localhost:5000/photography">
                            Photography
                        </a>
                        <a href="http://localhost:5000/decorating">
                            Decorating
                        </a>
                        <a href="http://localhost:5000/books">
                            Books
                        </a>
                        <a href="http://localhost:5000/blog">
                            Blog
                        </a>
                    </div>
                </div>
                <a href="#" style="text-decoration:none; color:dimgrey">
                    <p style="margin:0 0 0 20px">about me</p>
                </a>
                <a href="#" style="text-decoration:none; color:dimgrey">
                    <p style="margin:0 0 0 20px">contact</p>
                </a>
            </nav>
        </div>
    </header>
""")

    body_middle = ("""\
    <section class="jumbotron">
        <div class="container">
            <div class="row text-center">
                <h2>Photography</h2>
            </div>
        </div>
    </section>
""")

    body_end = ("""\
    <footer class="container">
        <div class="row">
            <p class="col-sm-4" style="font-size: 12px">&copy \
2016 Hello World!</p>
            <ul class="col-sm-8">
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_LinkedIn-128.png"/>
                    </a>
                </li>
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_Facebook-128.png"/>
                    </a>
                </li>
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_Google-128.png"/>
                    </a>
                </li>
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_SoundCloud-128.png"/>
                    </a>
                </li>
            </ul>
        </div>
    </footer>
</body>
""")

    output = ('%s%s') % (output, head)
    output = ('%s%s') % (output, body_start)
    output = ('%s%s') % (output, body_middle)
    output = ('%s%s') % (output, body_end)

    return output


class Decor(object):
    """funtion for posting."""

    def __init__(self, body, subject, image_url, link):
        """init for blog."""
        self.body = body
        self.subject = subject
        self.image_url = image_url
        self.link = link

        self.conn = pymysql.connect(host='localhost', port=3306,
                                    user='root', passwd='Hello123?', db='blog')

    def post(self):
        """Add a post to blog."""
        cur = self.conn.cursor()

        sql = (
            'INSERT INTO writingdecor (subject, body, image_url, link) '
            'VALUES ("%s", "%s", "%s", "%s")') % (
                self.subject, self.body, self.image_url, self.link)

        cur.execute(sql)
        self.conn.commit()
        cur.close()
        self.conn.close()


def decorating():
    """Create web page."""
    output = ''

    head = ("""\
<!DOCTYPE html>
<html>
<head>
    <style>
        html, body {
            display: flex;
            flex-direction: column;
}

        header {
            margin-bottom: 30px;
}

        body {
            background-image: url("http://www.scrollshow.net/asse\
ts/themes/plimse/Gradient_gray/GradientGray_web.png");
            background-position: center top;
            background-size: cover;
            margin: 0px;
}

        .dropbtn {
            border: none;
            cursor: pointer;
            background-color: transparent;
            color: dimgrey;
}

        .dropbtn p:hoover {
            color: olivedrab;
}

        .dropdown {
            position: relative;
            display: inline-block;
}

        .dropdown-content {
            display: none;
        position: absolute;
            background-color: #f9f9f9;
            min-width: 160px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
}

        .dropdown-content a {
            color: dimgrey;
            padding: 12px 16px;
            text-decoration: none;
            display: block;
}

        .dropdown-content a:hover {
            background-color: #f1f1f1;
            color: olivedrab;
            text-decoration: none;
}

        .dropdown:hover .dropdown-content {
            display: block;
}

        a p:hover {
            color: olivedrab;
            text-decoration: none;
}

        p {
            font-size: 18px;
            font-family: Verdana, Georgia, Serif;
}

        div nav a p {
            font-size: 16px;
            display: inline;
            text-decoration:none;
            margin-top: 40px;
}

        .jumbotron {
            display: flex;
            align-items: center;
            background-image: url("https://format-com-cld-res.cloudinary.c\
om/image/private/s--AknKrISZ--/c_limit,g_center,h_1200,w_65535/a_auto,fl_k\
eep_iptc.progressive,q_95/203804-11191584-Thea_and_Jimmy_Wedding_Blog-10\
9_jpg.jpg");
            background-size: cover;
            height: 400px;
            text-shadow:
                -1.75px -1.75px 0 #556B2F,
                1.75px -1.75px 0 #556B2F,
                -1.75px 1.75px 0 #556B2F,
                1.75px 1.75px 0 #556B2F;
            color: #ffffff;
}

        .jumbotron h2 {
            font-size: 60px;
            font-weight: 700;
            margin: 0;
            color: #FFFAF0;
}

        footer ul {
            list-style: none;
}

        footer .col-sm-8 {
            display: flex;
            justify-content: flex-end;
}

        section .row img {
            margin: 0 0 30 0px;
            width: 100%;
}

        footer li a img {
            width: 33px;
            height: 33px;
            display: inline;
            position: right;
            display: flex;
            flex-wrap: wrap;
            margin-bottom: 15px;
}
    </style>
    <meta charset="utf-8"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/\
3.3.6/css/bootstrap.min.css"/>
</head>
""")

    body_start = ("""\
<body>
    <header class="container">
        <div class="row" display="flex" align-items: right>
            <h1 class="col-sm-8" style="font-size: 50px; font-family: cursive">
                <a style="color: black" href="http://localhost:5000/">
                    <b><em>Hello World!</em></b>
                </a>
            </h1>
            <nav class="col-sm-4" style="margin-top: 30px">
                <div class="dropdown">
                    <button class="dropbtn">
                            <p style="font-size: 16px">menu</p>
                    </button>
                    <div class="dropdown-content">
                        <a href="http://localhost:5000/cooking">
                            Cooking
                        </a>
                        <a href="http://localhost:5000/travel">
                            Travel
                        </a>
                        <a href="http://localhost:5000/plants">
                            Plants
                        </a>
                        <a href="http://localhost:5000/photography">
                            Photography
                        </a>
                        <a href="http://localhost:5000/decorating">
                            Decorating
                        </a>
                        <a href="http://localhost:5000/books">
                            Books
                        </a>
                        <a href="http://localhost:5000/blog">
                            Blog
                        </a>
                    </div>
                </div>
                <a href="#" style="text-decoration:none; color:dimgrey">
                    <p style="margin:0 0 0 20px">about me</p>
                </a>
                <a href="#" style="text-decoration:none; color:dimgrey">
                    <p style="margin:0 0 0 20px">contact</p>
                </a>
            </nav>
        </div>
    </header>
""")

    body_middle = ("""\
    <section class="jumbotron">
        <div class="container">
            <div class="row text-center">
                <h2>Decorating</h2>
            </div>
        </div>
    </section>
""")

    body_end = ("""\
    <footer class="container">
        <div class="row">
            <p class="col-sm-4" style="font-size: 12px">&copy \
2016 Hello World!</p>
            <ul class="col-sm-8">
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_LinkedIn-128.png"/>
                    </a>
                </li>
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_Facebook-128.png"/>
                    </a>
                </li>
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_Google-128.png"/>
                    </a>
                </li>
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_SoundCloud-128.png"/>
                    </a>
                </li>
            </ul>
        </div>
    </footer>
</body>
""")

    output = ('%s%s') % (output, head)
    output = ('%s%s') % (output, body_start)
    output = ('%s%s') % (output, body_middle)
    output = ('%s%s') % (output, body_end)

    return output


class Book(object):
    """funtion for posting."""

    def __init__(self, body, subject, image_url, link):
        """init for blog."""
        self.body = body
        self.subject = subject
        self.image_url = image_url
        self.link = link

        self.conn = pymysql.connect(host='localhost', port=3306,
                                    user='root', passwd='Hello123?', db='blog')

    def post(self):
        """Add a post to blog."""
        cur = self.conn.cursor()

        sql = (
            'INSERT INTO writingbook (subject, body, image_url, link) '
            'VALUES ("%s", "%s", "%s", "%s")') % (
                self.subject, self.body, self.image_url, self.link)

        cur.execute(sql)
        self.conn.commit()
        cur.close()
        self.conn.close()


def books():
    """Create web page."""
    output = ''

    head = ("""\
<!DOCTYPE html>
<html>
<head>
    <style>
        html, body {
            display: flex;
            flex-direction: column;
}

        header {
            margin-bottom: 30px;
}

        body {
            background-image: url("http://www.scrollshow.net/asse\
ts/themes/plimse/Gradient_gray/GradientGray_web.png");
            background-position: center top;
            background-size: cover;
            margin: 0px;
}

        .dropbtn {
            border: none;
            cursor: pointer;
            background-color: transparent;
            color: dimgrey;
}

        .dropbtn p:hoover {
            color: olivedrab;
}

        .dropdown {
            position: relative;
            display: inline-block;
}

        .dropdown-content {
            display: none;
        position: absolute;
            background-color: #f9f9f9;
            min-width: 160px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
}

        .dropdown-content a {
            color: dimgrey;
            padding: 12px 16px;
            text-decoration: none;
            display: block;
}

        .dropdown-content a:hover {
            background-color: #f1f1f1;
            color: olivedrab;
            text-decoration: none;
}

        .dropdown:hover .dropdown-content {
            display: block;
}

        a p:hover {
            color: olivedrab;
            text-decoration: none;
}

        p {
            font-size: 18px;
            font-family: Verdana, Georgia, Serif;
}

        div nav a p {
            font-size: 16px;
            display: inline;
            text-decoration:none;
            margin-top: 40px;
}

        .jumbotron {
            display: flex;
            align-items: center;
            background-image: url("http://images.photowall.com/products/47268/bookshelf-wooden-long-beige.jpg?h=850");
            background-size: cover;
            height: 400px;
            text-shadow:
                -1.75px -1.75px 0 #996300,
                1.75px -1.75px 0 #996300,
                -1.75px 1.75px 0 #996300,
                1.75px 1.75px 0 #996300;
            color: #ffffff;
}

        .jumbotron h2 {
            font-size: 60px;
            font-weight: 700;
            margin: 0;
            color: #FFFAF0;
}

        footer ul {
            list-style: none;
}

        footer .col-sm-8 {
            display: flex;
            justify-content: flex-end;
}

        section .row img {
            margin: 0 0 30 0px;
            width: 100%;
}

    footer li a img {
            width: 33px;
            height: 33px;
            display: inline;
            position: right;
            display: flex;
            flex-wrap: wrap;
            margin-bottom: 15px;
}
    </style>
    <meta charset="utf-8"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/\
3.3.6/css/bootstrap.min.css"/>
</head>
""")

    body_start = ("""\
<body>
    <header class="container">
        <div class="row" display="flex" align-items: right>
            <h1 class="col-sm-8" style="font-size: 50px; font-family: cursive">
                <a style="color: black" href="http://localhost:5000/">
                    <b><em>Hello World!</em></b>
                </a>
            </h1>
            <nav class="col-sm-4" style="margin-top: 30px">
                <div class="dropdown">
                    <button class="dropbtn">
                            <p style="font-size: 16px">menu</p>
                    </button>
                    <div class="dropdown-content">
                        <a href="http://localhost:5000/cooking">
                            Cooking
                        </a>
                        <a href="http://localhost:5000/travel">
                            Travel
                        </a>
                        <a href="http://localhost:5000/plants">
                            Plants
                        </a>
                        <a href="http://localhost:5000/photography">
                            Photography
                        </a>
                        <a href="http://localhost:5000/decorating">
                            Decorating
                        </a>
                        <a href="http://localhost:5000/books">
                            Books
                        </a>
                        <a href="http://localhost:5000/blog">
                            Blog
                        </a>
                    </div>
                </div>
                <a href="#" style="text-decoration:none; color:dimgrey">
                    <p style="margin:0 0 0 20px">about me</p>
                </a>
                <a href="#" style="text-decoration:none; color:dimgrey">
                    <p style="margin:0 0 0 20px">contact</p>
                </a>
            </nav>
        </div>
    </header>
""")

    body_middle = ("""\
    <section class="jumbotron">
        <div class="container">
            <div class="row text-center">
                <h2>Books</h2>
            </div>
        </div>
    </section>
""")

    body_end = ("""\
    <footer class="container">
        <div class="row">
            <p class="col-sm-4" style="font-size: 12px">&copy \
2016 Hello World!</p>
            <ul class="col-sm-8">
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_LinkedIn-128.png"/>
                    </a>
                </li>
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_Facebook-128.png"/>
                    </a>
                </li>
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_Google-128.png"/>
                    </a>
                </li>
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_SoundCloud-128.png"/>
                    </a>
                </li>
            </ul>
        </div>
    </footer>
</body>
""")

    output = ('%s%s') % (output, head)
    output = ('%s%s') % (output, body_start)
    output = ('%s%s') % (output, body_middle)
    output = ('%s%s') % (output, body_end)

    return output


class Blog(object):
    """funtion for posting."""

    def __init__(self, body, subject, image_url, link):
        """init for blog."""
        self.body = body
        self.subject = subject
        self.image_url = image_url
        self.link = link

        self.conn = pymysql.connect(host='localhost', port=3306,
                                    user='root', passwd='Hello123?', db='blog')

    def post(self):
        """Add a post to blog."""
        cur = self.conn.cursor()

        sql = (
            'INSERT INTO writingblog (subject, body, image_url, link) '
            'VALUES ("%s", "%s", "%s", "%s")') % (
                self.subject, self.body, self.image_url, self.link)

        cur.execute(sql)
        self.conn.commit()
        cur.close()
        self.conn.close()


def blog():
    """Create web page."""
    output = ''

    head = ("""\
<!DOCTYPE html>
<html>
<head>
    <style>
        html, body {
            display: flex;
            flex-direction: column;
}

        header {
            margin-bottom: 30px;
}

        body {
            background-image: url("http://www.scrollshow.net/asse\
ts/themes/plimse/Gradient_gray/GradientGray_web.png");
            background-position: center top;
            background-size: cover;
            margin: 0px;
}

        .dropbtn {
            border: none;
            cursor: pointer;
            background-color: transparent;
            color: dimgrey;
}

        .dropbtn p:hoover {
            color: olivedrab;
}

        .dropdown {
            position: relative;
            display: inline-block;
}

        .dropdown-content {
            display: none;
        position: absolute;
            background-color: #f9f9f9;
            min-width: 160px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
}

        .dropdown-content a {
            color: dimgrey;
            padding: 12px 16px;
            text-decoration: none;
            display: block;
}

        .dropdown-content a:hover {
            background-color: #f1f1f1;
            color: olivedrab;
            text-decoration: none;
}

        .dropdown:hover .dropdown-content {
            display: block;
}

        a p:hover {
            color: olivedrab;
            text-decoration: none;
}

        p {
            font-size: 18px;
            font-family: Verdana, Georgia, Serif;
}

        div nav a p {
            font-size: 16px;
            display: inline;
            text-decoration:none;
            margin-top: 40px;
}

        .jumbotron {
            display: flex;
            align-items: center;
            background-image: url("http://i.imgur.com/k7F6HxC.jpg");
            background-size: cover;
            height: 400px;
            text-shadow:
                -1.75px -1.75px 0 #008B8B,
                1.75px -1.75px 0 #008B8B,
                -1.75px 1.75px 0 #008B8B,
                1.75px 1.75px 0 #008B8B;
            color: #ffffff;
}

        .jumbotron h2 {
            font-size: 60px;
            font-weight: 700;
            margin: 0;
            color: #FFFAF0;
}

        footer ul {
            list-style: none;
}

        footer .col-sm-8 {
            display: flex;
            justify-content: flex-end;
}

        section .row img {
            margin: 0 0 30 0px;
            width: 100%;
}

    footer li a img {
            width: 33px;
            height: 33px;
            display: inline;
            position: right;
            display: flex;
            flex-wrap: wrap;
            margin-bottom: 15px;
}
    </style>
    <meta charset="utf-8"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/\
3.3.6/css/bootstrap.min.css"/>
</head>
""")

    body_start = ("""\
<body>
    <header class="container">
        <div class="row" display="flex" align-items: right>
            <h1 class="col-sm-8" style="font-size: 50px; font-family: cursive">
                <a style="color: black" href="http://localhost:5000/">
                    <b><em>Hello World!</em></b>
                </a>
            </h1>
            <nav class="col-sm-4" style="margin-top: 30px">
                <div class="dropdown">
                    <button class="dropbtn">
                            <p style="font-size: 16px">menu</p>
                    </button>
                    <div class="dropdown-content">
                        <a href="http://localhost:5000/cooking">
                            Cooking
                        </a>
                        <a href="http://localhost:5000/travel">
                            Travel
                        </a>
                        <a href="http://localhost:5000/plants">
                            Plants
                        </a>
                        <a href="http://localhost:5000/photography">
                            Photography
                        </a>
                        <a href="http://localhost:5000/decorating">
                            Decorating
                        </a>
                        <a href="http://localhost:5000/books">
                            Books
                        </a>
                        <a href="http://localhost:5000/blog">
                            Blog
                        </a>
                    </div>
                </div>
                <a href="#" style="text-decoration:none; color:dimgrey">
                    <p style="margin:0 0 0 20px">about me</p>
                </a>
                <a href="#" style="text-decoration:none; color:dimgrey">
                    <p style="margin:0 0 0 20px">contact</p>
                </a>
            </nav>
        </div>
    </header>
""")

    body_middle = ("""\
    <section class="jumbotron">
        <div class="container">
            <div class="row text-center">
                <h2>Blog</h2>
            </div>
        </div>
    </section>
""")

    body_end = ("""\
    <footer class="container">
        <div class="row">
            <p class="col-sm-4" style="font-size: 12px">&copy \
2016 Hello World!</p>
            <ul class="col-sm-8">
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_LinkedIn-128.png"/>
                    </a>
                </li>
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_Facebook-128.png"/>
                    </a>
                </li>
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_Google-128.png"/>
                    </a>
                </li>
                <li class="col-sm-1">
                    <a href="#">
                        <img src="https://cdn3.iconfinder.com/data/i\
cons/social-media-2026/60/Socialmedia_icons_SoundCloud-128.png"/>
                    </a>
                </li>
            </ul>
        </div>
    </footer>
</body>
""")

    output = ('%s%s') % (output, head)
    output = ('%s%s') % (output, body_start)
    output = ('%s%s') % (output, body_middle)
    output = ('%s%s') % (output, body_end)

    return output
