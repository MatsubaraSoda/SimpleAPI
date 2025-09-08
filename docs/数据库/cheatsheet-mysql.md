# MySQL Cheatsheet (Ubuntu)

## 更新系统与安装 MySQL

```bash
sudo apt update
sudo apt install mysql-server -y
sudo systemctl start mysql
sudo systemctl enable mysql
```

## 登录 MySQL

- 无密码（sudo）：

```bash
sudo mysql
```

- 有密码（root 或其他用户）：

```bash
mysql -u root -p
```

## 创建数据库

```sql
CREATE DATABASE mydb;
SHOW DATABASES;
```

## 创建用户与授权

### 本地用户

```sql
CREATE USER 'manager1'@'localhost' IDENTIFIED BY 'YourPasswordHere';
GRANT ALL PRIVILEGES ON mydb.* TO 'manager1'@'localhost';
FLUSH PRIVILEGES;
```

### 远程用户（任意 IP）

```sql
CREATE USER 'manager1'@'%' IDENTIFIED BY 'YourPasswordHere';
GRANT ALL PRIVILEGES ON mydb.* TO 'manager1'@'%';
FLUSH PRIVILEGES;
```

> 配置远程访问时，需要修改 MySQL 配置文件：

```bash
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
# bind-address = 0.0.0.0
sudo systemctl restart mysql
```

## MySQL 端口修改（如改为 1433）

1. 编辑配置文件：

```bash
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
# 在 [mysqld] 下添加或修改
port = 1433
bind-address = 0.0.0.0  # 允许远程访问
```

1. 重启 MySQL：

```bash
sudo systemctl restart mysql
```

## 防火墙（UFW）设置

- 开放端口（TCP）：

```bash
sudo ufw allow 3306/tcp   # MySQL 默认端口
sudo ufw allow 1433/tcp   # SQL Server/MySQL自定义端口
```

- 关闭端口：

```bash
sudo ufw delete allow 3306/tcp
sudo ufw deny 3306/tcp
```

- 查看状态：

```bash
sudo ufw status numbered
```

## 测试连接

```bash
mysql -u manager1 -p -h 127.0.0.1 -P 1433
```