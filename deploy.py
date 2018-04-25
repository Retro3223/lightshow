from robotpy_installer.installer import SshController

ssh = SshController('10.32.23.6', 'pi', 'pypi', allow_mitm=True)
ssh.ssh("mkdir -p /home/pi/squiggly")
ssh.ssh("rm -rf /home/pi/squiggly/*")
ssh.sftp('./src', '/home/pi/squiggly')
ssh.ssh("sudo /etc/init.d/lightshow restart")
