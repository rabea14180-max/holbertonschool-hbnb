import os
import subprocess

def kill_server():
    print("Searching for process on port 5000...")
    try:
        # Use netstat to find LISTENING process on 5000
        output = subprocess.check_output('netstat -ano | findstr :5000', shell=True).decode()
        pids = set()
        for line in output.splitlines():
            if 'LISTENING' in line:
                parts = line.strip().split()
                pid = parts[-1]
                pids.add(pid)
        
        if not pids:
            print("No LISTENING process found on port 5000.")
        else:
            for pid in pids:
                print(f"Stopping PID {pid}...")
                os.system(f"taskkill /F /PID {pid}")
            print("✅ Server processes stopped.")
    except Exception as e:
        print(f"⚠️ Error or no process found: {e}")

if __name__ == "__main__":
    kill_server()
