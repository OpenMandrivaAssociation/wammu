%define name wammu
%define version 0.34
%define release %mkrel 2

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
rm -rf $RPM_BUILD_ROOT
SKIPWXCHECK=yes python setup.py install --root=$RPM_BUILD_ROOT

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc README AUTHORS FAQ COPYING
%{_bindir}/*
%{py_puresitedir}/*
%{_datadir}/Wammu
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
%{_mandir}/man1/*
%lang(cs) %{_mandir}/cs/man?/*
%lang(de) %{_mandir}/de/man?/*
%lang(it) %{_mandir}/it/man?/*
%lang(nl) %{_mandir}/nl/man?/*
%lang(ru) %{_mandir}/ru/man?/*
%lang(sk) %{_mandir}/sk/man?/*
