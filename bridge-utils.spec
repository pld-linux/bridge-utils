Summary:	Utilities for configuring the Linux ethernet bridge
Summary(pl):	Narzêdzia przeznaczone do konfiguracji linuksowego ethernet bridge
Name:		bridge-utils
Version:	1.0.4
Release:	1
License:	GPL
Group:		Networking/Admin
Source0:	http://dl.sourceforge.net/bridge/%{name}-%{version}.tar.gz
# Source0-md5:	2cab42847c4654e58c4d0ba114bfe2c2
URL:		http://bridge.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	linux-libc-headers >= 7:2.6.7
BuildRequires:	sysfsutils-devel
BuildRequires:	sed >= 4.0
Obsoletes:	brcfg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
This package contains utilities for configuring the Linux ethernet
bridge. The Linux ethernet bridge can be used for connecting multiple
ethernet devices together. The connecting is fully transparent: hosts
connected to one ethernet device see hosts connected to the other
ethernet devices directly.

%description -l pl
Ten pakiet zawiera narzêdzia przeznaczone do konfigurowania
linuksowego ethernet bridge (inteligentnego switcha). Linux ethernet
bridge mo¿e byæ u¿yty do ³±czenia kilku ethernetowych interfejsów
sieciowych w jeden. Po³±czenie jest w pe³ni prze¼roczyste; hosty
przy³±czone po jednej stronie widz± hosty z drugiej strony
bezpo¶rednio.

%package devel
Summary:	Libraries for the linux ethernet bridge programs
Summary(pl):	Biblioteki u¿ywane do sterowania linuksowym bridge
Group:		Development/Libraries

%description devel
This package contains the header and object files necessary for
developing programs which use 'libbridge', the interface to the linux
kernel ethernet bridge.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe i bibliotekê konieczn± do rozwoju
programów u¿ywaj±cych libbridge - interfejsu do linuksowego ethernet
bridge.

%prep
%setup -q

rm -rf autom4te.cache

%build
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
%configure
chmod u+w libbridge/libbridge_private.h
sed -i -e 's#sysfs/libsysfs.h#libsysfs.h#g' libbridge/libbridge_private.h
sed -i -e 's#KERNEL_HEADERS=.*#KERNEL_HEADERS=#g' */Makefile*
%{__make} \
	KERNEL_HEADERS=""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir},%{_includedir}} \
	$RPM_BUILD_ROOT%{_mandir}/man8

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{FAQ,FIREWALL,HOWTO,SMPNOTES,WISHLIST}
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_includedir}/*.h
