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

### Railway 部署（推荐）

1. **准备项目**
   - 确保项目在GitHub上
   - 项目包含 `railway.json` 配置文件

2. **部署步骤**
   - 访问 [Railway.app](https://railway.app)
   - 使用GitHub账号登录
   - 点击 "New Project" → "Deploy from GitHub repo"
   - 选择您的SimpleAPI仓库
   - Railway会自动检测Python项目并部署

3. **环境变量配置**
   - 在Railway项目设置中可以配置环境变量
   - 如需要，可以设置 `FLASK_ENV=production`

4. **自动部署**
   - 每次推送到GitHub主分支，Railway会自动重新部署
   - 可以在Railway仪表板查看部署状态和日志

### 部署优势

- 🚀 **免费额度**: $5/月免费额度，足够个人项目
- 🔄 **自动部署**: 连接GitHub，推送即部署
- 📊 **监控**: 内置性能监控和日志查看
- 🌐 **全球CDN**: 自动分配最佳服务器位置

## 安全特性

- 表达式字符白名单验证
- 仅支持数字、运算符、括号
- 防止任意代码执行

## 项目结构

```
SimpleAPI/
├── app.py              # 主应用文件
├── requirements.txt    # Python依赖
├── environment.yml     # Anaconda环境配置
├── railway.json        # Railway部署配置
├── README.md          # 项目说明
├── docs/              # 文档目录
│   ├── 需求文档.md    # 需求文档
│   └── 环境创建日志.md # 环境创建和测试日志
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
