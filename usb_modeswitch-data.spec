Name:		usb_modeswitch-data
Version:	20100826
Release:	%mkrel 1
Summary:	USB Modeswitch gets 4G cards in operational mode 
Group:		Applications/System
License:	GPLv2+
URL:		http://www.draisberghof.de/usb_modeswitch/
%define	fname	usb-modeswitch-data
Source0:	http://www.draisberghof.de/%{name}/%{fname}-%{version}.tar.bz2
Patch0:		usb-modeswitch-data-dlink-dwm156.patch
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
%patch0 -p1

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog README
/lib/udev/rules.d/40-usb_modeswitch.rules
%dir %{_sysconfdir}/usb_modeswitch.d/
%{_sysconfdir}/usb_modeswitch.d/*
