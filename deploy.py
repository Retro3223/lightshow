from robotpy_installer.installer import SshController

ssh = SshController('10.32.23.6', 'pi', 'pypi', allow_mitm=True)
ssh.ssh("mkdir -p /home/pi/squiggly")
ssh.ssh("rm -rf /home/pi/squiggly/*")
ssh.sftp('./src', '/home/pi/squiggly')
ssh.sftp('./etc', '/home/pi/squiggly' )
ssh.ssh("sudo cp /home/pi/squiggly/etc/systemd/system/lightshow.service /etc/systemd/system/lightshow.service")
#ssh.ssh("sudo cp /home/pi/squiggly/etc/init.d/lightshow /etc/init.d/lightshow")
#ssh.ssh("sudo cp /home/pi/squiggly/etc/default/lightshow /etc/default/lightshow")
ssh.ssh("sudo systemctl restart lightshow.service")
