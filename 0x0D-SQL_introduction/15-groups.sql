-- lists number of records with the same score in `second_table`
-- `score` will be displayed & number of `score` record will be labelled `number`
-- values will be in a descending order.

SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
