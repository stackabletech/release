Name:           The Stackable Platform - Orchestrator Components
Version:        1.0.0
Release:        1%{?dist}
Summary:        A metapackage that installs all operators of the Stackable platform
BuildArch:      noarch

License:        OSL 3.0
Source0:        %{name}-%{version}.tar.gz

Requires:       bash
Requires:       stackable-kafka-operator=0.3.0
Requires:       stackable-spark-operator=0.2.0
Requires:       stackable-zookeeper-operator=0.2.0
Requires:       stackable-nifi-operator=0.2.0
Requires:       stackable-opa-operator=0.2.0
Requires:       stackable-regorule-operator=0.2.0
Requires:       stackable-monitoring-operator=0.2.0

%description
This package constitutes a platform release of the Stackable Platform.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp %{name}.sh $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/stackable.sh

%changelog
* Mon Sep 13 2021 Sönke Liebau <soenke.liebau@stackable.de> - 1.0.0
- First release of the Stackable Platform