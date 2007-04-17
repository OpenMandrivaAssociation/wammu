%define name wammu
%define version 0.19
%define release %mkrel 1

%define python_gammu_req 0.19

Summary:        Mobile phone manager
Name:           %{name}
Version:        %{version}
Release:        %{release}
Source0:        %{name}-%{version}.tar.bz2
License:        GPL
Group:          Communications
Url:        	http://www.cihar.com/gammu/wammu
Buildroot:  	%{_tmppath}/%name-%version-root
Requires:       wxPythonGTK, python-gammu >= %{python_gammu_req}, gnome-bluetooth
BuildRequires:  wxPythonGTK, python-gammu >= %{python_gammu_req}, python-devel
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
%doc README AUTHORS FAQ COPYING NEWS
%doc %{_mandir}/man1/*
%dir %py_puresitedir/Wammu/

