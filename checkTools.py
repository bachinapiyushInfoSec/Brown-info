import subprocess

# Define colors
GREEN = "\033[92m"   # Green for installed
RED = "\033[91m"     # Red for not installed
YELLOW = "\033[93m"  # Yellow for installation process
RESET = "\033[0m"    # Reset color

def run_command(command):
    """Run a shell command silently (no output)."""
    subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def command_exists(command):
    """Check if a command exists on the system."""
    return subprocess.call(f"command -v {command}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

def install_tool(tool):
    """Check and install a required tool with color-coded output."""
    ins_cmds = {
        "subfinder": "go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest",
        "assetfinder": "go install github.com/tomnomnom/assetfinder@latest",
        "sublist3r": "pip install git+https://github.com/aboul3la/Sublist3r.git",
        "curl": "sudo apt install curl -y",
        "amass": "go install -v github.com/owasp-amass/amass/v4/...@latest",
        "httpx": "go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest",
        "tee": "sudo apt install coreutils -y",
        "waybackurls": "go install github.com/tomnomnom/waybackurls@latest",
        "gau": "go install github.com/lc/gau/v2/cmd/gau@latest",
        "katana": "go install github.com/projectdiscovery/katana/cmd/katana@latest",
        "nuclei": "go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest"
    }

    if command_exists(tool):
        print(f"{GREEN}[+] {tool} is already installed.{RESET}")
    else:
        print(f"{RED}[!] {tool} is not installed. {YELLOW}Installing now...{RESET}")
        run_command(ins_cmds[tool])
        if command_exists(tool):
            print(f"{GREEN}[+] {tool} installed successfully!{RESET}")
        else:
            print(f"{RED}[X] Failed to install {tool}!{RESET}")

print("[+] Checking if the Required Tools are installed...")

tools = ['subfinder', 'assetfinder', 'sublist3r', 'curl', 'amass', 'httpx', 'tee', 'waybackurls', 'gau', 'katana', 'nuclei']

for tool in tools:
    install_tool(tool)
