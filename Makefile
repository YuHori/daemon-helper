setup:
	sudo yum install -y rpmdevtools yum-utils
	rpmdev-setuptree

install:
	install -m 755 bin/daelp.sh /usr/bin/daelp.sh

package:
	mv rpm/*.spec ~/rpmbuild/SPECS/
	sudo rpmbuild -bb ~/rpmbuild/SPECS/*.spec --define "dist .el7"
