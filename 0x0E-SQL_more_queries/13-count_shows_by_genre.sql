-- lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each.
-- each record displays: `<TV Show genre>`- `<Number of shows linked to this genre>`
-- first column is called `genre`
-- second column is called `number_of_shows`
-- genres without any shows linked are not displayed
-- results are sorted in descending order by the number of shows linked

SELECT g.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres AS g
INNER JOIN tv_show_genres AS sg ON g.id = sg.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
