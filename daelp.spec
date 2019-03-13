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
install -m 755 /usr/bin/daelp %{buildroot}/usr/bin/daelp
install -m 755 /etc/systemd/system/daemontools.service %{buildroot}/etc/systemd/system/daemontools.service

%files
/usr/bin/daelp
/etc/systemd/system/daemontools.service

%changelog
* Tue Feb 16 1999 Jun YuHori 1.0.0-1
- initial
