-- lists all shows from `hbtn_0d_tvshows_rate` by their rating
-- each record displays: `tv_shows.title` - `rating_sum`
-- results are sorted in descending order by rating

SELECT title, SUM(rate) AS rating
  FROM `tv_shows` AS ts
       INNER JOIN tv_show_ratings AS rt
       ON ts.id = rt.show_id
 GROUP BY title
 ORDER BY rating DESC;
