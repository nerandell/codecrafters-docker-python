import subprocess
import sys


def main():
    command = sys.argv[3]
    args = sys.argv[4:]

    completed_process = subprocess.run([command, *args], capture_output=True)
    print(completed_process.stdout.decode("utf-8"), end="")
    print(completed_process.stderr.decode("utf-8"), end="", file=sys.stderr)
    sys.exit(completed_process.returncode)


if __name__ == "__main__":
    main()
