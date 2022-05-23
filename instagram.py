import os
os.system('git pull')
if __name__ == "__main__":
        try:
                __import__("igxrex1").checkin()
        except Exception as e:
                exit(str(e))
