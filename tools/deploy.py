#/bin/python
#Author: Matias Menares @matiasmenares
import subprocess
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-i", help="Host IP SSH Raspberry pi")
parser.add_argument("-d", help="Destiny Path webserver Raspberry pi")
parser.add_argument("-u", help="User SSH Raspberry pi")

params = parser.parse_args()

def run(user, host, dir):
	hostname = user+"@"+host
	os.system("cd .. && npm run build")
	os.system("cd .. && zip -r dist.zip dist")
	os.system("cd .. && zip -r dashboard.zip dashboard")
	subprocess.run(["scp", "../dist.zip", hostname+":~/dist.zip"])
	subprocess.run(["scp", "../dashboard.zip", hostname+":~/dashboard.zip"])
	subprocess.run(["scp", "raspberry/kiosk.sh", hostname+":~/kiosk.sh"])
	#Frontend
	# subprocess.call(['ssh', hostname, "sudo rm -rf ~/dist"])
	# subprocess.call(['ssh', hostname, "sudo rm -rf /var/www/html"])
	# subprocess.call(['ssh', hostname, "sudo mkdir /var/www/html"])
	# subprocess.run(['ssh', hostname, "sudo unzip ~/dist.zip"])
	# subprocess.call(['ssh', '-t', hostname, "sudo rm ~/dist.zip"])
	# subprocess.call(['ssh', '-t', hostname, "sudo mv ~/dist/* /var/www/html"])

	subprocess.call(['ssh', hostname, "sudo rm -rf ~/dist"])
	subprocess.call(['ssh', hostname, "rm -rf /var/www/html/css"])
	subprocess.call(['ssh', hostname, "rm -rf /var/www/html/fonts"])
	subprocess.call(['ssh', hostname, "rm -rf /var/www/html/image"])
	subprocess.call(['ssh', hostname, "rm -rf /var/www/html/img"])
	subprocess.call(['ssh', hostname, "rm /var/www/html/index.html"])
	subprocess.call(['ssh', hostname, "rm -rf /var/www/html/js"])
	subprocess.run(['ssh', hostname, "unzip ~/dist.zip"])
	subprocess.call(['ssh', '-t', hostname, "rm ~/dist.zip"])
	subprocess.call(['ssh', '-t', hostname, "mv ~/dist/* /var/www/html"])
	#Backend
	subprocess.call(['ssh', hostname, "sudo rm -rf ~/nissboard-prod"])
	subprocess.call(['ssh', hostname, "sudo rm -rf ~/dashboard"])
	subprocess.call(['ssh', hostname, "mkdir  ~/nissboard-prod"])
	subprocess.run(['ssh', hostname, "unzip ~/dashboard.zip"])
	subprocess.run(['ssh', hostname, "mv ~/dashboard/* ~/nissboard-prod/"])
	subprocess.run(['ssh', hostname, "pip3 install -r ~/nissboard-prod/requirements.txt"])
	#Reboot
	subprocess.call(['ssh', '-t', hostname, "sudo reboot"])

if __name__ == '__main__':
	run(params.u, params.i, params.d)
