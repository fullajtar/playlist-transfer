import tidalapi
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


result = session.search('album', 'Nectar')

for album in result.albums:
    print(album.artist.name)