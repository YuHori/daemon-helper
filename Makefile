setup:
	sudo yum install -y rpmdevtools yum-utils
	rpmdev-setuptree

install:
	install -m 755 bin/daelp /usr/bin/daelp
	install -m 755 conf/daemontools.service /etc/systemd/system/daemontools.service

package:
	mv rpm/*.spec ~/rpmbuild/SPECS/
	sudo rpmbuild -bb ~/rpmbuild/SPECS/*.spec --define "dist .el7"
