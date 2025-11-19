import argparse
import subprocess
import time

def resumable_command(cmd: str) -> None:
    """Run a command in a subprocess until it exits with code 0."""
    while True:
        print(f"Running: {cmd}")
        result = subprocess.run(cmd, shell=True)

        if result.returncode == 0:
            print("Command completed successfully.")
            break

        print(f"Command failed with exit code {result.returncode}. Retrying...")
        time.sleep(1)

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--resume",
        type=str,
        default=None,
        help="Path or identifier to resume from"
    )

    args = parser.parse_args()
    if args.resume:
        resumable_command(args.resume)
