# SimpleAPI

一个**无数据库依赖**的Python Flask API服务，提供实时计算和随机数据生成功能。

## 快速开始

### 本地运行

1. **克隆项目**
```bash
git clone <your-repo-url>
cd SimpleAPI
```

2. **安装依赖**
```bash
# 使用 Anaconda（推荐）
conda env create -f environment.yml
conda activate SimpleAPI

# 或使用 pip
pip install -r requirements.txt
```

3. **启动服务**
```bash
python app.py
```

4. **访问API**
- 首页: http://localhost:5000/
- 计算API: POST http://localhost:5000/calculate
- 数据生成API: POST http://localhost:5000/generate-table

## API 接口

### 1. 计算表达式 API

**接口**: `POST /calculate`

**请求示例**:
```bash
curl -X POST http://localhost:5000/calculate \
  -H "Content-Type: application/json" \
  -d '{"expression": "2+3*4"}'
```

**请求格式**:
```json
{
  "expression": "2+3*4"
}
```

**成功响应**:
```json
{
  "expression": "2+3*4",
  "value": 14
}
```

**错误响应**:
```json
{
  "expression": "2+3*4",
  "error": "计算错误: 语法错误"
}
```

### 2. 生成随机数据表格 API

**接口**: `POST /generate-table`

**请求示例**:
```bash
curl -X POST http://localhost:5000/generate-table \
  -H "Content-Type: application/json" \
  -d '{"rows": 5}'
```

**请求格式**:
```json
{
  "rows": 5
}
```

**成功响应**:
```json
[
  {
    "id": 1,
    "name": "张三",
    "phone": "13912345678"
  },
  {
    "id": 2,
    "name": "李四",
    "phone": "18888888888"
  },
  {
    "id": 3,
    "name": "王五",
    "phone": "17777777777"
  }
]
```

**错误响应**:
```json
{
  "error": {
    "code": 400,
    "message": "数据量错误，rows参数应在1-32之间",
    "details": "请检查请求参数格式和范围"
  }
}
```

## 参数说明

### 计算表达式 API
- **expression** (string, 必填): 算术表达式，支持 +、-、*、/、() 和数字

### 生成数据表格 API
- **rows** (integer, 必填): 生成的行数，范围 1-32
- **返回字段**: 固定返回 id、name、phone 三个字段

## 部署

### Railway 部署（推荐）

1. 将项目推送到 GitHub
2. 访问 [Railway.app](https://railway.app)
3. 连接 GitHub 仓库
4. 自动部署完成

**在线地址**: https://simple-api-exercises.up.railway.app

## 技术栈

- **后端**: Python Flask
- **数据生成**: Faker 库
- **部署**: Railway
- **环境**: Python 3.11

## 项目结构

```
SimpleAPI/
├── app.py                    # 主应用文件
├── requirements.txt          # Python依赖
├── environment.yml           # Anaconda环境配置
├── module/                   # 功能模块
│   ├── validator.py         # 参数验证
│   ├── calculator.py        # 计算逻辑
│   └── generate_table.py    # 数据生成
└── docs/                    # 文档目录
```

## 许可证

MIT License