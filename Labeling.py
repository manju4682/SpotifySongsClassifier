import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import csv
import WriteData
from ClientClass import SpotifyAPI

def training_model(datafile):
    df = pd.read_csv(datafile)
    print(df.shape)

    # selecting the target lables
    y = ['Pop', 'Rock', 'Hip Hop', 'Folk', 'Metal', 'Blues','Jazz']
    Y = df[y]
    features = ['duration','is_explicit', 'time_signature',
       'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
       'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
       'popularity']
    X = df[features]   
    model = RandomForestClassifier(n_estimators=200)
    model.fit(X,Y)
    joblib.dump(model, "genre_model.joblib")

def get_genres(preds):
    list = []
    if preds[0]==1:
        list.append("Pop")
    if preds[1]==1:
        list.append("Rock")
    if preds[2]==1:
        list.append("Hip Hop")
    if preds[3]==1:
        list.append("Folk/Accoustic")
    if preds[4]==1:
        list.append("Metal")
    if preds[5]==1:
        list.append("Blues")
    if preds[6]==1:
        list.append("Jazz")       
    return list                     


def classifier(data):
    model = joblib.load("genre_model.joblib")
    predicts = model.predict(data)
    #print(predicts)
    return predicts

def print_song_by_genre(genre,songs):
    print(genre," songs")
    count = 1
    for song in songs:
        print(count,". ",song)
        count+=1
    print()    

def classify_songs(file):
    df = pd.read_csv(file)
    features = ['duration','is_explicit', 'time_signature',
       'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
       'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
       'popularity']
    feature_data = df[features]
    predictions = classifier(feature_data)
    print("Recieved predictions")
    Pop = []
    Rock = []
    Hip_Hop = []
    Folk_Accoustic = []
    Metal = []
    Blues = []
    Jazz = []
    with open(file,'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row,pred in zip(reader,predictions):
            #print(pred,row)
            if(pred[0]==1):
                Pop.append(row[1]+' by '+row[3])
            if(pred[1]==1):
                Rock.append(row[1]+' by '+row[3])
            if(pred[2]==1):
                Hip_Hop.append(row[1]+' by '+row[3])
            if(pred[3]==1):
                Folk_Accoustic.append(row[1]+' by '+row[3])
            if(pred[4]==1):
                Metal.append(row[1]+' by '+row[3])
            if(pred[5]==1):
                Blues.append(row[1]+' by '+row[3])
            if(pred[6]==1):
                Jazz.append(row[1]+' by '+row[3])               
    if Pop:                 
        print_song_by_genre("Pop",Pop)
    if Rock:                 
        print_song_by_genre("Rock",Rock)
    if Hip_Hop:                 
        print_song_by_genre("Hip Hop",Hip_Hop)
    if Folk_Accoustic:                 
        print_song_by_genre("Folk/Accoustic",Folk_Accoustic)
    if Metal:                 
        print_song_by_genre("Metal",Metal)
    if Blues:                 
        print_song_by_genre("Blues",Blues)
    if Jazz:                 
        print_song_by_genre("Jazz",Jazz)                                                                                            

def Do_classifying(client,playlist_id,no_of_songs):
    songs_file = WriteData.write_song_details(client,playlist_id,no_of_songs)
    features_file = WriteData.write_audio_features(client,songs_file)
    file = WriteData.combine_files(songs_file,features_file)
    classify_songs(file)

if __name__=="__main__":
    playlist_id = input("Paste the playlist id- ")
    no_of_songs = int(input("Enter no of songs in the playlist- "))
    client = SpotifyAPI('[API_KEY]', '[API_SECRET]')      
    print(client.get_access_token())   
    Do_classifying(client,playlist_id,no_of_songs)