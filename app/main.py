import os
import shutil
import subprocess
import sys
import ctypes

CHROOT_DIR = "/tmp/chroot"
CLONE_NEWPID = 0x20000000


def main():
    command = sys.argv[3]
    args = sys.argv[4:]

    source = command
    destination = CHROOT_DIR + command
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    shutil.copy(source, destination)
    os.chroot(CHROOT_DIR)

    libc = ctypes.CDLL("libc.so.6")
    libc.unshare(CLONE_NEWPID)

    completed_process = subprocess.run([command, *args], capture_output=True)
    print(completed_process.stdout.decode("utf-8"), end="")
    print(completed_process.stderr.decode("utf-8"), end="", file=sys.stderr)
    sys.exit(completed_process.returncode)


if __name__ == "__main__":
    main()
