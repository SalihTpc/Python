def song_decoder(song):
    song = song.replace("WUB", " ")
    return " ".join(song.split())

print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))
print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))
