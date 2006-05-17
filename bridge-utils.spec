Summary:	Utilities for configuring the Linux ethernet bridge
Summary(pl):	Narzêdzia przeznaczone do konfiguracji linuksowego ethernet bridge
Name:		bridge-utils
Version:	1.1
Release:	1
License:	GPL
Group:		Networking/Admin
Source0:	http://dl.sourceforge.net/bridge/%{name}-%{version}.tar.gz
# Source0-md5:	43bbd2a67b59cac3e15d545f8b51df68
URL:		http://linux-net.osdl.org/index.php/Bridge
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	linux-libc-headers >= 7:2.6.7
BuildRequires:	sysfsutils-devel >= 1.3.0-3
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
sieciowych w jeden. Po³±czenie jest w pe³ni przezroczyste; hosty
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
cp -f /usr/share/automake/{config.*,missing} .
%{__aclocal}
%{__autoconf}
%configure
sed -i -e 's#KERNEL_HEADERS=.*#KERNEL_HEADERS=#g' */Makefile*
%{__make} \
	CFLAGS="%{rpmcflags} -Wall" \
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
