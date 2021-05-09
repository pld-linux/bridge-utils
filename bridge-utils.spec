Summary:	Utilities for configuring the Linux ethernet bridge
Summary(pl.UTF-8):	Narzędzia przeznaczone do konfiguracji linuksowego ethernet bridge
Name:		bridge-utils
Version:	1.7.1
Release:	1
License:	GPL v2+
Group:		Networking/Admin
Source0:	https://www.kernel.org/pub/linux/utils/net/bridge-utils/%{name}-%{version}.tar.xz
# Source0-md5:	3e1fee4dc22cac5457c2f6ffb990a518
Patch0:		debian.patch
Patch1:		man.patch
Patch2:		build_fix.patch
URL:		http://www.linuxfoundation.org/collaborate/workgroups/networking/bridge
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	linux-libc-headers >= 7:2.6.7
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
Summary(pl.UTF-8):	Biblioteki używane do sterowania linuksowym bridge
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
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cp -f /usr/share/automake/{config.*,missing} .
%{__aclocal}
%{__autoconf}
%configure \
	--with-linux-headers=%{_includedir}

%{__make} \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir},%{_includedir}} \
	$RPM_BUILD_ROOT%{_mandir}/man8

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install libbridge/libbridge.h $RPM_BUILD_ROOT%{_includedir}
install libbridge/libbridge.a $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog THANKS doc/{FAQ,FIREWALL,HOWTO,SMPNOTES,WISHLIST}
%attr(755,root,root) %{_sbindir}/brctl
%{_mandir}/man8/brctl.8*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libbridge.a
%{_includedir}/libbridge.h
