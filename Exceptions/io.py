try:
    with open("/dev/full", "w") as f:
        f.write("test")
except OSError as e:
    print(f"IOException: {e}")
    