Summary:	Utilities for configuring the linux ethernet bridge
Summary(pl):	U�ytki przeznaczone do konfiguracji linux ethernet bridge
Name:		bridge-utils
Version:	1.0.2
Release:	0.1
License:	GPL
Group:		Networking/Admin
Source0:	http://dl.sourceforge.net/bridge/%{name}-%{version}.tar.gz
# Source0-md5:	cbff660d83d24815e9a5bcf890ce22f1
URL:		http://bridge.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	sysfsutils-devel
BuildRequires:	kernel-headers(bridging)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	brcfg

%define		_sbindir	/sbin

%description
This package contains utilities for configuring the linux ethernet
bridge. The linux ethernet bridge can be used for connecting multiple
ethernet devices together. The connecting is fully transparent: hosts
connected to one ethernet device see hosts connected to the other
ethernet devices directly.

%description -l pl
Ten pakiet zawiera narz�dzia przeznaczone do konfigurowania
linuksowego ethernet bridge (inteligentny switch). Linux ethernet
bridge mo�e by� u�yty do ��czenia kilku ethernetowych interfejs�w
sieciowych w jeden. Po��czenie jest w pe�ni prze�roczyste; hosty
przy��czone po jednej stronie widz� hosty z drugiej strony
bezpo�rednio.

%package devel
Summary:	Libraries for the linux ethernet bridge programs
Summary(pl):	Biblioteki u�ywane do sterowania linuksowym bridge
Group:		Development/Libraries

%description devel
This package contains the header and object files necessary for
developing programs which use 'libbridge', the interface to the linux
kernel ethernet bridge.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe i bibliotek� konieczn� do rozwoju
program�w u�ywaj�cych 'libbridge' - interfejs do linuksowego ethernet
bridge.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%configure
chmod u+w brctl/brctl.h libbridge/libbridge_private.h
echo "#include <linux/errno.h>" >> brctl/brctl.h
echo "#include <linux/errno.h>" >> libbridge/config.h
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
%{_mandir}/man?/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_includedir}/*.h
