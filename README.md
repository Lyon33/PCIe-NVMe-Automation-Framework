# PCIe-NVMe Automation Framework

[![PCIe-NVMe Automation CI](https://github.com/Lyon33/PCIe-NVMe-Automation-Framework/actions/workflows/ci.yml/badge.svg)](https://github.com/Lyon33/PCIe-NVMe-Automation-Framework/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.10-blue)
![Platform](https://img.shields.io/badge/platform-Linux-orange)

> 面向高速存储芯片的系统级自动化测试框架  
> 用于 PCIe/NVMe 设备的枚举、功能验证与性能基准测试

---

## 📌 项目简介

本项目旨在解决高速存储芯片（PCIe/NVMe SSD）在系统层面的回归测试痛点。  
通过 Python + pytest 构建自动化测试体系，结合 **GitHub CI（云端）** 与 **Lab Runner（物理机）** 的双轨架构，实现代码质量保障与真实硬件验证的解耦。

---

## 🏗 架构设计

\`\`\`mermaid
graph TD
A[PCIe-NVMe 自动化测试框架] --> B[测试类型]
B --> B1[PCIe 枚举与链路信息]
B --> B2[NVMe 控制器识别]
B --> B3[FIO 性能基准测试]

A --> C[执行环境]
C --> C1[GitHub Runner<br/>无硬件自动跳过]
C --> C2[Lab Runner<br/>真实芯片测试]

A --> D[测试产出]
D --> D1[pytest 报告]
D --> D2[HTML 可视化]
D --> D3[CI 状态徽章]
\`\`\`

---

## 🚀 快速开始

### 1️⃣ 克隆仓库
\`\`\`bash
git clone https://github.com/Lyon33/PCIe-NVMe-Automation-Framework.git
cd PCIe-NVMe-Automation-Framework
\`\`\`

### 2️⃣ 安装依赖
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 3️⃣ 运行测试
\`\`\`bash
pytest tests/ -v
\`\`\`

---

## 🧠 设计亮点

- **双轨测试模型**：CI 环境无硬件优雅跳过，Lab 环境执行全量测试  
- **统一硬件抽象**：通过 `conftest.py` 集中管理 PCIe/NVMe 设备探测逻辑  
- **工程化规范**：语义化 Commit、自动化 CI、可视化 HTML 报告  

---

## 📂 目录结构

\`\`\`text
.
├── .github/workflows/ci.yml   # GitHub Actions CI
├── scripts/                   # PCIe/NVMe 测试脚本
├── tests/                     # Pytest 测试用例
├── docs/                      # 架构与文档
├── conftest.py                # 全局硬件检测
└── requirements.txt
\`\`\`

---

## 📈 适用场景

- 芯片回片系统级回归测试  
- 固件版本验证  
- 驱动兼容性测试  
- 自动化测试平台原型

---

## 📄 License

MIT License
