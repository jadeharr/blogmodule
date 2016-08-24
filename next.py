#!/usr/bin/env python3
"""Second page of website."""

import pymysql
from flask import Flask
from flask import render_template

from blogmodule import pages

app = Flask(__name__)


@app.route('/')
def title_page():
    """Title page of website."""
    # Initialize key variables
    return pages.title()


@app.route('/cooking')
def cooking_page():
    """Cooking page of website."""
    # Initialize key variables
    return pages.cooking()


@app.route('/travel')
def travel_page():
    """Travel page of website."""
    # Initialize key variables
    return pages.travel()


@app.route('/plants')
def plants_page():
    """plants page of website."""
    # Initialize key variables
    return pages.plants()


@app.route('/photography')
def photography_page():
    """photography page of website."""
    # Initialize key variables
    return pages.photography()


@app.route('/decorating')
def decorating_page():
    """ page of website."""
    # Initialize key variables
    return pages.decorating()


@app.route('/books')
def books_page():
    """books page of website."""
    # Initialize key variables
    return pages.books()


@app.route('/blog')
def blog_page():
    """blog page of website."""
    # Initialize key variables
    return pages.blog()

if __name__ == '__main__':
    app.run()
