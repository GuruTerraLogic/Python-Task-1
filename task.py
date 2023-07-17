import sys   #it provide the access of the system
import psutil  #it retrive the information abt running process

def check_process_running(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the process/program name as a command-line argument.")
        sys.exit(1)

    process_name = sys.argv[1]
    if check_process_running(process_name):
        print(f"The process '{process_name}' is running.")
    else:
        print(f"The process '{process_name}' is not running.")
