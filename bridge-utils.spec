Summary:	Utilities for configuring the linux ethernet bridge
Summary(pl):	U¿ytki przeznaczone do konfiguracji linux ethernet bridge
Name:		bridge-utils
Version:	0.9.6
Release:	1
License:	GPL
Group:		Networking/Admin
Source0:	http://bridge.sourceforge.net/bridge-utils/%{name}-%{version}.tar.gz
# Source0-md5:	c45ede7ebd2fa762b4093f62ff582fd0
Patch0:		%{name}-rootonly.patch
URL:		http://bridge.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
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
Ten pakiet zawiera narzêdzia przeznaczone do konfigurowania
linuksowego ethernet bridge (inteligentny switch). Linux ethernet
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
programów u¿ywaj±cych 'libbridge' - interfejs do linuksowego ethernet
bridge.

%prep
%setup -q -n %{name}
#%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir},%{_includedir}} \
	$RPM_BUILD_ROOT%{_mandir}/man8

install brctl/brctl		$RPM_BUILD_ROOT%{_sbindir}
#install brctl/brctld		$RPM_BUILD_ROOT%{_sbindir}
install doc/*.8			$RPM_BUILD_ROOT%{_mandir}/man8
install libbridge/libbridge.a	$RPM_BUILD_ROOT%{_libdir}
install libbridge/libbridge.h	$RPM_BUILD_ROOT%{_includedir}

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
