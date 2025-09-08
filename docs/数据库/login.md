## 创建 user 

```mysql
USE mydb;
```

```mysql
CREATE TABLE user (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    point BIGINT UNSIGNED DEFAULT 0
);
```

```mysql
CREATE TABLE user_auth (
    id BIGINT PRIMARY KEY,                 
    username VARCHAR(255) NOT NULL UNIQUE, 
    password_hash VARCHAR(255) NOT NULL,   
    FOREIGN KEY (id) REFERENCES user(id) ON DELETE CASCADE
);
```

```mysql
CREATE TABLE user_token (
    id BIGINT PRIMARY KEY,
    token VARCHAR(32) NOT NULL,
    FOREIGN KEY (id) REFERENCES user(id) ON DELETE CASCADE
);

```

