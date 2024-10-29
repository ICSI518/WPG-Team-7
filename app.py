# app.py - Main application file for the Web Prototype Generator

'''
This code is being built simultaneously by all team members.

The contribution is clearly mentioned in the following Format: '{Team Member Name} - Team Member's Contribution'

Whenever a Team member make any change pushes the code, they will highlight their part of the contribution with comments.

This source code has few components created using ChatGPT-4o and they are clearly mentioned.
'''

from flask import Flask, render_template, request, jsonify, send_file
import google.generativeai as genai
import requests
import nltk
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
