SELECT AVG(energy)
FROM songs
WHERE artist_id =
(
    Select id
    FROM artists
    WHERE    name ="Drake"
)

