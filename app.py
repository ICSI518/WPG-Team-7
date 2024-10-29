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

# Kona Venkata Sylesh: Image Fetching Helper Function

# Helper function to fetch images from Unsplash
def fetch_images(description, num_images=3):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(description)
    keywords = [word for word in words if word.lower() not in stop_words and word.isalpha()]
    search_query = ", ".join(keywords[:5])

    url = "https://api.unsplash.com/search/photos"
    params = {
        "query": search_query,
        "per_page": num_images,
        "client_id": UNSPLASH_ACCESS_KEY,
        "orientation": "landscape"
    }
    response = requests.get(url, params=params)
    image_urls = []

    if response.status_code == 200:
        data = response.json()
        for result in data['results']:
            image_urls.append(result['urls']['regular'])

    return image_urls

