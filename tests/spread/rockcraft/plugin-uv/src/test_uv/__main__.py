# Test the importing of a non-stdlib module
import black  # pyright: ignore[reportMissingImports]
import subprocess

# "Use" it without using it so linters don't complain
_ = black


def main():
    print("Hello from uv")
    subprocess.run(["apt", "update"])
    subprocess.run(["apt", "install", "-y", "gcc"])



if __name__ == "__main__":
    main()
