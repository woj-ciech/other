# DanderSpritz script to retrieve last connected networks and presence of virtual machines

import dsz, dsz.path, dsz.ui, dsz.control, dsz.lp, dsz.cmd
from ops.parseargs import ArgumentParser
import optparse, os, shutil, sys
import os.path
import sys
import ops.files.dirs
import ops.system
import ops.system.environment, ops.system.systemversion
from ops.pprint import pprint


def virtual_machines():
	dsz.ui.Echo( '============================Virtual Machines====================================', dsz.GOOD)
	bad_list = ['.', '..', 'NetworkService', 'LocalService', 'Default', 'Public', 'All Users', 'Default User']
	user_path = "C:\Users"
	cmd = ('dir -dirsonly -path "%s"' % user_path)
	dircmd = ops.cmd.getDszCommand(cmd)
	dirobject = dircmd.execute()
	for user in dirobject.diritem[0].fileitem:
		if user.name not in bad_list:
			try:
				virtual_box_path = ("C:\Users\%s\Documents\Virtual Machines" % user.name)
				print virtual_box_path
				cmd = ('dir -path "%s"' % virtual_box_path)
				check_vdi = ops.cmd.getDszCommand(cmd)
				executed_check_vdi = check_vdi.execute()
				for directory in executed_check_vdi.diritem[0].fileitem:
					if ((directory.name is not None) and (directory.name.lower() not in ['.', '..'])):
						dsz.ui.Echo(directory.name, dsz.GOOD)
						output = dsz.ui.Prompt('Do you want to check that directory?', True)
						if output:
							inside = virtual_box_path + '\\' + directory.name
							cmd1 = ('dir -path "%s"' % inside)
							dsz_command = ops.cmd.getDszCommand(cmd1)
							executed_cmd = dsz_command.execute()
							for file in executed_cmd.diritem[0].fileitem:
								if ((file.name is not None) and (file.name.lower() not in ['.', '..'])):
									dsz.ui.Echo(file.name, dsz.GOOD)
						else:
							pas
			except Exception as e:
				#print e
				dsz.ui.Echo('Nothing found', dsz.ERROR)
				
	
				
	
def wifi_networks():
	dsz.ui.Echo( '============================WIFI Networks====================================', dsz.GOOD)
	home = list()
	home_network = ops.system.registry.get_registrykey('L', 'SOFTWARE\\Microsoft\\Windows\\currentversion\\HomeGroup\\NetworkLocations\Home')
	for key in home_network.key[0].value:
		profile = 'SOFTWARE\\Microsoft\\Windows NT\\currentversion\\NetworkList\\Profiles\\' + key.name
		details = ops.system.registry.get_registrykey('L', profile)
		for detail in details.key[0].value:		
			home.append({'name':detail.name,'value':detail.value})
	pprint(home,dictorder=['name','value'] )
		
	work_network = ops.system.registry.get_registrykey('L', 'SOFTWARE\\Microsoft\\Windows\\currentversion\\HomeGroup\\NetworkLocations\work')
	for key in work_network.key[0].value:
		profile = 'SOFTWARE\\Microsoft\\Windows NT\\currentversion\\NetworkList\\Profiles\\' + key.name
		details = ops.system.registry.get_registrykey('L', profile)
		for detail in details.key[0].value:
			work.append({'name':detail.name,'value':detail.value})
			

	pprint(work,dictorder=['name','value'] )

if (__name__ == '__main__'):
	wifi_networks()
	virtual_machines()
	
