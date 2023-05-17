-- displays cities with their temperatures measured in Fahrenheit.
-- temperature values will be listed in a descending order

SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
