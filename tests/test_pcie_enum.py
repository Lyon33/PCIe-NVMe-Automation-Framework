import subprocess
import pytest

@pytest.mark.skipif(
    subprocess.run("which lspci", shell=True).returncode != 0,
    reason="lspci not available"
)

def test_pcie_exist():
    out = subprocess.getoutput("lspci | wc -l")
    assert int(out) > 0
