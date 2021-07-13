# 🎧 Spotify Data Project

#### A serverless solution for getting the audio features data from the Spotify Web API into a BigQuery database.

<p align="center">
<img align="center" src="https://github.com/tgel0/spotify-data/blob/master/Spotify_data_diagram.png?raw=true">
</p>

## 💻 Installation
 1. Clone this repo
 2. Initialize gcloud `gcloud init`
 3. Deploy Cloud Function
```
gcloud functions deploy get_spotify_audio_features_data_to_bigquery --runtime python38 --trigger-topic spotify_topic --set-env-vars CID='YOUR_SPOTIFY_CID',SECRET='YOUR_SPOTIFY_SECRET',PROJECT_ID=YOUR_GCP_PROJECT_ID,DATASET_ID=YOUR_BIGQUERY_DATASET_NAME,TABLE_ID=YOUR_BIGQUERY_TABLE_NAME
```
4. Create a [Cloud Scheduler](https://cloud.google.com/scheduler/docs/quickstart) job to run automatically (optional)

## 🛠️ Built With

### 🖥️ APIs

+ [Spotify Web API](https://developer.spotify.com/documentation/web-api/)

### 🐍 Python libraries:

* [Spotipy](https://spotipy.readthedocs.io/) - Python wrapper for Spotify Web API

### ☁️ Google Cloud Platform services

+ [Cloud Functions](https://cloud.google.com/functions/) 
+ [BigQuery](https://cloud.google.com/bigquery/)
+ [Cloud PubSub](https://cloud.google.com/pubsub/)
+ [Cloud Scheduler](https://cloud.google.com/scheduler/)

## 🌱 Notebooks, Datasets, Blogs

+ Blog post ['Spotify Data Project Part 1 - from Data Retrieval to First Insights'](https://towardsdatascience.com/spotify-data-project-part-1-from-data-retrieval-to-first-insights-f5f819f8e1c3)
+ Blog post ['Using Data to Find the Most Popular Tracks of the Summer on Spotify'](https://medium.com/@tgel0/kiki-do-you-analyze-me-using-data-to-find-the-most-popular-tracks-of-the-summer-on-spotify-67ba8ef5773c)
+ Notebook part 1: data retrieval: [github](https://github.com/tgel0/spotify-data/blob/master/notebooks/SpotifyDataRetrieval.ipynb) | [nbviewer](http://nbviewer.jupyter.org/github/tgel0/spotify-data/blob/master/notebooks/SpotifyDataRetrieval.ipynb)
+ Notebook part 2: data exploration: [github](https://github.com/tgel0/spotify-data/blob/master/notebooks/SpotifyDataExploPopularity.ipynb) | [nbviewer](http://nbviewer.jupyter.org/github/tgel0/spotify-data/blob/master/notebooks/SpotifyDataExploPopularity.ipynb)
+ Dataset [via Kaggle](https://www.kaggle.com/tomigelo/spotify-audio-features) (latest update: April 2019)