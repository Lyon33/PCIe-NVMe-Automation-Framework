import subprocess
import pytest

def test_fio_exists():
    assert subprocess.run("which fio", shell=True).returncode == 0
