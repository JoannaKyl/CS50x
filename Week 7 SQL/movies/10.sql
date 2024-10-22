SELECT DISTINCT(name)
FROM people
JOIN directors ON people.id = directors.person_id
JOIN ratings on directors.movie_id = ratings.movie_id
Where ratings.rating >= 9
