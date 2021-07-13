import os
import logging
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from google.cloud import bigquery

logger = logging.getLogger()

def get_tracks_data(spotify_client, query, chunk_size, max_results):

    tracks_data_list = []
    single_track_dict = {}

    for i in range(0, max_results, chunk_size):
        try:
            track_results = spotify_client.search(q=query, type='track', limit=50,offset=i)
            for i, track in enumerate(track_results['tracks']['items']):                              
                single_track_dict = {                                       
                    'track_name': track['name'],
                    'artist_name': track['artists'][0]['name'],
                    'track_id': track['id']            
                }
                tracks_data_list.append(single_track_dict)
        except Exception as e:
            print(e)
            logger.info(e)
            continue

    return tracks_data_list

def get_audio_features_data(spotify_client, track_ids, chunk_size):
    audio_features_list = []

    for i in range(0, len(track_ids), chunk_size):    
        try:
            track_id_list = track_ids[i:i+chunk_size]
            results = spotify_client.audio_features(track_id_list)
            results = [dict({'id':'None'}) if v is None else v for v in results]
            audio_features_list.extend(results)
        except Exception as e:
            print(e)
            logger.info(e)
            continue
    return audio_features_list

def insert_bigquery(client, project_id, dataset_id, table_id, data):

    table_id = "{}.{}.{}".format(project_id, dataset_id, table_id)
    job_config = bigquery.LoadJobConfig(autodetect=True, write_disposition=bigquery.WriteDisposition.WRITE_APPEND, schema_update_options = bigquery.SchemaUpdateOption.ALLOW_FIELD_ADDITION)
    job = client.load_table_from_json(destination=table_id, json_rows=data, job_config=job_config)

    logger.info("Successfully uploaded to table {}".format(table_id))


def get_spotify_audio_features_data_to_bigquery(event, context):
    """
    This function combines data from 2 Spotify endpoints:
    1. v1/search
    2. v1/audio-features
    and loads it into BigQuery
    """

    client_id = os.environ['CID']
    client_secret = os.environ['SECRET']
    project_id = os.environ['PROJECT_ID']
    dataset_id = os.environ['DATASET_ID']
    table_id = os.environ['TABLE_ID']

    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    spotify_client = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        
    tracks_data_list = get_tracks_data(spotify_client, 'year:2021', 50, 1000)
    track_ids = [d['track_id'] for d in tracks_data_list]
    audio_features_list = get_audio_features_data(spotify_client, track_ids, 100)
    merged_list = [{**u, **v} for u, v in zip(tracks_data_list, audio_features_list)]
    
    client = bigquery.Client()

    insert_bigquery(client, project_id, dataset_id, table_id, merged_list)