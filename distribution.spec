Name:           distribution
Version:        2.8.3
Release:        1%{?dist}
Summary:        oci container registry

License:        Apache 2.0
URL:            https://github.com/distribution/distribution.git
Source0:        %{name}-%{version}.tar.gz
Source1:        config.yaml
Source2:        registry.service

BuildRequires:  golang
BuildRequires:  systemd-rpm-macros
#Requires:       

%description
Open Source Registry implementation for storing and distributing container images and other content using the OCI Distribution Specification.

%global debug_package %{nil}

%prep
%autosetup


%build
make binaries

%install
mkdir -p -m 0755 %{buildroot}/%{_sharedstatedir}/registry
install -Dpm 0755 bin/registry %{buildroot}%{_bindir}/registry
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/registry/config.yaml
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_unitdir}/registry.service

%files
%{_bindir}/registry
%{_sysconfdir}/registry/config.yaml
%{_unitdir}/registry.service
%dir %{_sharedstatedir}/registry
%license LICENSE


%changelog
* Mon Oct 30 2023 papira
- 
