$curlpath = 'C:\Windows\System32\curl.exe'
$playlistId = '0w1Mjpwt3vDVHsFwna20FS'
$token = "BQBD9RoAG5crfnbpKB5xQLJKMMyGNfzWHhyRaxvMdjS8dMiGLAQZftCZ7i8pdnWzh8tnDSAUbv0fOMZpzw8xwp3ibsUDS7zwgKv-Hb7nW6NvpLmzgNPT2uqpy1WkCda0-B8quSp9gIRSWAsWxv4WZ_FF2xiKa_fMV_D6cAbU8lHDV-Suz1RNDfjf-6xjmSmWXQWeALpUAFMhX5Ux"
$response = & $curlpath -X "GET" "https://api.spotify.com/v1/playlists/$($playlistId)/tracks" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer $($token)"
$playlist = $response | ConvertFrom-Json

$jsonString = '['
foreach ($song in $playlist.items){
    $jsonString += '{"artist_name":"'+$song.track.artists.name+'", "track_name":"'+$song.track.name+'", "track_album":"'+$song.track.album.name+'"},'
}
$jsonString = $jsonString.Substring(0, $jsonString.Length-1)
$jsonString += ']'

$myJsonObj = $jsonString | ConvertFrom-Json
Write-Output $myJsonObj