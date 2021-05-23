# Spotify Songs Classifier
## Motivation for the project
Recently Spotify rolled out a new feature to categorise songs of 'Liked Songs' into different genres. This feature was released in a few english speaking nations. The motivation for this project was derived from here. Songs can be classified into different genres based on some of their features. Truly speaking, there is no one easy way to classify these songs based on these features. But, some song features like Loudness, instrumentalness and speechiness can pave the way for deciding the genre a song belongs to. 

## Features
~ A user can just paste the playlist id and all the songs in the playlist will be classified into 7 different genres namely, Pop, Rock, Hip Hop, Jazz, Blues, Folk/Accoustic and Metal  
~ The project makes use of a Multi-label classifier ML model to classify the songs into these genres.  
~ The song features used to classify a song are pulled from Spotify API.  
~ The training data for the model was also pulled from Spotify API and were categorised into variuos genres based on Spotify recommendation.

## Implementation and Tools used
Initially a large amount of songs were collected belonging to several genres. Their genres were recorded. And then the song details and song features were pulled from different Spotify API endpoints. All that was stored in csv files. Then, using pandas data was cleaned to make it legible for machine learning. And then pandas statistics and seaborn libraries were used to decide on the features to be used for training the ML model. After thorough research, Random Forest multi-label model was chosen for the application. And then model was trained using sklearn package. And then joblib was used to save the model. joblib can be used to load the model to predict values.  
Several tools and technologies used during the course of this project:  
* panadas/numpy/matplotlib/seaborn
* sklearn
* Handling APIs
* json/csv file handling
* Understanding of several ML algorithms
* Training and testing ML models

## Conclusion and takeaways
Being a music lover myself, wanted to do something that concerned the music industry and probably benefit it. And this idea seemed interesting. It becomes difficult to classify a song into different genres based on their features. Because a song can belong to multiple genres. And challenging problems are also most fun to solve. And multi-label classification came in handy. Although it may not be the most accurate of the classifiers, it does fairly well to put a song into closest genre it might belong to. And this project did truly exposed me to a lot of different tools and technologies in ML domain. ML is a vast and ever growing domain. I am happy that I was able to do something to satisfy that music lover in me.
