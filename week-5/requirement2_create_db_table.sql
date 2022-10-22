CREATE DATABASE website;

USE website;

CREATE TABLE member (
    id             BIGINT AUTO_INCREMENT,
    `name`         VARCHAR(255) NOT NULL,
    username       VARCHAR(255) NOT NULL,
    `password`     VARCHAR(255) NOT NULL,
    follower_count INT UNSIGNED NOT NULL DEFAULT 0,
    `time`         DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);