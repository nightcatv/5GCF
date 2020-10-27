import os
import platform
import menu
import process

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

		process.load_route(path)
		input("")


if __name__ == "__main__":
	clean()
	menu.info()
	main()
