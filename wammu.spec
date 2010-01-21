%define name wammu
%define version 0.32.1
%define release %mkrel 1

%define python_gammu_req 0.24

Summary:        Mobile phone manager
Name:           %{name}
Version:        %{version}
Release:        %{release}
Source0:        http://dl.cihar.com/%{name}/latest/%{name}-%{version}.tar.bz2
License:        GPLv2+
Group:          Communications
Url:        	http://wammu.eu
Buildroot:  	%{_tmppath}/%name-%version-root
Requires:       wxPythonGTK >= 2.6.2, python-gammu >= %{python_gammu_req}, gnome-bluetooth
BuildRequires:  wxPythonGTK >= 2.6.2, python-gammu >= %{python_gammu_req}, python-devel
BuildArch:	noarch

%description
Mobile phone manager using Gammu as it's backend. It works with any phone Gammu
supports - many Nokia, Siemens, Alcatel, ... Written using wxGTK.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" SKIPWXCHECK=yes python setup.py build

%install
SKIPWXCHECK=yes python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
sed -i '/man1/ D' INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README AUTHORS FAQ COPYING
%doc %{_mandir}/man1/*
%dir %py_puresitedir/Wammu/
%lang(cs) /usr/share/man/cs/*/*
%lang(de) /usr/share/man/de/*/*
%lang(nl) /usr/share/man/nl/*/*
