import subprocess
import pytest
import os

def has_nvme():
    return os.path.exists("/dev/nvme0")

@pytest.mark.skipif(not has_nvme(), reason="No NVMe device")

def test_nvme_identify():
    rc = subprocess.run(
        "nvme id-ctrl /dev/nvme0",
        shell=True
    ).returncode
    assert rc == 0
