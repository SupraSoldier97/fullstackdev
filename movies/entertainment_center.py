import fresh_tomatoes
import media

# Gladiator movie: title, storyline, poster link and youtube trailer
gladiator = media.Movie(
    "Gladiator",
    "A Roman General cast from his position by the Emperor's jealous and "
    "murderous son",
    "https://20ui41tp7v127j03rcnp97oh-wpengine.netdna-ssl.com/wp-content/uploads/2013/10/gladiatorbg.jpg",  # NOQA
    "https://www.youtube.com/watch?v=AxQajgTyLcM"
)

# Avatar movie: title, storyline, poster link and youtube trailer
avatar = media.Movie(
    "Avatar",
    "A Marine on an alien planet",
    "http://www.impawards.com/2009/posters/avatar_xlg.jpg",
    "https://www.youtube.com/watch?v=cRdxXPV9GNQ"
)

# Navy SEALs movie: title, storyline, poster link and youtube trailer
navy_seals = media.Movie(
    "Navy SEALs",
    "Badass operators take the fight to the terrorists",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTAzODQzOTk5MTheQTJeQWpwZ15BbWU2MDIwOTgzOQ@@._V1_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=Is16u0jr1bQ"
)

# Homeward Bound movie: title, storyline, poster link and youtube trailer
homeward_bound = media.Movie(
    "Homeward Bound",
    "Journey of three runaway pets on a search for their family",
    "http://img.moviepostershop.com/homeward-bound-the-incredible-journey-movie-poster-1992-1020271560.jpg",  # NOQA
    "https://www.youtube.com/watch?v=U8LO9hRL3fQ"
)

# To Go Viking movie: title, storyline, poster link and youtube trailer
to_go_viking = media.Movie(
    "To Go Viking",
    "Documentary on modern-day Viking reconstructionists",
    "http://www.impawards.com/2013/posters/to_go_viking_xlg.jpg",
    "https://www.youtube.com/watch?v=XdoI_XKUfcM"
)

# The Revenant movie: title, storyline, poster link and youtube trailer
the_revenant = media.Movie(
    "The Revenant",
    "Wildman crawls for weeks on his stomach looking for the "
    "murderer of his son",
    "http://beacon.nwciowa.edu/wp-content/uploads/2016/01/The-Revenant-2015-poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=QRfj1VCg16Y"
)

# Create list of movies that will be used in media file
movies = [
    gladiator, avatar, navy_seals,
    homeward_bound, to_go_viking, the_revenant
]

# Open HTML file in webbrowser via fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
