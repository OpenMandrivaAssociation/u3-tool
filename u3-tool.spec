%define name    u3-tool
%define version 0.3

Name:           %{name} 
Summary:        Tool for controlling the special features of a "U3 smart drive" USB Flash disk
Version:        %{version} 
Release:	5
Source0:        http://downloads.sourceforge.net/project/u3-tool/%{name}/%{version}/%{name}-%{version}.tar.gz
# gw fix for off-by-one crash
# https://sourceforge.net/tracker/?func=detail&aid=3010918&group_id=208198&atid=1004732
Patch: u3-print-size.patch
URL:            https://u3-tool.sourceforge.net/
Group:          System/Configuration/Hardware
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot 
License:        GPLv2+ 

%description
Tool for controlling USB flash devices that confirm to the U3
specifications. This program can control the following features:

* Replacing of CD image
* Changing of virtual CD allocated size and completely removing it
* Enabling and disabling Security
* Unlocking and changing password of secured U3 device
* Obtaining various device information

WARNING: This Software is still alpha. Since the commands for
controlling U3 devices aren't publicly available, we don't exactly
know what we are doing. Although the application has been tested on a
Sandisk Cruzer micro and a Verbatim Store 'N Go, it is not said that
it won't stop other devices from working. The author is not
responsible for any damage to your device.

%prep 
%setup -q -a 0 
%patch -p0

%build 
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root) 
%doc README NEWS AUTHORS 
%{_sbindir}/u3-tool
%{_mandir}/man1/u3-tool.1*



%changelog
* Fri Dec 09 2011 Götz Waschk <waschk@mandriva.org> 0.3-4mdv2012.0
+ Revision: 739298
- yearly rebuild

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3-3mdv2011.0
+ Revision: 615282
- the mass rebuild of 2010.1 packages

* Thu Jun 03 2010 Götz Waschk <waschk@mandriva.org> 0.3-2mdv2010.1
+ Revision: 547023
- fix crash in u3-tool -i

* Sun Jan 03 2010 Götz Waschk <waschk@mandriva.org> 0.3-1mdv2010.1
+ Revision: 485926
- import u3-tool


* Sun Jan  3 2010 Götz Waschk <waschk@mandriva.org> 0.3-1mdv2010.1
- fix URL and description
- use the right configure macro

* Fri Dec 25 2009 Marianne Lombard <marianne@tuxette.fr> 0.3-1mdv
- First mandriva package
