-- list all records of `second_table` of `htbn_0c_0` database.
-- rows on't be listed withoit names
-- records will be displayed in descending order

SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ''
ORDER BY `score` DESC;
