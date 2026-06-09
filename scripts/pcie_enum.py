#!/usr/bin/env python3
"""
PCIe 设备枚举与链路信息提取
"""
import subprocess
import platform

def run_cmd(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True)
    except Exception as e:
        return str(e)

def pci_enumeration():
    if platform.system() == "Darwin":
        return run_cmd("system_profiler SPPCIDataType")

    output = []
    output.append("=== PCIe 设备 ===")
    output.append(run_cmd("lspci -nn"))

    output.append("\n=== NVMe 设备链路信息 ===")
    output.append(run_cmd("lspci -vv | grep -A5 NVMe"))
    return "\n".join(output)

if __name__ == "__main__":
    print(pci_enumeration())
