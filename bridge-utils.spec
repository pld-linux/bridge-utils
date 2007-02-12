Summary:	Utilities for configuring the Linux ethernet bridge
Summary(pl.UTF-8):   Narzędzia przeznaczone do konfiguracji linuksowego ethernet bridge
Name:		bridge-utils
Version:	1.2
Release:	1
License:	GPL
Group:		Networking/Admin
Source0:	http://dl.sourceforge.net/bridge/%{name}-%{version}.tar.gz
# Source0-md5:	1e6cff57ac90d7ab984d9512fdd9f2dd
URL:		http://linux-net.osdl.org/index.php/Bridge
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	linux-libc-headers >= 7:2.6.7
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

%description -l pl.UTF-8
Ten pakiet zawiera narzędzia przeznaczone do konfigurowania
linuksowego ethernet bridge (inteligentnego switcha). Linux ethernet
bridge może być użyty do łączenia kilku ethernetowych interfejsów
sieciowych w jeden. Połączenie jest w pełni przezroczyste; hosty
przyłączone po jednej stronie widzą hosty z drugiej strony
bezpośrednio.

%package devel
Summary:	Libraries for the linux ethernet bridge programs
Summary(pl.UTF-8):   Biblioteki używane do sterowania linuksowym bridge
Group:		Development/Libraries

%description devel
This package contains the header and object files necessary for
developing programs which use 'libbridge', the interface to the linux
kernel ethernet bridge.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe i bibliotekę konieczną do rozwoju
programów używających libbridge - interfejsu do linuksowego ethernet
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
%doc AUTHORS ChangeLog THANKS TODO doc/{FAQ,FIREWALL,HOWTO,SMPNOTES,WISHLIST}
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_includedir}/*.h
