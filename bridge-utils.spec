Summary:	Utilities for configuring the linux ethernet bridge.
Summary(pl):	U¿ytki przeznaczone do konfiguracji linux ethernet bridge.
Name:		bridge-utils
Version:	0.9.0
Release:	1
Group:		Networking/Admin
Group(pl):	Sieciowe/Administracja
Copyright:	GPL
Source0:	ftp://openrock.net/bridge/%{name}-%{version}.tar.gz
Patch0:		bridge-utils-opt.patch
Patch1:		bridge-utils-rootonly.patch
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	brcfg

%description
This package contains utilities for configuring the linux ethernet
bridge. The linux ethernet bridge can be used for connecting multiple
ethernet devices together. The connecting is fully transparent: hosts
connected to one ethernet device see hosts connected to the other
ethernet devices directly.

%description -l pl
Ten pakiet zawiera narzêdzia przeznaczone do konfigurowania linuxowego
ethernet bridge (inteligentny switch). Linux ethernet bridge mo¿e byæ
u¿yty do ³±czenia kilku ethernetowych interfejsów sieciowych w jeden.
Po³±czenie jest w pe³ni prze¼roczyste; hosty przy³±czone po jednej
stronie widz± hosty z drugiej strony bezpo¶rednio.

%package devel
Summary:        Libraries for the linux ethernet bridge programs.
Summary(pl):    Biblioteki u¿ywane do sterowania linuxowym bridge.
Group:          Development/Libraries
Group(pl):      Programowanie/Biblioteki

%description devel
This package contains the header and object files necessary
for developing programs which use 'libbridge', the interface
to the linux kernel ethernet bridge.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe i bibliotekê konieczn±
do rozwoju programów u¿ywaj±cych 'libbridge' - interfejs
do linuxowego ethernet bridge.

%prep
%setup -q -n bridge
%patch0 -p1
%patch1 -p1

%build
make OPT="$RPM_OPT_FLAGS" all

%install
rm -rf $RPM_BUILD_ROOT
install -d	$RPM_BUILD_ROOT/sbin
install -d      $RPM_BUILD_ROOT%{_libdir}
install -d      $RPM_BUILD_ROOT%{_includedir}
install -d      $RPM_BUILD_ROOT%{_mandir}/man8

install -s brctl/brctl		$RPM_BUILD_ROOT/sbin/
#install -s brctl/brctld		$RPM_BUILD_ROOT/sbin/
install doc/*.8			$RPM_BUILD_ROOT%{_mandir}/man8
install libbridge/libbridge.a	$RPM_BUILD_ROOT%{_libdir}
install libbridge/libbridge.h	$RPM_BUILD_ROOT%{_includedir}
	
gzip -9nf doc/*	$RPM_BUILD_ROOT%{_mandir}/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{FAQ,FIREWALL,HOWTO,TODO,WISHLIST}.gz
%attr(0755,root,root) /sbin/*
%{_mandir}/man8/*

%files devel
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/*.a
%attr(644,root,root) %{_includedir}/*.h
