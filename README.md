# PCIeHighSpeedTester: 高速接口芯片自动化测试框架

## 项目简介
专门为高速接口芯片方向计的自动化测试平台，重点覆盖 **PCIe/CXL 协议、驱动/固件测试
、Linux环境、性能基准、自动化框架**。

## 快速开始
```bash
# 部署环境（需要sudo权限）
bash scripts/setup_env.sh

# 运行测试
python -m pytest tests/ -v --html=reports/report.html

# 设备枚举
python scripts/pcie_enum.py

# 性能测试
python scripts/performance_test.py
```
