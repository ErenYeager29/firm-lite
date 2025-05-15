import os

def scan_files(path):
    print(f"Scanning: {path}")
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith(('.conf', '.txt', '.sh', '.php', '.py')):
                print(f"[+] Found file: {os.path.join(root, f)}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Simple file scanner")
    parser.add_argument("path", help="Directory to scan")
    args = parser.parse_args()

    scan_files(args.path)
