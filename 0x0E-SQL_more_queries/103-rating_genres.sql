-- lists all genres in the `hbtn_0d_tvshows_rate` database by their rating
-- each record displays: `tv_genres.name` - `rating_sum`
-- results are sorted in descending order by rating

SELECT name, SUM(rate) AS rating_sum
  FROM tv_genres AS tg
       INNER JOIN tv_show_genres AS ts
       ON ts.genre_id = tg.id

       INNER JOIN tv_show_ratings AS rt
       ON rt.show_id = ts.show_id
 GROUP BY name
 ORDER BY rating_sum DESC;
