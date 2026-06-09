#!/usr/bin/env python3
"""
NVMe 控制器信息读取
"""
import subprocess

def nvme_identify():
        try:
            return subprocess.check_output(
                "nvme id-ctrl /dev/nvme0",
                shell=True,
                text=True
            )
        except Exception as e:
            return f"NVMe 设备不可用: {e}"

if __name__ == "__main__":
    print(nvme_identify())
