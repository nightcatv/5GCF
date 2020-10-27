from art import *
import os
import platform

def clean():
	if platform.system() == "Windows":
		os.system("cls")
	else:
		os.system("clear")

def info():
	clean()
	title = "5GCF"
	subtitle = "5G Core Fuzzer"
	author = "Иo1lz"
	
	tprint(title, font = "3d_diagonal")
	print("+--------------------------------+")
	print("| " + subtitle + " " * (31 - len(subtitle)) + "|")
	print("| by " + author + " " * (28 - len(author)) + "|")
	print("+--------------------------------+")
	print()

def menu():
	NF = ["AMF", "AUSF", "NRF", "NSSF", "NEF", "PCF", "SMF", "UDM", "UDR"]
	NetworkFunction = ["Access and Mobility Management Function", "Authentication Server Function", "Network Repository Function", "Network Slice Selection Function", "Network Exposure Function", "Policy Control Function", "Session Management Function", "Unified Data Management", "Unified Data Repository"]
	path = ""

	print("Please choose the NF you want to fuzz.")
	for i in range(1, len(NF) + 1):
		print("[" + str(i) + "] " + NF[i - 1] + " " * (5 - len(NF[i - 1])) + " - " + NetworkFunction[i - 1])
	print("[0] Quit")
	
	while True:
		choose = input(">> ")
		if choose == "0":
			exit()
		elif choose.isnumeric() and int(choose) <= len(NF):
			choose = int(choose)
			chosen_nf = api(NF[choose - 1])
			path += "/" + NF[choose - 1]
			break
		else:
			print("Wrong input, please choose again")
	
	print("\n" + "-" * 33)
	for i in range(1, len(chosen_nf)):
		print("[" + str(i) + "] " + chosen_nf[i])
	print("[0] Quit")
	
	while True:
		choose = input(">> ")
		if choose == "0":
			exit()
		elif choose.isnumeric() and  int(choose) <= len(chosen_nf):
			choose = int(choose)
			path += "/"
			for i in chosen_nf[choose].split(" "):
				path += i
			path = "src" + path + "/route"
			break
		else:
			print("Wrong input, please choose again")
	
	return path, chosen_nf[0]

def api(nf):
	API_AMF = ["29518", "Communication", "Event Exposure", "Location", "MT", "Else"]
	API_AUSF = ["29509", "SoR Protection", "UE Authentication", "UPU Protection"]
	API_NRF = ["29510", "Access Token", "NF Discovery", "NF Management"]
	API_NSSF = ["29531", "NSSAI Availability", "NS Selection"]
	API_NEF = ["0", "PFD Management"]
	API_PCF = ["29507", "AM Policy Control", "BDT Policy Control", "Policy Authorization", "SM Policy Control", "UE Policy Control", "Else"]
	API_SMF = ["29502", "PDU Session", "Else"]
	API_UDM = ["29503", "Event Exposure", "Parameter Provision", "Subscriber Data Management", "UE Authentication", "UE Context Management", "Else"]
	API_UDR = ["29504", "Data Repository"]
	
	if nf == "AMF":
		return API_AMF
	elif nf == "AUSF":
		return API_AUSF
	elif nf == "NRF":
		return API_NRF
	elif nf == "NSSF":
		return API_NSSF
	elif nf == "NEF":
		return API_NEF
	elif nf == "PCF":
		return API_PCF
	elif nf == "SMF":
		return API_SMF
	elif nf == "UDM":
		return API_UDM
	elif nf == "UDR":
		return API_UDR
