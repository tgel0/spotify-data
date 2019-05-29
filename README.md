# 🎧 Spotify Data Project

A full-stack data project utilizing audio features data from the official Spotify Web API.

<p align="center">
<img align="center" src="https://github.com/tgel0/spotify-data/blob/master/GCP_diagram.png?raw=true">
</p>

## 🌱 Motivation

Main motivation for this project was to get practical experience in all the steps of a data project including setting up a data retrieval pipeline from scratch, analyzing and gaining insights from data as well as data modeling, using Python, SQL, Bash and GCP.

## 📓 Notebooks

* Data retrieval: [github](https://github.com/tgel0/spotify-data/blob/master/notebooks/SpotifyDataRetrieval.ipynb) | [nbviewer](http://nbviewer.jupyter.org/github/tgel0/spotify-data/blob/master/notebooks/SpotifyDataRetrieval.ipynb)
* Data exploration: [github](https://github.com/tgel0/spotify-data/blob/master/notebooks/SpotifyDataExploPopularity.ipynb) | [nbviewer](http://nbviewer.jupyter.org/github/tgel0/spotify-data/blob/master/notebooks/SpotifyDataExploPopularity.ipynb)
* Modeling: **TBA**

## 📁 Datasets

Data is available on [Kaggle](https://www.kaggle.com/tomigelo/spotify-audio-features) (latest update: April 2019)


## 📝 Blog Posts

+ ['A Whole New World: Going Serverless with GCP (Aladdin-style)'](https://tgel0.github.io/blog/A-Whole-New-World-Going-Serverless-with-GCP-Aladdin-Style/)
+ ['Spotify Data Project Part 1 - from Data Retrieval to First Insights' on tgel0.github.io](https://tgel0.github.io/blog/spotify-data-project-part-1-from-data-retrieval-to-first-insights/) and republished by [Towards Data Science on Medium.com](https://towardsdatascience.com/spotify-data-project-part-1-from-data-retrieval-to-first-insights-f5f819f8e1c3)
+ ['Using Data to Find the Most Popular Tracks of the Summer on Spotify' on Medium.com](https://medium.com/@tgel0/kiki-do-you-analyze-me-using-data-to-find-the-most-popular-tracks-of-the-summer-on-spotify-67ba8ef5773c)

## 🛠️ Built With

### 🖥️ APIs

+ [Spotify Web API](https://developer.spotify.com/documentation/web-api/)

### ☁️ GCP services

+ [Cloud Functions](https://cloud.google.com/functions/) + [Cloud Scheduler](https://cloud.google.com/scheduler/)
+ [BigQuery](https://cloud.google.com/bigquery/)

### 🐍 Python libraries:

* [Pandas](http://pandas.pydata.org/), [Numpy](http://www.numpy.org/) - data analysis
* [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/) - data visualization
* [Spotipy](https://spotipy.readthedocs.io/) - access to Spotify Web API
