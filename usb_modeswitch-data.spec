Name:		usb_modeswitch-data
Version:	20150627
Release:	2
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
