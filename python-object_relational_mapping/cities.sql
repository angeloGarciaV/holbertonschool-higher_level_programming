SELECT cities.name FROM cities
INNER JOIN states
ON state_id = states.id
WHERE states.name = 'California'
ORDER BY cities.id ASC;