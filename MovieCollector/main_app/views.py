from django.shortcuts import render

class Movie:
    def __init__(self, title, director, genre, description, released):
        self.title = title
        self.director = director
        self.genre = genre
        self.description = description
        self.released = released

# Create a list of Cat instances
movies = [
    Movie('Avengers', 'Joss Whedon', 'Action, Adventure, Sci-Fi', 'The Avengers face off against Ultron, an AI created by Tony Stark and Bruce Banner, who aims to bring about world peace through human extinction.', 2015),
    Movie('The Bank Job', 'Roger Donaldson', 'Heist, Action, Drama, Suspense, Crime Film','Loosely based on the 1971 "Walkie-Talkie Robbery," following a small-time car dealer, Terry, who is lured into a bank heist by his ex-girlfriend, Martine, unaware that the true target is a safety deposit box containing compromising photos of a royal, leading to a dangerous game of cat and mouse with government agents, gangsters, and corrupt cops', 2008),
    Movie('Hustle & Flow', 'Craig Brewer', 'Music, Romance, Comedy, Drama','A 2005 crime drama musical film about a Memphis pimp in a mid-life crisis who, with the help of friends, attempts to become a successful hip-hop emcee, inspired by his life on the streets.', 2005),
    Movie('Friday', 'Steve Carr, Marcus Raboy, F. Gary Gray', 'Comedy, Drama','"Friday" follows Craig Jones (Ice Cube) and Smokey (Chris Tucker) as they navigate a chaotic Friday afternoon in their South Central Los Angeles neighborhood, dealing with a drug dealer, a neighborhood bully, and various other antics', 1995),
    Movie('School Dance','Nick Cannon','Comedy, Drama', 'A school dance is a dance event, often themed or celebrating a specific occasion, organized and sponsored by a school, providing students with a supervised and social space to enjoy music and dancing.', 2014)
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def movie_index(request):
    return render(request, 'movies/index.html', {'movies': movies})