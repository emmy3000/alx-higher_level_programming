-- lists all records of `second_table` of `hbtn_0c_0` database in MySQL server.
-- record of scores will be in a descending order

SELECT `score`, `name`
FROM `second_table`
ORDER BY `score` DESC;
