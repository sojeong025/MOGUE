import requests
import json

TMDB_API_KEY = '997575cda831dceaec7ef6d31d6c6794'

total_data = []
k = 0
for i in range(1, 251):
    request_popular_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
    
    popular = requests.get(request_popular_url).json()
    for movie in popular['results']:
        print(movie)
        if movie['release_date'] and movie['overview'] and movie['poster_path']:
            request_movie_detail_url = f"https://api.themoviedb.org/3/movie/{movie['id']}?api_key={TMDB_API_KEY}&language=ko-KR"
            detail = requests.get(request_movie_detail_url).json()
            data = {
                "model": 'movies.movie',
                'pk': movie['id'],
                'fields': {
                    'title': movie['title'],
                    'release_date': movie['release_date'],
                    'overview': movie['overview'],
                    'popularity': movie['popularity'],
                    'runtime': detail['runtime'],
                    'vote_count': movie['vote_count'],
                    'poster_path': movie['poster_path'],
                }
            }
            print(k)
            k += 1
            total_data.append(data)
        
with open("movies.json", "w", encoding="utf-8") as w:
    json.dump(total_data, w, indent="\t", ensure_ascii=False)
