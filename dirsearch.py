import subprocess

def command_exists(command):
    """Check if a command exists on the system."""
    return subprocess.call(f"type {command}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0


def run_command(command):
    """Run a system command and return the output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()


def dirsearch_cmd(in_path, out_path):
    if not command_exists("dirsearch"):
        exit(1)
    extensions = "php,asp,aspx,jsp,py,txt,conf,config,bak,backup,swp,old,db,sql,asp,aspx,py,rb,bak,bkp,cache,cgi,conf,csv,html,inc,jar,js,json,jsp,lock,log,rar,old,sql,sql.gz,tar,tar.gz,txt,wadl,zip"
    return f"python3 dirsearch.py -e {extensions} -l {in_path} -o {out_path} -i 200 --full-url"



    

    
