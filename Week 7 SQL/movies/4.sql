SELECT count(title) title
from movies
JOIN ratings ON id = movie_id
Where ratings.rating = 10;

