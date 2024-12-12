# 定义一些通用变量
PYTHON = python3
PIP = pip
VENV_DIR = .venv
VENV_ACTIVATE = $(VENV_DIR)/bin/activate
REQUIREMENTS = requirements.txt

# 环境重建
.PHONY: env
env:
	@echo "Creating a virtual environment..."
	@if [ ! -d $(VENV_DIR) ]; then \
		$(PYTHON) -m venv $(VENV_DIR); \
	fi
	@echo "Virtual environment created."

# 安装依赖
.PHONY: install
install:
	@echo "Installing dependencies..."
	@source $(VENV_ACTIVATE) && $(PIP) install --upgrade pip
	@source $(VENV_ACTIVATE) && $(PIP) install -r $(REQUIREMENTS)
	@echo "Dependencies installed."

# 数据库迁移
.PHONY: migrate
migrate:
	@echo "Running database migrations..."
	@source $(VENV_ACTIVATE) && alembic upgrade head
	@echo "Migrations completed."

# 启动项目
.PHONY: start
start:
	@echo "Starting the project..."
	@source $(VENV_ACTIVATE) && uvicorn app.main:app --reload
	@echo "Project started."

# 清理环境
.PHONY: clean
clean:
	@echo "Cleaning virtual environment and *.pyc files..."
	rm -rf $(VENV_DIR)
	find . -name "*.pyc" -exec rm -f {} +
	@echo "Cleaned."

# 重新安装依赖（包括清理环境）
.PHONY: reinstall
reinstall: clean install
	@echo "Reinstalling dependencies from scratch."

# 生成数据库迁移脚本
.PHONY: revision
revision:
	@echo "Generating migration script..."
	@source $(VENV_ACTIVATE) && alembic revision --autogenerate -m "$(message)"
	@echo "Migration script created."

# 运行测试
.PHONY: test
test: install
	@echo "Running tests..."
	@source $(VENV_ACTIVATE) && pytest
	@echo "Tests completed."

# 查看帮助信息
.PHONY: help
help:
	@echo "Makefile commands:"
	@echo "  env         - Create a virtual environment."
	@echo "  install     - Install dependencies."
	@echo "  migrate     - Run database migrations."
	@echo "  start       - Start the project."
	@echo "  clean       - Clean the virtual environment and *.pyc files."
	@echo "  reinstall   - Reinstall dependencies from scratch."
	@echo "  revision    - Generate a database migration script."
	@echo "  test        - Run tests."
	@echo "  help        - Show this help message."
