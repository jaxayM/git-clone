import sys
import os


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    # args: list[str] = sys.argv
    # if (args[1] == "init"):
    #     os.makedirs(".git/objects")
    #     os.makedirs(".git/refs")
    #     f = open(".git/HEAD", 'w')
    #     f.write("ref: refs/heads/main\n")
    #     f.close()
    
    command = sys.argv[1]
    if command == "init":
        os.mkdir(".git")
        os.mkdir(".git/objects")
        os.mkdir(".git/refs")
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/main\n")
        print("Initialized git directory")
    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
