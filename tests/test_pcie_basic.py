import pytest
import subprocess

def test_pcie_tools():
    assert subprocess.run("which lspci", shell=True).returncode == 0

def test_environment():
    result = subprocess.run("lspci | wc -l", shell=True, capture_output=True, text=True)
    assert int(result.stdout.strip()) > 0
