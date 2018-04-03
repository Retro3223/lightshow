from robotpy_installer.installer import SshController

ssh = SshController('10.32.23.6', 'pi', 'raspberry', allow_mitm=True)
ssh.ssh("rm -rf /home/pi/squiggly/*")
ssh.sftp('./src', '/home/pi/squiggly')