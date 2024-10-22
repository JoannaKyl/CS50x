SELECT movies.title
FROM movies
JOIN stars stars0 ON movies.id = stars0.movie_id
JOIN stars stars1 ON movies.id = stars1.movie_id
JOIN people people0 ON people0.id = stars0.person_id
JOIN people people1 ON people1.id = stars1.person_id
WHERE people0.name ='Bradley Cooper'
AND people1.name ='Jennifer Lawrence'




