import os

	#print('Only macOS is currently supported')


def createsymlink(path2original):
	print('Detected',os.name)
	if (os.name == 'mac') or (os.name == 'posix'):
		os.chmod(os.path.abspath(path2original),7550)
		os.symlink(os.path.abspath(path2original),'/usr/bin/'+path2original)
	else:
		print('Bad OS')

if __name__ == '__main__':
	
	createsymlink(input())