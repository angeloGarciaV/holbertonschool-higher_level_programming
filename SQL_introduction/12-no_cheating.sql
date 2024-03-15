-- updates the score of Bob to 10
UPDATE second_table
SET score = 10
WHERE `name` = "Bob";

SELECT * FROM second_table
ORDER BY score DESC;
