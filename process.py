import requests

def load_route(address, path):
	routes = []
	methods = []
	with open(path) as f:
		for data in f.readlines():
			tmp = data.split("|")
			routes.append("http://" + address + tmp[0])
			methods.append(tmp[1][:-1])
	return routes, methods

def connect(routes, methods):
	print("\nMETHOD" + " " * 2 + "URL" + " " * 147 + "RESPONSE" + "\n" + "-" * 166)
	for route, method in zip(routes, methods):
		result = method + " " * (8 - len(method)) + route + " " * (150 - len(route))
		try:
			if method == "GET":
				Print(result, requests.get(route, timeout = 5).status_code)
			elif method == "POST":
				Print(result, requests.post(route, timeout = 5).status_code)
			elif method == "PUT":
				Print(result, requests.put(route, timeout = 5).status_code)
			elif method == "DELETE":
				Print(result, requests.delete(route, timeout = 5).status_code)
			elif method == "PATCH":
				Print(result, requests.patch(route, timeout = 5).status_code)
		except requests.exceptions.Timeout:
			Print(result, 0)
			continue
		except requests.exceptions.ConnectionError:
			Print(result, -1)
			continue

def Print(result, status):
	print(result, end = "")

	div = status // 100
	mod = status % 100

	if div == 2:
		print("\033[1;42m %s \033[0m" % str(status))
	elif div == 4 and mod == 0:
		print("\033[1;45m %s \033[0m" % str(status))
	elif div == 4 and mod == 3:
		print("\033[1;43m %s \033[0m" % str(status))
	elif div == 5:
		print("\033[1;41m %s \033[0m" % str(status))
	elif status == 0:
		print("\033[1;46m %s \033[0m" % "TimeOut")
	elif status == -1:
		print("\033[1;46m %s \033[0m" % "Crash")
	else:
		print(" " + str(status))
