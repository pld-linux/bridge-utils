Summary:	Utilities for configuring the linux ethernet bridge
Summary(pl):	U¿ytki przeznaczone do konfiguracji linux ethernet bridge
Name:		bridge-utils
Version:	0.9.1
Release:	2
License:	GPL
Group:		Networking/Admin
Group(de):	Netzwerkwesen/Administration
Group(pl):	Sieciowe/Administacyjne
Source0:	ftp://openrock.net/bridge/bridge-utils/%{name}-%{version}.tar.gz
Patch0:		%{name}-opt.patch
Patch1:		%{name}-rootonly.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	brcfg
BuildRequires:	kernel-headers(bridging)

%define		_sbindir	/sbin

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
Summary:	Libraries for the linux ethernet bridge programs.
Summary(pl):	Biblioteki u¿ywane do sterowania linuxowym bridge.
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki

%description devel
This package contains the header and object files necessary for
developing programs which use 'libbridge', the interface to the linux
kernel ethernet bridge.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe i bibliotekê konieczn± do rozwoju
programów u¿ywaj±cych 'libbridge' - interfejs do linuxowego ethernet
bridge.

%prep
%setup -q -n bridge
%patch0 -p1
%patch1 -p1

%build
%{__make} all OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir},%{_includedir}} \
	$RPM_BUILD_ROOT%{_mandir}/man8

install brctl/brctl		$RPM_BUILD_ROOT%{_sbindir}
#install brctl/brctld		$RPM_BUILD_ROOT%{_sbindir}
install doc/*.8			$RPM_BUILD_ROOT%{_mandir}/man8
install libbridge/libbridge.a	$RPM_BUILD_ROOT%{_libdir}
install libbridge/libbridge.h	$RPM_BUILD_ROOT%{_includedir}

gzip -9nf doc/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{FAQ,FIREWALL,HOWTO,TODO,WISHLIST}.gz
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_includedir}/*.h
