import subprocess


def test_make():
    subprocess.run(['make', '-C', '/var/yp'])


if __name__ == "__main__":
    test_make()