-- lists all genres not linked to the show Dexter in the `hbtn_0d_tvshows` database
-- each record displays `tv_genres.name`
-- results are sorted in an ascending order by genre name

SELECT g.name
FROM tv_genres AS g
LEFT JOIN (
	SELECT sg.genre_id
	FROM tv_show_genres AS sg
	JOIN tv_shows AS s ON sg.show_id = s.id AND s.title ='Dexter'
) AS s
ON g.id = s.genre_id
WHERE s.genre_id IS NULL
ORDER BY g.name;
