def  make_album(artist_name,album_title, no_of_track=None):
    albums={}
    albums[artist_name]=album_title
    albums['tracks']=no_of_track
    return albums

one = make_album("DSP","Arya2")
second = make_album(artist_name="Thaman",album_title="SVP")
thrid = make_album("ARINUD","JALIER",5)
new =[one,second,thrid]
for i in new:
    print(i)