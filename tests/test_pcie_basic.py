import pytest
import subprocess

def has_lspci():
    return subprocess.run("which lspci", shell=True).returncode == 0

def pci_device_count():
    result = subprocess.run(
        "lspci | wc -l",
        shell=True,
        capture_output=True,
        text=True
    )
    return int(result.stdout.strip())

@pytest.mark.skipif(not has_lspci(), reason="lspci not available")
def test_pcie_tools():
    assert has_lspci()

@pytest.mark.skipif(
    not has_lspci() or pci_device_count() == 0,
    reason="No PCIe devices found"
)

def test_environment():
    assert pci_device_count() > 0
