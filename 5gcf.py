import menu
import process

host = ""
port = ""

def main():
	host = input("Set host ip address: ")
	
	while True:
		menu.info()
		path, port = menu.menu()
		address = host + ":" + port

		routes, methods = process.load_route(address, path)

		menu.info()
		process.connect(routes, methods)
		input("")


if __name__ == "__main__":
	menu.info()
	main()
