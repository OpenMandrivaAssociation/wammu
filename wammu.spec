%define name wammu
%define version 0.35
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


%changelog
* Thu Dec 02 2010 Funda Wang <fwang@mandriva.org> 0.35-1mdv2011.0
+ Revision: 604648
- update to new version 0.35

* Thu Nov 04 2010 Funda Wang <fwang@mandriva.org> 0.34-2mdv2011.0
+ Revision: 593072
- rebuild for py2.7

* Tue Sep 07 2010 Funda Wang <fwang@mandriva.org> 0.34-1mdv2011.0
+ Revision: 576555
- new version 0.34

* Sat Jul 17 2010 Funda Wang <fwang@mandriva.org> 0.33-1mdv2011.0
+ Revision: 554722
- update file list
- new version 0.33

* Thu Jan 21 2010 Frederik Himpe <fhimpe@mandriva.org> 0.32.1-1mdv2010.1
+ Revision: 494653
- Update to new version 0.32.1

* Wed Jan 13 2010 Frederik Himpe <fhimpe@mandriva.org> 0.32-1mdv2010.1
+ Revision: 491047
- Update to new version 0.32

* Wed Dec 16 2009 Frederik Himpe <fhimpe@mandriva.org> 0.31.1-1mdv2010.1
+ Revision: 479571
- Update to new version 0.31.1

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.30.1-2mdv2010.0
+ Revision: 445734
- rebuild

* Sat Mar 07 2009 Funda Wang <fwang@mandriva.org> 0.30.1-1mdv2009.1
+ Revision: 351730
- update to new version 0.30.1

* Sat Mar 07 2009 Funda Wang <fwang@mandriva.org> 0.30-1mdv2009.1
+ Revision: 350991
- New version 0.30

* Fri Jan 02 2009 Funda Wang <fwang@mandriva.org> 0.29-2mdv2009.1
+ Revision: 323361
- rebuild

* Sun Oct 12 2008 Funda Wang <fwang@mandriva.org> 0.29-1mdv2009.1
+ Revision: 292627
- New version 0.29

* Tue Jul 22 2008 Funda Wang <fwang@mandriva.org> 0.28-1mdv2009.0
+ Revision: 240395
- New version 0.28

* Tue May 13 2008 Funda Wang <fwang@mandriva.org> 0.27-1mdv2009.0
+ Revision: 206514
- update to new version 0.27

* Tue Mar 04 2008 Funda Wang <fwang@mandriva.org> 0.26-1mdv2008.1
+ Revision: 178469
- New version 0.26

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Dec 21 2007 Funda Wang <fwang@mandriva.org> 0.25-1mdv2008.1
+ Revision: 136366
- New version 0.25

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 13 2007 Funda Wang <fwang@mandriva.org> 0.24-1mdv2008.1
+ Revision: 108372
- New version 0.24

* Thu Nov 08 2007 Funda Wang <fwang@mandriva.org> 0.23-2mdv2008.1
+ Revision: 106937
- bump required python-gammu version
- rebuild for new gammu
- fix url

* Sat Oct 13 2007 Funda Wang <fwang@mandriva.org> 0.23-1mdv2008.1
+ Revision: 97826
- New version 0.23

* Tue Apr 17 2007 Erwan Velu <erwan@mandriva.org> 0.19-1mdv2008.0
+ Revision: 14125
- 0.19


* Fri Feb 09 2007 Erwan Velu <erwan@mandriva.org> 0.17-1mdv2007.0
+ Revision: 118472
- Missing buildrequires
- 0.17

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - import wammu-0.13-1mdk

* Thu Apr 27 2006 Erwan Velu <velu@seanodes.com> 0.13-1mdk
- 0.13

* Fri Mar 17 2006 Erwan Velu <velu@seanodes.com> 0.12-2mdk
- Adding buildrequires

* Wed Mar 15 2006 Guillaume Bedot <littletux@mandriva.org> 0.12-1mdk
- 0.12
- use new python macro
- fix redundant-prefix-tag

* Wed Dec 28 2005 Erwan Velu <velu@seanodes.com> 0.11-1mdk
- 0.11

* Tue Aug 23 2005 Erwan Velu <velu@seanodes.com> 0.10-1mdk
- 0.10

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.8-3mdk
- Rebuild for new python

* Mon Nov 01 2004 Michael Scherer <misc@mandrake.org> 0.8-2mdk
- [DIRM]

* Sat Sep 25 2004 Erwan Velu <erwan@mandrakesoft.com> 0.8-1mdk
- Initial mdk release

