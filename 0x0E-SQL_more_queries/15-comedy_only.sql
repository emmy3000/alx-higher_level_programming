-- lists all Comedy shows in the database `hbtn_0d_tvshows`
-- the `tv_genres` table contains only one record where `name` = Comedy (but with different id)
-- each record displays `tv_shows.title`
-- results are sorted in an ascending irder by the show's `title`

SELECT ts.title
FROM tv_shows AS ts
JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id
JOIN tv_genres AS tg ON tsg.genre_id = tg.id
WHERE tg.name = 'Comedy'
ORDER BY ts.title ASC;
