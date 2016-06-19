import fresh_tomatoes
import media

"""List of my favorite movies and their title, storyline, poster image, and trailer"""

crouching_tiger = media.Movie("Crouching Tiger, Hidden Dragon", "Chinese warriors battle to find a great sword.",
                            "https://upload.wikimedia.org/wikipedia/en/9/97/Crouching_tiger_hidden_dragon_poster.jpg",
                            "https://www.youtube.com/watch?v=gLpZ_5bHmo8")

moonrise_kingdom = media.Movie("Moonrise Kingdom", "Coming-of-age movie where two twelve year olds run away one summer.",
                            "https://upload.wikimedia.org/wikipedia/en/4/4f/Moonrise_Kingdom_FilmPoster.jpeg",
                            "https://www.youtube.com/watch?v=eP0QJ_Ba1Bs")

bullets_over_broadway = media.Movie("Bullets Over Broadway",
                            "Struggling playwright makes a deal with mobster to let the mobster's girlfriend play lead in his play in exchange for financing",
                            "https://upload.wikimedia.org/wikipedia/en/b/bf/Bullets_over_Broadway_movie_poster.jpg",
                            "https://www.youtube.com/watch?v=qOEXK0aVfvE")

lost_in_translation = media.Movie("Lost in Translation",
                            "A lonely aging movie star and a conflicted newlywed meet and form a bond in Tokyo.",
                            "https://upload.wikimedia.org/wikipedia/en/4/4c/Lost_in_Translation_poster.jpg",
                            "https://www.youtube.com/watch?v=W6iVPCRflQM")

twenty46 = media.Movie("2046",
                            "A sci-fi writer engages in numerous affairs with women who inspire his writings in this movie where fiction blends with reality.",
                            "https://upload.wikimedia.org/wikipedia/en/a/a3/2046_movie.jpg",
                            "https://www.youtube.com/watch?v=3Tz6KgPfeuk")

taxi_driver = media.Movie("Taxi Driver",
                            "A New York City cab driver grows increasingly detached from reality and plot to kill a presidential candidate.",
                            "https://upload.wikimedia.org/wikipedia/en/c/c9/Taxi_Driver_poster.JPG",
                            "https://www.youtube.com/watch?v=cujiHDeqnHY")

movies = [taxi_driver, twenty46, lost_in_translation, moonrise_kingdom, crouching_tiger, bullets_over_broadway]

fresh_tomatoes.open_movies_page(movies)
