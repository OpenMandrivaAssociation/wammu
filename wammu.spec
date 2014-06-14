%define name wammu
%define version 0.36
%define release 1

%define python_gammu_req 0.24

Summary:        Mobile phone manager
Name:           %{name}
Version:        %{version}
Release:        %{release}
Source0:        http://dl.cihar.com/%{name}/latest/%{name}-%{version}.tar.bz2
License:        GPLv2+
Group:          Communications
Url:        	http://wammu.eu
BuildRequires:  wxPythonGTK >= 2.6.2
BuildRequires:  python-gammu >= %{python_gammu_req}
BuildRequires:  python-devel

Requires:       wxPythonGTK >= 2.6.2
Requires:       python-gammu >= %{python_gammu_req}
Requires:       gnome-bluetooth
Requires:	python-pybluez

BuildArch:	noarch

%description
Mobile phone manager using Gammu as it's backend. It works with any phone Gammu
supports - many Nokia, Siemens, Alcatel, ... Written using wxGTK.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" SKIPWXCHECK=yes python setup.py build

%install
SKIPWXCHECK=yes python setup.py install --root=$RPM_BUILD_ROOT

%find_lang %name

%files -f %name.lang
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
%lang(es) %{_mandir}/es/man?/*
%lang(fr) %{_mandir}/fr/man?/*
%lang(pt_BR) %{_mandir}/pt_BR/man?/*


