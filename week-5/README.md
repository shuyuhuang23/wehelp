## 要求三：SQL CRUD
    INSERT INTO member (`name`, username, `password`)
    VALUES 
        ('test', 'test', 'test');
    --------------------------------------------------
    INSERT INTO member (`name`, username, `password`)
    VALUES 
        ('pengpeng', 'peng', 'secretkey'),
        ('custard', 'cake', 'cake123'),
        ('user3', 'shy', 'hsj'),
        ('user4', 'gfe', 'efg'),
        ('user5', 'abc', 'cba');
![Alt text](./img/3-1.png)

    SELECT * FROM member;
![Alt text](./img/3-2.png)

    SELECT * FROM member
    ORDER BY `time` DESC;
![Alt text](./img/3-3.png)

    SELECT id, `name`, username, `password`, follower_count, `time` FROM
    (
        SELECT 
            *, 
            ROW_NUMBER() OVER (
                ORDER BY `time` DESC
            ) row_num
        FROM 
            member
    ) tb
    WHERE row_num BETWEEN 2 AND 4
    ORDER BY `time` DESC;
![Alt text](./img/3-4.png)

    SELECT * FROM member
    WHERE username = 'test';
![Alt text](./img/3-5.png)

    SELECT * FROM member
    WHERE 
        username = 'test' AND
        `password` = 'test';
![Alt text](./img/3-6.png)

    UPDATE member 
    SET 
        `name` = 'test2'
    WHERE
        username = 'test'; 
![Alt text](./img/3-7.png)

## 要求四：SQL Aggregate Functions
    SELECT count(1) cnt FROM member;
![Alt text](./img/4-1.png)

    SELECT sum(follower_count) FROM member;
![Alt text](./img/4-2.png)

    SELECT avg(follower_count) FROM member;
![Alt text](./img/4-3.png)

## 要求五: SQL JOIN (Optional)
    SELECT 
        left_tb.*,
        right_tb.name
    FROM
        `message` left_tb
    JOIN 
        member right_tb
    ON left_tb.member_id = right_tb.id;
![Alt text](./img/5-1.png)

    SELECT 
        left_tb.*,
        right_tb.name
    FROM
        `message` left_tb
    JOIN 
        member right_tb
    ON left_tb.member_id = right_tb.id
    WHERE right_tb.name = 'test';
![Alt text](./img/5-2.png)

    SELECT 
        avg(left_tb.like_count)
    FROM
        `message` left_tb
    JOIN 
        member right_tb
    ON left_tb.member_id = right_tb.id
    WHERE right_tb.name = 'test';
![Alt text](./img/5-3.png)


