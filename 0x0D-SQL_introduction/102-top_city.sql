-- Import in `hbtn_0c_0` database a table from an external table dump.
-- displays the top 3 cities temperature during July & August.
-- temperature values will be listed in descending order.

SELECT `city`, MAX(`value`) AS `avg_temp`
FROM `temperatures`
WHERE `month` IN (7, 8)
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;
