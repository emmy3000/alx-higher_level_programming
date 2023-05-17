-- displays cities with their temperatures measured in Fahrenheit.
-- temperature values will be listed in a descending order

SELECT `city`, AVG(value) AS `average_temperature`
FROM `temperatures`
GROUP BY `city`
ORDER BY `average_temperature` DESC;
