%global oname Wammu
%global name %(echo %oname | tr [:upper:] [:lower:])

# NOTE: wammu has not been ported to wxpython4 yet
#    https://github.com/gammu/wammu/issues/78

# NOTE: use commit if the last release is too old
%global	snapshot 20221007
%global	commit f0bbd43c25f26e93fd050934b0ffc477b9b5e9bc

Summary:	Mobile phone manager
Name:		%{name}
Version:	0.44
Release:	%{?snapshot:0.%{snapshot}.}2
#Source0:	http://dl.cihar.com/%{name}/releases/%{name}-%{version}.tar.xz
#Source0:	https://github.com/gammu/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source0:	https://github.com/gammu/%{name}/archive/%{?commit:master}%{!?commit:%{version}}/%{name}-%{?commit:master}%{!?commit:%{version}}.tar.gz

# (upstream)
#   https://github.com/gammu/wammu/commit/7a8e4414cd15b320adca6312a1febde9744b7df3.patch
Patch0:		wammu-0.44-fix_python.patch
License:	GPLv3+
Group:		Communications
Url:		http://wammu.eu

BuildRequires:	python-dbus
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(python-gammu)
BuildRequires:	python3dist(pybluez)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(six)
BuildRequires:	python3dist(wxpython)
# for patch0
#BuildRequires:	python3dist(python-gettext)

#Requires:	python-dbus
#Requires:	pythonegg(pybluez)
#Requires:	pythonegg(python-gammu)
#Requires:	pythonegg(wxpython)

BuildArch:	noarch

%description
Mobile phone manager using Gammu as it's backend. It works with any phone Gammu
supports - many Nokia, Siemens, Alcatel, ... Written using wxGTK.

%files -f %name.lang
%doc README.* COPYING ChangeLog
%{_bindir}/%{name}
%{_bindir}/%{name}-configure
%{_datadir}/%{oname}
%{_datadir}/pixmaps/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/*.1.*
%{py_puresitedir}/%{oname}
%{py_puresitedir}/%{name}-%{version}-*.egg-info
%lang(dk) %{_mandir}/da/man1/*.1.*
%lang(cz) %{_mandir}/cs/man1/*.1.*
%lang(de) %{_mandir}/de/man1/*.1.*
%lang(es) %{_mandir}/es/man1/*.1.*
%lang(et) %{_mandir}/et/man1/*.1.*
%lang(fr) %{_mandir}/fr/man1/*.1.*
%lang(gb) %{_mandir}/en_GB/man1/*.1.*
%lang(hu) %{_mandir}/hu/man1/*.1.*
%lang(id) %{_mandir}/id/man1/*.1.*
%lang(it) %{_mandir}/it/man1/*.1.*
%lang(nl) %{_mandir}/nl/man1/*.1.*
%lang(pt_br) %{_mandir}/pt_BR/man1/*.1.*
%lang(ru) %{_mandir}/ru/man1/*.1.*
%lang(uk) %{_mandir}/uk/man1/*.1.*
%lang(sk) %{_mandir}/sk/man1/*.1.*
%lang(sv) %{_mandir}/sv/man1/*.1.*
%lang(tr) %{_mandir}/tr/man1/*.1.*

#--------------------------------------------------------------

%prep
%autosetup -p1  -S gendiff  -n %{name}-%{?commit:master}%{!?commit:%{version}}

%build
%py_build

%install
%py_install

# locales
%find_lang %name

