#!/bin/bash

echo "=== PCIe/NVMe 测试环境部署 ==="

if [ "$(uname)" != "Linux"  ]; then
        echo "⚠️  当前非 Linux，跳过系统依赖安装"
            exit 0
fi

sudo apt update
sudo apt install -y pciutils nvme-cli fio python3-pip

pip3 install -r requirements.txt

echo "✅ 环境部署完成"
fi
