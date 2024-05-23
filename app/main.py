import sys
import os
import zlib

def main():

    args = sys.argv
    command = args[1]
    if command == "init":
        os.mkdir(".git")
        os.mkdir(".git/objects")
        os.mkdir(".git/refs")
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/main\n")
        print("Initialized git directory")
    elif command == "cat-file":
        with open(f".git/objects/{args[3][:2]}/{args[3][2:]}", "rb") as file:
            decoded = str(zlib.decompress(file.read()), "utf8")
            if args[2] == "-t":
                out = decoded.split(" ")[0]
            elif args[2] == "-s":
                out = decoded.split("\0")[0].split(" ")[1]
            elif args[2] == "-p":
                out = decoded.split("\0")[1]
            else:
                raise RuntimeError(f"Incorrect use of command #{command}")
            sys.stdout.write(out)
    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
