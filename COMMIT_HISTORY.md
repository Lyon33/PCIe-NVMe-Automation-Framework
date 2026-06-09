# Commit History（专业工程师风格）

## v1.0.0 — 初始框架
- feat: 初始化 PCIe/NVMe 自动化测试框架
- feat: 新增 PCIe 设备枚举脚本
- feat: 新增 NVMe 控制器识别
- feat: 新增 FIO 性能测试

## v1.1.0 — CI 与稳定性
- ci: 新增 GitHub Actions 流水线
- fix: 升级 upload-artifact 至 v4
- test: 增加 pytest 单元测试
- test: 无硬件环境优雅跳过测试

## v1.2.0 — 工程化增强
- refactor: 统一硬件检测至 conftest.py
- docs: 新增 CI / Lab 双轨架构说明
- feat: 自动生成 HTML 测试报告
- chore: 完善 .gitignore 与项目结构
