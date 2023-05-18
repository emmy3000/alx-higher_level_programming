-- lists all genres of the show Dexter from the `hbtn_0d_tvshows` database.
-- each record displays: `tv_genres.name`
-- results are sorted in an ascending order by the genre name.

SELECT g.name
FROM tv_shows AS s
JOIN tv_show_genres AS sg ON s.id = sg.show_id
JOIN tv_genres AS g ON sg.genre_id = g.id
WHERE s.title = 'Dexter'
ORDER BY g.name ASC;
