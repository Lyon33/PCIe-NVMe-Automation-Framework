#!/usr/bin/env python3
"""
基于 fio 的 NVMe 性能测试
"""
import subprocess
import yaml
import os

def run_fio(job):
    cmd = (
        f"fio --name={job['name']} "
        f"--filename={job['device']} "
        f"--rw={job['rw']} "
        f"--bs={job['bs']} "
        f"--size={job['size']} "
        f"--numjobs={job['numjobs']} "
        f"--runtime={job['runtime']} "
        "--group_reporting"
    )
    subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    config = {
        "name": "nvme_seq_read",
        "device": "/dev/nvme0n1",
        "rw": "read",
        "bs": "128k",
        "size": "1G",
        "numjobs": 1,
        "runtime": 30
    }
    run_fio(config)
