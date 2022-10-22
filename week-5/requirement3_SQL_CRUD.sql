USE website;

INSERT INTO member (`name`, username, `password`)
VALUES 
    ('test', 'test', 'test');

INSERT INTO member (`name`, username, `password`)
VALUES 
    ('pengpeng', 'peng', 'secretkey'),
    ('custard', 'cake', 'cake123'),
    ('user3', 'shy', 'hsj'),
    ('user4', 'gfe', 'efg'),
    ('user5', 'abc', 'cba');

SELECT * FROM member;

SELECT * FROM member
ORDER BY `time` DESC;

SELECT id, `name`, username, `password`, follower_count, `time` FROM
(
    SELECT 
        *, 
        ROW_NUMBER() OVER (
            ORDER BY `time`
        ) row_num
    FROM 
        member
) tb
WHERE row_num BETWEEN 2 AND 4
ORDER BY `time` DESC;

SELECT * FROM member
WHERE username = 'test';

SELECT * FROM member
WHERE 
    username = 'test' AND
    `password` = 'test';

UPDATE member 
SET 
    `name` = 'test2'
WHERE
    username = 'test'; 