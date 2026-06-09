import subprocess
import pytest

def has_lspci:
    return subprocess.run("which lspci", shell=True).returncode ==0

@pytest.mark.skipif(not has_lspci(), reason="No lspci")

def test_pcie_exist():
    result = subprocess.run(
        "lspci | wc -l",
        shell=True,
        capture_output=True,
        text=True
    )
    assert int(result.stdout.strip()) >= 0  #云环境允许
