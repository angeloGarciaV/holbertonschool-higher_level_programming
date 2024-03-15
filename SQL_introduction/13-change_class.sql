--  removes all records with a score <= 5
DELETE FROM second_table
WHERE score <= 5;
SELECT * FROM second_table
ORDER BY score DESC;
