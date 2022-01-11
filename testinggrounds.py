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

reddit = praw.Reddit(
    username = 'WestEstimate3179',
    password = '999MarineCore',
    client_id = 'RthpUmIMJwFz872sejsRrQ',
    client_secret = 'pkxYnYkQ_A2XEBnXZlgJSWSJ-K3PQg',
    user_agent = 'testbot 1.0'
    )
Subreddit = reddit.subreddit("shitposting")
hot = Subreddit.hot(limit = 10)
x = next(hot)
dir(x)
#print (dir(x))