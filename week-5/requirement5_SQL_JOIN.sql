CREATE TABLE `message` (
    id         BIGINT AUTO_INCREMENT,
    member_id  BIGINT NOT NULL,
    content    VARCHAR(255) NOT NULL,
    like_count INT UNSIGNED NOT NULL DEFAULT 0,
    `time`     DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (member_id) REFERENCES member(id)
);

INSERT INTO `message` (member_id, content, like_count)
VALUES 
    (2, "Welcome to js world.", 10),
    (2, "I like python more than js.", 100),
    (3, "Cakes are best snack in the world.", 2022),
    (1, 'test', 30);

SELECT 
    left_tb.*,
    right_tb.name
FROM
    `message` left_tb
JOIN 
    member right_tb
ON left_tb.member_id = right_tb.id;

SELECT 
    left_tb.*,
    right_tb.name
FROM
    `message` left_tb
JOIN 
    member right_tb
ON left_tb.member_id = right_tb.id
WHERE right_tb.name = 'test';

SELECT 
    avg(left_tb.like_count)
FROM
    `message` left_tb
JOIN 
    member right_tb
ON left_tb.member_id = right_tb.id
WHERE right_tb.name = 'test';