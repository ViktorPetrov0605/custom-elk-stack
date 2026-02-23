import sys
import pexpect

HOST = "10.4.4.87"
USER = "telehouse"
PASS = "T3l3h0us#"

def run_test():
    child = pexpect.spawn(f"ssh -o StrictHostKeyChecking=no {USER}@{HOST}", encoding='utf-8', timeout=10)
    index = child.expect(['(?i)password:', pexpect.EOF, pexpect.TIMEOUT])
    if index == 0:
        child.sendline(PASS)
        child.expect([r'\$', r'#'])
    
    child.sendline("whoami")
    child.expect([r'\$', r'#'])
    print(f"WHOAMI: {child.before.strip().splitlines()[-1]}")

    child.sendline("su -")
    idx = child.expect([r'(?i)password:', pexpect.TIMEOUT], timeout=10)
    if idx == 0:
        child.sendline(PASS)
        child.expect(r'#')
        child.sendline("whoami")
        child.expect(r'#')
        print(f"WHOAMI AFTER ES: {child.before.strip().splitlines()[-1]}")

    child.terminate()

if __name__ == "__main__":
    run_test()
