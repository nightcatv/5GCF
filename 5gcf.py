import os
import platform
import menu

host = ""
port = ""

def clean():
	if platform.system() == "Windows":
		os.system("cls");
	else:
		os.system("clear");

def main():
	host = input("Set host ip address: ")
	
	while True:
		clean()
		menu.info()
		path, port = menu.menu()
		address = host + ":" + port
		print(path)
		print(address)
		input("")


if __name__ == "__main__":
	clean()
	menu.info()
	main()
