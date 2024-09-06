import os
import subprocess
import sys


def command_exists(command):
    """Check if a command exists on the system."""
    return subprocess.call(f"type {command}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0


def run_command(command):
    """Run a system command and return the output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def dirsearch_cmd(path):
    if not command_exists("dirsearch"):
        exit(1)
    extensions = "php,asp,aspx,jsp,py,txt,conf,config,bak,backup,swp,old,db,sql,asp,aspx,py,rb,bak,bkp,cache,cgi,conf,csv,html,inc,jar,js,json,jsp,lock,log,rar,old,sql,sql.gz,tar,tar.gz,txt,wadl,zip"
   return command = f"python3 dirsearch.py -e {extensions} -l -o {path} -i 200 --full-url"

    print("[+] Running dirsearch...")
    dirsearch_output = run_command(f"python dirsearch.py -e php,asp,aspx,jsp,py,txt,conf,config,bak,backup,swp,old,db,sqlasp,aspx,aspx~,asp~,py,py~,rb,rb~,php,php~,bak,bkp,cache,cgi,conf,csv,html,inc,jar,js,json,jsp,jsp~,lock,log,rar,old,sql,sql.gz,sql.zip,sql.tar.gz,sql~,swp,swp~,tar,tar.bz2,tar.gz,txt,wadl,zip -l {domain}/403.txt -i 200 --full-url")
    print(f"[+] Dirsearch results saved to {domain}/dirsearch-403.txt")
    
    print("[+] Running dirsearch...")
    dirsearch_output = run_command(f"python dirsearch.py -e php,asp,aspx,jsp,py,txt,conf,config,bak,backup,swp,old,db,sqlasp,aspx,aspx~,asp~,py,py~,rb,rb~,php,php~,bak,bkp,cache,cgi,conf,csv,html,inc,jar,js,json,jsp,jsp~,lock,log,rar,old,sql,sql.gz,sql.zip,sql.tar.gz,sql~,swp,swp~,tar,tar.bz2,tar.gz,txt,wadl,zip -l {domain}/404.txt -i 200 --full-url")
    print(f"[+] Dirsearch results saved to {domain}/dirsearch-404.txt")

    

    
