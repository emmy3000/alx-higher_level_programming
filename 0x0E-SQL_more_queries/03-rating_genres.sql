-- lists all genres in `hbtn_0d_tvshows_rate` by their rating
-- each record displays: `tv_genres.name` - `rating_sum`
-- results are sorted in descending order by rating

SELECT tv_genres.name, SUM(tv_show_ratings.rating) AS rating_sum
FROM tv_show_ratings
JOIN tv_shows ON tv_show_ratings.tv_show_id = tv_shows.id
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
