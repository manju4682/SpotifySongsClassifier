from ClientClass import SpotifyAPI
import csv
import json

def write_song_details(client,playlist_id,no_songs):
    with open("temp_song_details.csv",'w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id','name','duration','artist_name','is_explicit','popularity'])
        
        offset = 0
        limit = 50
        no_of_songs = 0
        while no_of_songs < no_songs:
            data = client.get_resource(playlist_id,offset,limit)
            for item in data['items']:
                song_details = []
                try:
                    song_details.append(item['track']['id'])
                    song_details.append(item['track']['name'])
                    song_details.append(item['track']['duration_ms'])
                    song_details.append(item['track']['artists'][0]['name'])
                    song_details.append(item['track']['explicit'])
                    song_details.append(item['track']['popularity'])
                    #print(song_details)
                    writer.writerow(song_details)
                    no_of_songs += 1
                except:
                        
                    no_of_songs += 1
                    continue
            offset += 50   
    print("Written song details...")   
    return "temp_song_details.csv" 


def write_audio_features(client,file):
    with open(file,'r') as file:
        reader = csv.reader(file)
        next(reader)
        count = 0
        str = ''
        with open("temp_songs_features.csv",'w',newline='') as writer_file:
            writer = csv.writer(writer_file)
            writer.writerow(['id','time_signature','danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo'])

            for row in reader:
                #print(row[0],row[1])
                str += row[0]
                str += ','
                count +=1
                if count==100:
                    #print(str[:-1])
                    data = client.get_audio_features(str[:-1])
                    for item in data['audio_features']:
                        li = []
                        try:
                            li.append(item['id'])
                            li.append(item['time_signature'])
                            li.append(item['danceability'])
                            li.append(item['energy'])
                            li.append(item['key'])
                            li.append(item['loudness'])
                            li.append(item['mode'])
                            li.append(item['speechiness'])
                            li.append(item['acousticness'])
                            li.append(item['instrumentalness'])
                            li.append(item['liveness'])
                            li.append(item['valence'])
                            li.append(item['tempo'])
                            #print(li)
                            writer.writerow(li)
                        except:
                            print("A none object found")  
                            writer.writerow(li)  
                    print("________________________________________________________")    
                    count = 0
                    str = ''
                    continue    

            data = client.get_audio_features(str[:-1])
            #print("The last bit")
            for item in data['audio_features']:
                li = []
                try:
                    li.append(item['id'])
                    li.append(item['time_signature'])
                    li.append(item['danceability'])
                    li.append(item['energy'])
                    li.append(item['key'])
                    li.append(item['loudness'])
                    li.append(item['mode'])
                    li.append(item['speechiness'])
                    li.append(item['acousticness'])
                    li.append(item['instrumentalness'])
                    li.append(item['liveness'])
                    li.append(item['valence'])
                    li.append(item['tempo'])
                    #print(li)
                    writer.writerow(li)
                except:
                    #print("A none object found")  
                    writer.writerow(li) 
    print("Written song features...")                
    return  "temp_songs_features.csv"                       

def combine_files(file1,file2):
    with open(file1,'r') as f1:
        with open(file2,'r') as f2:
            with open("temp_test.csv",'w',newline='') as f3:
                reader1 = csv.reader(f1)
                reader2 = csv.reader(f2)
                writer = csv.writer(f3)    
                next(reader1)
                next(reader2)      
                writer.writerow(['id','name','duration','artist_name','is_explicit','time_signature','danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo','popularity'])      
                for line1,line2 in zip(reader1,reader2):
                    li = []
                    if not line2:
                        continue
                    if line1[0]==line2[0]:
                        li.append(line1[0])
                        li.append(line1[1])
                        li.append(line1[2])
                        li.append(line1[3])
                        li.append(line1[4])
                        li.append(line2[1])
                        li.append(line2[2])
                        li.append(line2[3])
                        li.append(line2[4])
                        li.append(line2[5])
                        li.append(line2[6])
                        li.append(line2[7])
                        li.append(line2[8])
                        li.append(line2[9])
                        li.append(line2[10])
                        li.append(line2[11])
                        li.append(line2[12])
                        li.append(line1[5])
                        #print(li)
                        writer.writerow(li)
    print("Combined files...")
    return 'temp_test.csv'

def write_genre_data(file1,file2):
    with open(file1,'r',encoding='utf8') as file1:
        with open(file2, 'r') as file2:
            reader = csv.reader(file1)
            next(reader)
            reading = csv.reader(file2)
            next(reading)
            dict = {}
            count = 0
            for row in reader:
                list = row[5].split(',')
                stripped = [i.strip() for i in list]
                dict[row[1]] = stripped
            print(len(dict))  
            with open("finalplaylist3.csv",'w',newline='') as write:
                writer = csv.writer(write)
                header = ['id','name','duration','artist_name','is_explicit','time_signature','danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo','popularity','Pop','Rock','Hip Hop','Folk','Metal','Blues','Jazz']
                writer.writerow(header)
                for row in reading:
                    genre = dict.get(row[1])
                    if not genre:
                        continue
                    if 'Pop' in genre:
                        row.append(1)
                    else:
                        row.append(0)
                    if 'Rock' in genre:
                        row.append(1)
                    else:
                        row.append(0) 
                    if 'Hip Hop' in genre:
                        row.append(1)
                    else:
                        row.append(0) 
                    if 'Folk/Acoustic' in genre:
                        row.append(1)
                    else:
                        row.append(0)
                    if 'Metal' in genre:
                        row.append(1)
                    else:
                        row.append(0)
                    if 'Blues' in genre:
                        row.append(1)
                    else:
                        row.append(0)
                    if 'Jazz' in genre:
                        row.append(1)
                    else:
                        row.append(0)      
                    writer.writerow(row)
                    count+=1
                print(count)    


