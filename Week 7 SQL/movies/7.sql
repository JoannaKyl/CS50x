SELECT movies.title , ratings.rating
from movies
JOIN ratings on movies.id = ratings.movie_id
Where movies.year = 2010 and ratings.rating > 0
ORDER BY ratings.rating DESC , movies.title ASC;
