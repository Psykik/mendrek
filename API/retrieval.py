import httpx
request = httpx.get("http://www.omdbapi.com/?t=Apothecary+Diaries&apikey=b8b9d254")
print(request.text)