-- lists all cities contained in the `hbtn_0d_usa` database in MySQL server
-- each record displays `cities.id` - `cities.name` - `states.name`
-- results are sorted in an ascending order by `cities.id`

SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id;
