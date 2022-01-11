from re import L
from flask import Flask
from flask import render_template, request, url_for, redirect
from flask_socketio import SocketIO, join_room, leave_room 
import os
from numpy.lib.type_check import imag
import praw
import random
from praw import reddit, models
from praw.models.listing.mixins import submission, subreddit
import requests
import cv2
import numpy as np
import pickle
from bs4 import BeautifulSoup
import requests
from praw.models import Image, MoreComments
import json

from testinggrounds import Subreddit

#hooking up the server
IMAGE_FOLDER = os.path.join('static', 'photo')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/RedditProxy', methods = ['get', 'post'])
def RedditProxy():
    if request.method == 'POST':
        FROM_HOME = request.form['RedditProxy']
        if RedditProxy:
            return render_template('RedditProxy.html')
        else:
            return render_template('404.html')

#Subreddit Page
@app.route('/RedditSub', methods = ['get', 'post'])
def RedditSub():
    #praw stuff
    RedditSub = request.args.get('RedditSub')
    
    
    if RedditSub:
        reddit = praw.Reddit(
    username = 'WestEstimate3179',
    password = '999MarineCore',
    client_id = 'RthpUmIMJwFz872sejsRrQ',
    client_secret = 'pkxYnYkQ_A2XEBnXZlgJSWSJ-K3PQg',
    user_agent = 'testbot 1.0'
    )

    
    class Image:
        praw.models.Image
    
    def create_reddit_object(json_file="reddit_config.json"):

        with open(json_file) as f:
            data = json.load(f)

        

    
    Imagee= Image()
    subreddit = reddit.subreddit(RedditSub)
    sub_list = open('sub_list.csv', 'w')
    sub_list.write(str(subreddit))
    sub_list.close()
    hot_subreddit= subreddit.hot(limit=100)
    return render_template('RedditSub.html', RedditSub=RedditSub, submission=submission, hot_subreddit=hot_subreddit)

@app.route('/RedditSubMore', methods=['get', 'post'])
def RedditSubMore():
    #praw stuff
    RedditSub = request.args.get('RedditSub')
    RedditSubMore = request.args.get('RedditSubmore')

    if RedditSub and RedditSubMore:
        reddit = praw.Reddit(
    username = 'WestEstimate3179',
    password = '999MarineCore',
    client_id = 'RthpUmIMJwFz872sejsRrQ',
    client_secret = 'pkxYnYkQ_A2XEBnXZlgJSWSJ-K3PQg',
    user_agent = 'testbot 1.0'
    )

    
    class Image:
        praw.models.Image
    
    def create_reddit_object(json_file="reddit_config.json"):

        with open(json_file) as f:
            data = json.load(f)

        

    
    Imagee= Image()
    subreddit = reddit.subreddit(RedditSub)
    sub_list = open('sub_list.csv', 'w')
    sub_list.write(str(subreddit))
    sub_list.close()
    hot_subreddit= subreddit.hot(limit=70)
    return render_template('RedditSub.html', RedditSub=RedditSub, submission=submission, hot_subreddit=hot_subreddit)


@app.route('/RedComm', methods = ['get', 'post'])
def RedComm():
    return render_template("Comments.html", RedditSub=RedditSub, submission=submission, subreddit=subreddit)


if __name__ == ('__main__'):
    app.run(debug=True)

    #notestesting
    #def cup():
    #for submission in hot_subreddit:
    #   print(submission.image
    #   )