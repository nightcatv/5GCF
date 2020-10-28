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
		print("\nMETHOD" + " " * 2 + "URL" + " " * 147 + "RESPONSE" + "\n" + "-" * 166)
		for route, method in zip(routes, methods):
			# Change parameter here
			process.connect(route, method)
		input("")


if __name__ == "__main__":
	menu.info()
	main()
