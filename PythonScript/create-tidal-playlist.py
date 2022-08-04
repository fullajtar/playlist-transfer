import tidalapi
import json
session = tidalapi.Session()

access_token = None
session_id = None

try:
    access_token = open('PythonScript/access_token.txt', 'r').read()
    session_id = open('PythonScript/session_id.txt', 'r').read()
except:
    access_token = None
    session_id = None


if (access_token and session_id):
    try:
        # Will run until you visit the printed url and link your account
        session.load_oauth_session(session_id=session_id, token_type='Bearer',access_token=access_token)
    except:
        session.login_oauth_simple()
        f = open('PythonScript/access_token.txt', 'w')
        f.write(session.access_token)
        f.close()

        f = open('PythonScript/session_id.txt', 'w')
        f.write(session.session_id)
        f.close()
else:
    session.login_oauth_simple()
    f = open('PythonScript/access_token.txt', 'w')
    f.write(session.access_token)
    f.close()

    f = open('PythonScript/session_id.txt', 'w')
    f.write(session.session_id)
    f.close()

# try:
#     playlist = open('example.json')
# except:
#     print("Couldnt load playlist file for transferring to TIDAL")
#     exit()

spotify_playlist_string = '''
[{"artist_name":"Joji", "track_name":"MODUS", "track_album":"Nectar"},{"artist_name":"Joji", "track_name":"Glimpse of Us", "track_album":"Glimpse of Us"},{"artist_name":"Maduk", "track_name":"Go Back To The Jungle", "track_album":"Transformations"}]
'''
spotify_playlist = json.loads(spotify_playlist_string)
tidal_tracks_IDs = []

for track_spotify in spotify_playlist:
    result = session.search('track', track_spotify['track_name'])
    print('----------------')
    print('Searching: ',track_spotify['track_name'])

    for track in result.tracks[0:3]:
        if track.name == track_spotify['track_name'] and track.artist.name == track_spotify['artist_name'] and track.album.name == track_spotify['track_album']:
            print("BINGO!")
            # print("TrackName: ",track.name)
            # print("ArtistName: ",track.artist.name)
            # print("AlbumName: ",track.album.name)
            # print(track.id)
            tidal_tracks_IDs.append(track.id)

print("IDs: ", tidal_tracks_IDs)