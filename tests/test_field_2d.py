import subprocess
import sys
from pathlib import Path


def test_field_2d_creates_png(tmp_path, capsys):
    repo_root = Path(__file__).resolve().parents[1]
    png_path = repo_root / "field_2d.png"

    # ensure no stale file
    if png_path.exists():
        png_path.unlink()

    # run the example using the same python interpreter
    cmd = [
        sys.executable,
        str(repo_root / "examples" / "field_2d.py"),
        "--no-show",
    ]

    completed = subprocess.run(
        cmd,
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )

    # print output to help debugging when test fails
    print(completed.stdout)
    print(completed.stderr)

    assert (
        completed.returncode == 0
    ), f"example exited with {completed.returncode}"
    assert png_path.exists(), "field_2d.png was not created"

    # cleanup
    try:
        png_path.unlink()
    except Exception:
        pass
