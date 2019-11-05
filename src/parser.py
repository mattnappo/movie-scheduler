import csv, json

movies = []

with open('assets/watchlist.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        movie = {
            'movie': row[1],
            'url': row[3]
        }

        movies.append(movie)

with open('assets/watchlist.json', 'w') as json_file:
    json_file.write(json.dumps(movies))