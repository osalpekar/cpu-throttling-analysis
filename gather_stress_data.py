import paramiko
import argparse
from remote_execution import *




"""
	system prep:
	install stress-ng
	install htop
	set container to one core
	make python file using code in sqrt.py and put it in the container at /var/www/
"""


def gather_data(ssh_client, ip):
	#CPU

	#change the container name in update and test commands before starting
	update_command = 'docker update --cpu-period 1000000 --cpu-quota {} upbeat_heyrovsky'
	stress_command = 'stress-ng -c 0 -l {}'
	test_command = 'docker exec upbeat_heyrovsky python /var/www/test.py'
	kill_command = 'killall stress-ng'

	for capacity in range(10,110,10):
		ssh_exec(ssh_client, update_command.format(capacity*10000))
		for stress_percent in range(10, 110, 10):
			print(capacity, stress_percent)
			ssh_client.exec_command(stress_command.format(stress_percent))
			for _ in range(5):
				x, stdout, y = ssh_client.exec_command(test_command)
				print(stdout.read())
			ssh_client.exec_command(kill_command)
	
	ssh_client.close()
	exit()





if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("machine_ip", help="IP to test")
    args = parser.parse_args()

    ssh_client = quilt_ssh(args.machine_ip)
    gather_data(ssh_client, args.machine_ip)

