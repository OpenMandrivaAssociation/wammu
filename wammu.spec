Summary:	Mobile phone manager
Name:		wammu
Version:	0.44
Release:	1
Source0:	http://dl.cihar.com/%{name}/releases/%{name}-%{version}.tar.xz
License:	GPLv2+
Group:		Communications
Url:		http://wammu.eu

BuildRequires:	python-dbus
BuildRequires:	pkgconfig(python2)
BuildRequires:	pythonegg(python-gammu)
BuildRequires:	pythonegg(setuptools)
BuildRequires:	pythonegg(wxpython)

Requires:	python-dbus
Requires:	pythonegg(pybluez)
Requires:	pythonegg(python-gammu)
Requires:	pythonegg(wxpython)

BuildArch:	noarch

%description
Mobile phone manager using Gammu as it's backend. It works with any phone Gammu
supports - many Nokia, Siemens, Alcatel, ... Written using wxGTK.

%files -f %name.lang
%doc README.* COPYING ChangeLog
%{_bindir}/%{name}
%{_bindir}/%{name}-configure
%{_datadir}/Wammu
%{_datadir}/pixmaps/*
%{_datadir}/appdata/wammu.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/*.1.xz
%{python2_sitelib}/Wammu
%{python2_sitelib}/%{name}-%{version}-*.egg-info
%lang(dk) %{_mandir}/da/man1/*.1.xz
%lang(cz) %{_mandir}/cs/man1/*.1.xz
%lang(de) %{_mandir}/de/man1/*.1.xz
%lang(es) %{_mandir}/es/man1/*.1.xz
%lang(et) %{_mandir}/et/man1/*.1.xz
%lang(fr) %{_mandir}/fr/man1/*.1.xz
%lang(gb) %{_mandir}/en_GB/man1/*.1.xz
%lang(hu) %{_mandir}/hu/man1/*.1.xz
%lang(id) %{_mandir}/id/man1/*.1.xz
%lang(it) %{_mandir}/it/man1/*.1.xz
%lang(nl) %{_mandir}/nl/man1/*.1.xz
%lang(pt_br) %{_mandir}/pt_BR/man1/*.1.xz
%lang(ru) %{_mandir}/ru/man1/*.1.xz
%lang(uk) %{_mandir}/uk/man1/*.1.xz
%lang(sk) %{_mandir}/sk/man1/*.1.xz
%lang(sv) %{_mandir}/sv/man1/*.1.xz
%lang(tr) %{_mandir}/tr/man1/*.1.xz

#--------------------------------------------------------------

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" SKIPWXCHECK=yes %{__python2} setup.py build

%install
SKIPWXCHECK=yes %{__python2} setup.py install --root=%{buildroot}

# locales
%find_lang %name

