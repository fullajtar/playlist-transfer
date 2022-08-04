$curlpath = 'C:\Windows\System32\curl.exe'
$playlistId = '0w1Mjpwt3vDVHsFwna20FS'
$token = "BQB5feIz1Z_UT8DRdlCEBMLDFVUGlLJ45AYPX3H-5PLD7-guethzc0I7tl0eH3swy0UlvljZlQANat_kpY3ujnELe1p-WqqJ10SzBOaZCJYbs3st_PzVNZgQ-T29GWDWMSSnZag6ipqYVN-8G37DT4RVWd9bmFJLi2ic09mC65hHTR6FAg4UtKO4CELx8Et01RiBV3l5RgQdIpXVOVd3eVu8s_M3F4XgOWM"
$response = & $curlpath -X "GET" "https://api.spotify.com/v1/playlists/$($playlistId)/tracks" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer $($token)"
$playlist = $response | ConvertFrom-Json

$jsonString = '['
foreach ($song in $playlist.items){
    $jsonString += '{"artist_name":"'+$song.track.artists.name+'", "track_name":"'+$song.track.name+'", "track_album":"'+$song.track.album.name+'"},'
}
$jsonString = $jsonString.Substring(0, $jsonString.Length-1)
$jsonString += ']'

$jsonString  | Out-File "C:\Users\Fullajtar\Documents\playlist-transfer\example.json"