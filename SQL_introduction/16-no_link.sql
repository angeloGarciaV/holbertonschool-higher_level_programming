--  lists all records of second_table that has a name
SELECT * FROM second_table
WHERE name IS NOT NULL and name <> ''
ORDER BY score DESC;
