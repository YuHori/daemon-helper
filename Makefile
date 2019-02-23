setup:
	sudo yum install -y rpmdevtools yum-utils
	rpmdev-setuptree

package:
	mv rpm/*.spec ~/rpmbuild/SPECS/
	sudo rpmbuild -bb ~/rpmbuild/SPECS/*.spec --define "dist .el7"
