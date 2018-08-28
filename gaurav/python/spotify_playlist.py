playlist={
	"title":"my playlist",
	"author":"gaurav",
	"songs":[
	{"name":"numb","duration":4,"artist":["eminem"]},
	{"name":"rockabye","duration":3.5,"artist":["clean bandit"]},
	{"name":"girls like you","duration":5.3,"artist":["maroon5"]},
	{"name":"scared to be lonely","duration":4.2,"artist":["martin garrix"]}
	]
}
duration=0;
for song in playlist["songs"]:
	duration+=song["duration"]

print(f"duration is {duration} mins")