import subprocess
import pytest

@pytest.mark.skipif(
    subprocess.run("which nvme", shell=True).returncode != 0,
    reason="nvme-cli not available"
)

def test_nvme_identify():
    rc = subprocess.run(
        "nvme id-ctrl /dev/nvme0",
        shell=True
            
    ).returncode
    assert rc == 0
