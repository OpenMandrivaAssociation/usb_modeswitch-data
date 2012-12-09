Name:		usb_modeswitch-data
Version:	20120120
Release:	1
Summary:	Activating Switchable USB Devices on Linux
Group:		System/Configuration/Hardware
License:	GPLv2+
URL:		http://www.draisberghof.de/usb_modeswitch/
%define	fname	usb-modeswitch-data
Source0:	http://www.draisberghof.de/usb_modeswitch/%{fname}-%{version}.tar.bz2
BuildArch:	noarch
Requires:	usb_modeswitch

%description
USB Modeswitch brings up your datacard into operational mode. When plugged
in they identify themselves as cdrom and present some non-Linux compatible
installation files. This tool deactivates this cdrom-devices and enables
the real communication device. It supports most devices built and
sold by Huawei, T-Mobile, Vodafone, Option, ZTE, Novatel.

This package contains the data files needed for usb_modeswitch to function.

%prep
%setup -q -n %{fname}-%{version}

%install
%makeinstall_std

%files
%doc ChangeLog README
/lib/udev/rules.d/40-usb_modeswitch.rules
%dir %{_datadir}/usb_modeswitch
%{_datadir}/usb_modeswitch/*


%changelog
* Tue Aug 09 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 20110805-1
+ Revision: 693704
- update require version on new usb_modeswitch-data

* Fri Jul 15 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 20110714-1
+ Revision: 690080
- new version

* Tue Jul 05 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 20110619-1
+ Revision: 688825
- drop legacy rpm spec stuff
- new version

* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 20110227-2
+ Revision: 670752
- mass rebuild

* Wed Mar 30 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 20110227-1
+ Revision: 649289
- new version

* Fri Dec 03 2010 Eugeni Dodonov <eugeni@mandriva.com> 20101202-1mdv2011.0
+ Revision: 606878
- Updated to 20101202 snapshot.

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - add NeedResponse=1 to configuration for Samsung GT-B3730 (updates P1)

* Tue Sep 07 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 20100826-2mdv2011.0
+ Revision: 576542
- fix incomplete switching of GT-B3730 (P1)

* Thu Sep 02 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 20100826-1mdv2011.0
+ Revision: 575480
- fix summary
- fix group
- don't create backups when applying patches, otherwise they get installed..
- add support for D-Link DWM-156 (P0)
- import usb_modeswitch-data


