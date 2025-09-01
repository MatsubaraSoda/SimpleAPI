# Anaconda 环境设置指南

## 创建 SimpleAPI 环境

### 方法1：使用 environment.yml 文件（推荐）

在 Anaconda Prompt 中执行：

```bash
# 进入项目目录
cd /d/WorkSpace/Blog/SimpleAPI

# 创建环境
conda env create -f environment.yml

# 激活环境
conda activate SimpleAPI
```

### 方法2：手动创建环境

```bash
# 创建新环境
conda create -n SimpleAPI python=3.11

# 激活环境
conda activate SimpleAPI

# 安装依赖
pip install -r requirements.txt
```

## 环境管理命令

```bash
# 查看所有环境
conda env list

# 激活环境
conda activate SimpleAPI

# 退出环境
conda deactivate

# 删除环境（如果需要重新创建）
conda env remove -n SimpleAPI

# 查看当前环境安装的包
conda list
```

## 运行项目

```bash
# 确保在 SimpleAPI 环境中
conda activate SimpleAPI

# 启动 Flask 应用
python app.py
```

## 环境导出

如果需要导出当前环境配置：

```bash
# 导出环境配置
conda env export > environment.yml

# 或者只导出 pip 包
pip freeze > requirements.txt
```

## 注意事项

- 每次开发前都要先激活环境：`conda activate SimpleAPI`
- 如果添加新的依赖包，记得更新 `environment.yml` 或 `requirements.txt`
- 建议在项目根目录下操作，这样相对路径更准确
