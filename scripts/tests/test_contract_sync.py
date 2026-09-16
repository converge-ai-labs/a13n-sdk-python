"""Offline integration of pinned input updates and reviewed-PR recovery."""

import subprocess
from pathlib import Path


def test_contract_sync_and_pr_recovery() -> None:
    subprocess.run(["bash", str(Path(__file__).with_name("contract-sync.sh"))], check=True)
