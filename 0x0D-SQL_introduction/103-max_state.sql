-- import table dump into `hbtn_0c_0` database in MySQL server.
-- display the max temperature of eaach state ordered by state's name.

SELECT `state`, MAX(`value`) AS `max_temp`
FROM temperatures
GROUP BY `state`
ORDER BY `state`;
