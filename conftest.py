#!/usr/bin/env python
"""
conftest.py
Pytest global configuration and hardware detection
"""
import os
import subprocess
import pytest

# ---------- Hardware Detection ----------
def has_lspci():
    return subprocess.run(
        "which lspci",
        shell=True,
        stdout=subprocess.DEVNULL

    ).returncode == 0

def has_nvme():
    return os.path.exists("/dev/nvme0")

def pci_device_count():
    if not has_lspci():
        return 0
    result = subprocess.run(
        "lspci | wc -l",
        shell=True,
        capture_output=True,
        text=True
    )
    return int(result.stdout.strip())

# ---------- Pytest Hooks ----------
def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "hardware: mark test as requiring real PCIe/NVMe hardware"
    )

def pytest_collection_modifyitems(config, items):
    for item in items:
        if "nvme" in item.nodeid and not has_nvme():
            item.add_marker(
                pytest.mark.skip(reason="NVMe device not present")
            )
        if "pcie" in item.nodeid and not has_lspci():
            item.add_marker(
                pytest.mark.skip(reason="lspci not available")
            )

# ---------- Fixtures ----------
@pytest.fixture(scope="session")
def hardware_env():
    return {
        "lspci": has_lspci(),
        "nvme": has_nvme(),
        "pcie_devices": pci_device_count()
    }
