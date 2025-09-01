# SimpleAPI

一个**无数据库依赖、实时计算**的后端 API 服务，基于 Python Flask 框架实现。

## 项目特点

- 🚀 **无数据库依赖**: 所有计算基于内存，无需持久化存储
- ⚡ **实时计算**: 根据用户请求即时计算并返回结果
- 🔒 **安全可靠**: 严格的输入校验，防止代码注入
- 🌐 **易于部署**: 支持多种 BaaS 平台自动部署

## 技术栈

- **后端框架**: Python Flask
- **部署平台**: Vercel、Railway、Render、Fly.io、Heroku 等
- **代码托管**: GitHub

## 快速开始

### 本地运行

#### 使用 Anaconda（推荐）

1. 克隆项目
```bash
git clone <your-repo-url>
cd SimpleAPI
```

2. 创建并激活 Anaconda 环境
```bash
# 使用环境配置文件创建
conda env create -f environment.yml

# 激活环境
conda activate SimpleAPI
```

3. 启动服务
```bash
python app.py
```

#### 使用标准 Python

1. 克隆项目
```bash
git clone <your-repo-url>
cd SimpleAPI
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 启动服务
```bash
python app.py
```

4. 访问 API
- 首页: http://localhost:5000/
- 计算API: http://localhost:5000/calculate?expression=2+3*4

### API 使用

#### 计算表达式

**GET 请求**
```
GET /calculate?expression=2+6*96-(3-6)
```

**POST 请求**
```json
POST /calculate
Content-Type: application/json

{
    "expression": "2+6*96-(3-6)"
}
```

**响应示例**
```json
{
    "expression": "2+6*96-(3-6)",
    "result": 581.0,
    "status": "success"
}
```

## 部署说明

### Vercel 部署

1. 创建 `vercel.json` 配置文件
2. 连接 GitHub 仓库
3. 自动部署

### Railway 部署

1. 连接 GitHub 仓库
2. 选择 Python 环境
3. 自动构建部署

## 安全特性

- 表达式字符白名单验证
- 仅支持数字、运算符、括号
- 防止任意代码执行

## 项目结构

```
SimpleAPI/
├── app.py              # 主应用文件
├── requirements.txt    # Python依赖
├── README.md          # 项目说明
├── docs/              # 文档目录
│   └── 需求文档.md    # 需求文档
└── .gitignore         # Git忽略文件
```

## 开发计划

- [x] 基础项目结构
- [x] 计算表达式API
- [x] 安全校验逻辑
- [ ] 更多数学函数支持
- [ ] 性能优化
- [ ] 单元测试

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License
