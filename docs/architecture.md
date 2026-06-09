# PCIe/NVMe 自动化测试架构

## 双轨测试模型

### 1️⃣ CI Runner（GitHub Cloud）
- 操作系统：Ubuntu
- 用途：
- Python 代码校验
- 依赖安装验证
- 系统工具链检测
- 无硬件测试执行
- 特点：
- 快速反馈
- 防止低级错误合入主干

### 2️⃣ Lab Runner（物理机 / 服务器）
- 操作系统：Linux
- 硬件：
- PCIe Gen4 / Gen5 插槽
- NVMe SSD / 待测芯片
- 用途：
- PCIe 枚举与链路验证
- NVMe Identify / 功能测试
- FIO 性能基准
- 长时间稳定性测试

## 测试策略

| 测试类型 | CI Runner | Lab Runner |
|--------|---------|-----------|
| 语法检查 | ✅ | ✅ |
| 工具链检查 | ✅ | ✅ |
| PCIe 枚举 | ⏭ | ✅ |
| NVMe 功能 | ⏭ | ✅ |
| 性能测试 | ⏭ | ✅ |

> ⏭：自动跳过（skipif）
