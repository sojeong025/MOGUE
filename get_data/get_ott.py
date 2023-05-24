import json
import requests

check_list = []
total_data = []

otts = [2, 3, 8, 97, 192, 337]
k = 0
j = 0
file_path = "C:/Users/SSAFY/Desktop/final_pjt/back_server/movies/fixtures/movies.json"
with open(file_path, encoding='utf-8') as f:
    data = json.load(f)

for movie in data:
    url = f"https://api.themoviedb.org/3/movie/{movie['pk']}/watch/providers"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5OTc1NzVjZGE4MzFkY2VhZWM3ZWY2ZDMxZDZjNjc5NCIsInN1YiI6IjYzZDMzOTU4NjZhZTRkMDA4YzkyYTM4OCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ZUxmsj6U1koqcc3GGoYrAUoSO3uh6PVngcT3O0zMxpI"
    }

    response = requests.get(url, headers=headers).json()
    if 'KR' in response['results']:

        if 'buy' in response['results']['KR']:
            for a in response['results']['KR']['buy']:
                if a['provider_id'] in otts and (movie['pk'], a['provider_id']) not in check_list:
                    data = {
                        "model": "movies.ott_movies",
                        "pk": k,
                        'fields': {
                            'ott_id': a['provider_id'],
                            'movie_id': movie['pk']
                        }
                    }
                    total_data.append(data)
                    check_list.append((movie['pk'], a['provider_id']))
                    k += 1

        if 'flatrate' in response['results']['KR']:
            for a in response['results']['KR']['flatrate']:
                if a['provider_id'] in otts and (movie['pk'], a['provider_id']) not in check_list:
                    data = {
                        "model": "movies.ott_movies",
                        "pk": k,
                        'fields': {
                            'ott_id': a['provider_id'],
                            'movie_id': movie['pk']
                        }
                    }
                    total_data.append(data)
                    check_list.append((movie['pk'], a['provider_id']))
                    k += 1

        if 'rent' in response['results']['KR']:
            for a in response['results']['KR']['rent']:
                if a['provider_id'] in otts and (movie['pk'], a['provider_id']) not in check_list:
                    data = {
                        "model": "movies.ott_movies",
                        "pk": k,
                        'fields': {
                            'ott_id': a['provider_id'],
                            'movie_id': movie['pk']
                        }
                    }
                    total_data.append(data)
                    check_list.append((movie['pk'], a['provider_id']))
                    k += 1

        j += 1
        print(j)

with open("ott_movies.json", "w", encoding="utf-8") as w:
    json.dump(total_data, w, indent="\t", ensure_ascii=False)
