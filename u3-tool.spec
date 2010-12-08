%define name    u3-tool
%define version 0.3

Name:           %{name} 
Summary:        Tool for controlling the special features of a "U3 smart drive" USB Flash disk
Version:        %{version} 
Release:	%mkrel 3
Source0:        http://downloads.sourceforge.net/project/u3-tool/%{name}/%{version}/%{name}-%{version}.tar.gz
# gw fix for off-by-one crash
# https://sourceforge.net/tracker/?func=detail&aid=3010918&group_id=208198&atid=1004732
Patch: u3-print-size.patch
URL:            http://u3-tool.sourceforge.net/
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

