from flask import Flask, render_template,request,redirect,url_for,flash
from flask_cors import CORS
from autoscraper import AutoScraper
app = Flask(__name__)
CORS(app)

import os
import serpapi
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")
client = serpapi.Client(api_key=api_key)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shoping', methods=['GET','POST'])
def shoping():
    results = []  # Default empty results
    search_text = None  # Default search text

    if request.method == 'POST':
        # Get the search query from the form
        search_text = request.form.get('search_text')
        if not search_text:
            flash("Please enter a search query", "error")
        else:
            # Perform the search using SerpAPI
            result = client.search(
                q=search_text,  # Use the actual search query
                engine="google",
                location="India",
                hl="en",
                gl="IN"
            )

            # Extract organic search results
            results = [
                {
                    "title": item["title"],
                    "link": item["link"],
                    "snippet": item["snippet"],
                    "displayed_link": item["displayed_link"],
                    "price": item.get("price", "N/A"),
                    "image": item.get("thumbnail", "N/A")
                }
                for item in result.get("organic_results", [])
            ]

    # Render the shoping.html template with results
    return render_template('shoping.html', results=results, search_text=search_text)

@app.route('/food', methods=['GET','POST'])
def food():
    results = []  # Default empty results
    search_text = None  # Default search text

    if request.method == 'POST':
        # Get the search query from the form
        search_text = request.form.get('search_text')
        if not search_text:
            flash("Please enter a search query", "error")
        else:
            # Perform the search using SerpAPI
            result = client.search(
                q=search_text,  # Use the actual search query
                engine="google",
                location="India",
                hl="en",
                gl="IN"
            )

            # Extract organic search results
            results = [
                {
                    "title": item["title"],
                    "link": item["link"],
                    "snippet": item["snippet"],
                    "displayed_link": item["displayed_link"],
                    "price": item.get("price", "N/A"),
                    "image": item.get("thumbnail", "N/A")
                }
                for item in result.get("organic_results", [])
            ]

    # Render the shoping.html template with results
    return render_template('food.html',results=results, search_text=search_text)

@app.route('/hotel',methods=['GET','POST'])
def hotel():
    results = []  # Default empty results
    search_text = None  # Default search text

    if request.method == 'POST':
        # Get the search query from the form
        search_text = request.form.get('search_text')
        if not search_text:
            flash("Please enter a search query", "error")
        else:
            # Perform the search using SerpAPI
            result = client.search(
                q=search_text,  # Use the actual search query
                engine="google",
                location="India",
                hl="en",
                gl="IN"
            )

            # Extract organic search results
            results = [
                {
                    "title": item["title"],
                    "link": item["link"],
                    "snippet": item["snippet"],
                    "displayed_link": item["displayed_link"],
                    "price": item.get("price", "N/A"),
                    "image": item.get("thumbnail", "N/A")
                }
                for item in result.get("organic_results", [])
            ]

    # Render the shoping.html template with results
    
    return render_template('hotel.html',results=results, search_text=search_text)

@app.route('/travel',methods=['GET','POST'])
def travel():
    results = []  # Default empty results
    search_text = None  # Default search text

    if request.method == 'POST':
        # Get the search query from the form
        search_text = request.form.get('search_text')
        if not search_text:
            flash("Please enter a search query", "error")
        else:
            # Perform the search using SerpAPI
            result = client.search(
                q=search_text,  # Use the actual search query
                engine="google",
                location="India",
                hl="en",
                gl="IN"
            )

            # Extract organic search results
            results = [
                {
                    "title": item["title"],
                    "link": item["link"],
                    "snippet": item["snippet"],
                    "displayed_link": item["displayed_link"],
                    "price": item.get("price", "N/A"),
                    "image": item.get("thumbnail", "N/A")
                }
                for item in result.get("organic_results", [])
            ]

    # Render the shoping.html template with results
    
    return render_template('travelling.html',results=results, search_text=search_text)

@app.route('/about')
def about():

    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
