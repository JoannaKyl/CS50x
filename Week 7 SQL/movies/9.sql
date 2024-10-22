Select distinct(name)
from people
JOIN stars on people.id = stars.person_id
JOIN movies on stars.movie_id = movies.id
WHERE movies.year =2004
ORDER by people.birth


