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
install -m 755 bin/daelp.sh %{buildroot}/usr/bin/daelp.sh

%files
/usr/bin/daelp.sh

%changelog
# let skip this for now
