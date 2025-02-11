# PDF to Excel Converter

A Python script that converts PDF files containing tables to Excel format.

## Requirements

- Python 3.x
- Ghostscript
- Required Python packages:
  - camelot-py[cv]
  - opencv-python
  - pandas
  - openpyxl

## Installation

1. Install Ghostscript:
# 确保你在项目目录中
cd /Users/isy/Desktop/pdf2excel

# 连接到你的 GitHub 仓库
git remote add origin https://github.com/wzy1029/pdf2excel.git

# 推送代码到 GitHub
git push -u origin main
# 确保我们在项目根目录
cd /Users/isy/Desktop/pdf2excel

# 创建标准的项目结构
mkdir src
mkdir tests
mkdir docs

# 移动 Python 文件到 src 目录
mv /Users/isy/pdf_to_excel_converter.py src/

# 创建项目结构如下：
# 确保我们在项目根目录
cd /Users/isy/Desktop/pdf2excel

# 创建标准的项目结构
mkdir src
mkdir tests
mkdir docs

# 移动 Python 文件到 src 目录
mv /Users/isy/pdf_to_excel_converter.py src/

# 创建项目结构如下：
cat > requirements.txt << 'EOL'
camelot-py[cv]
opencv-python
pandas
openpyxl
