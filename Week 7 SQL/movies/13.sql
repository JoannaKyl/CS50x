SELECT people.name
FROM people
JOIN stars on people.id = stars.person_id
JOIN movies on stars.movie_id = movies.id
WHERE movies.id IN
(
SELECT movies.id
FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people on people.id = stars.person_id
WHERE people.name = "Kevin Bacon" and birth =1958
) and people.name != "Kevin Bacon"
