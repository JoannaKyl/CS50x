Select people.name
from people
JOIN stars on people.id = stars.person_id
Where stars.movie_id = (Select id from movies where title ="Toy Story")



