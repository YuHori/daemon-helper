Name:       daelp
Version:    1%{?dist}
Release:    %{release}
Summary:    Daemon Helper RPM package
License:    FIXME

%description
daemon-helper

%prep
# nothing here

%build
# nothing here

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 hello-world.sh %{buildroot}/usr/bin/hello-world.sh

%files
/usr/bin/hello-world.sh

%changelog
# let skip this for now
