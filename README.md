# Spotify Songs Classifier
## Motivation for the project
Recently Spotify rolled out a new feature to categorise songs of 'Liked Songs' into different genres. This feature was released in a few english speaking nations. The motivation for
this project was derived from here. Songs can be classified into different genres based on some of their features. Truly speaking, there is no one easy way to classify these songs based on these 
features. But, some song features like Loudness, instrumentaness and speechiness can pave for the genre classification. 

## Features
~ A user can just paste the playlist id and all the songs in the playlist will be classified into 7 different genres namely, Pop, Rock, Hip Hop, Jazz, Blues, Folk/Accoustic and Metal  
~ The project makes use of a Multi-label classifier ML model to classify the songs into these genres.  
~ The song features used to classify a song are pulled from Spotify API.  
~ The training data for the model was also pulled from Spotify API and were categorised into variuos genres based on Spotify recommendation.
