-- lists all shows without the genre 'Comedy' in the database `hbtn_0d_tvshows`
-- the `tv_genres` table contains only one record where name = 'Comedy' (but the id can be different)
-- each record displays: `tv_shows.title`
-- results are sorted in an ascending order by the show title
-- maximum of two SELECT statements are allowed to be used

SELECT t.title
FROM tv_shows AS t
LEFT JOIN (
    SELECT DISTINCT show_id
    FROM tv_show_genres
    WHERE genre_id = (
        SELECT id
        FROM tv_genres
        WHERE name = 'Comedy'
    )
) AS c ON c.show_id = t.id
WHERE c.show_id IS NULL
ORDER BY t.title;
