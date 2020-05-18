SELECT name FROM people
WHERE id IN (SELECT person_id FROM stars
WHERE movie_id IN (SELECT movie_id FROM movies
JOIN stars ON stars.movie_id = movies.id
JOIN people ON stars.person_id = people.id
WHERE people.name = "Kevin Bacon" AND
people.birth = 1958))
AND name != "Kevin Bacon";
