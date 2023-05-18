-- lists all shows and genres linted to them from `hbtn_0d_tvshows` database
-- if a show doesn't have a genre, NULL us displayed in the genre column
-- each record displays: `tv_shows.title` - `tv_genres.name`
-- results are sorted in an ascending order by the show's title and genre name

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
