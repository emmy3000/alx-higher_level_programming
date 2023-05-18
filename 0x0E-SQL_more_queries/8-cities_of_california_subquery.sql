-- lists all the cities of California in the `hbtn_0d_usa` database
-- results are sorted in an ascending order by cities.id
-- no JOIN keyowrd was used

SELECT `id`, `name`
FROM `cities`
WHERE `state_id` IN (
	SELECT `id`
	FROM `states`
	WHERE `name` = 'California'
)
ORDER BY `id` ASC;
