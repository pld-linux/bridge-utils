Summary:	Utilities for configuring the linux ethernet bridge
Summary(pl):	Uøytki przeznaczone do konfiguracji linux ethernet bridge
Name:		bridge-utils
Version:	0.9.5
Release:	1
License:	GPL
Group:		Networking/Admin
Group(de):	Netzwerkwesen/Administration
Group(pl):	Sieciowe/Administracyjne
Source0:	http://bridge.sourceforge.net/bridge-utils/%{name}-%{version}.tar.gz
Patch0:		%{name}-opt.patch
Patch1:		%{name}-rootonly.patch
URL:		http://bridge.sourceforge.net/
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
Ten pakiet zawiera narzÍdzia przeznaczone do konfigurowania
linuksowego ethernet bridge (inteligentny switch). Linux ethernet
bridge moøe byÊ uøyty do ≥±czenia kilku ethernetowych interfejsÛw
sieciowych w jeden. Po≥±czenie jest w pe≥ni przeºroczyste; hosty
przy≥±czone po jednej stronie widz± hosty z drugiej strony
bezpo∂rednio.

%package devel
Summary:	Libraries for the linux ethernet bridge programs.
Summary(pl):	Biblioteki uøywane do sterowania linuksowym bridge.
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…

%description devel
This package contains the header and object files necessary for
developing programs which use 'libbridge', the interface to the linux
kernel ethernet bridge.

%description devel -l pl
Ten pakiet zawiera pliki nag≥Ûwkowe i bibliotekÍ konieczn± do rozwoju
programÛw uøywaj±cych 'libbridge' - interfejs do linuksowego ethernet
bridge.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__make} all OPT="%{rpmcflags}" CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir},%{_includedir}} \
	$RPM_BUILD_ROOT%{_mandir}/man8

install brctl/brctl		$RPM_BUILD_ROOT%{_sbindir}
#install brctl/brctld		$RPM_BUILD_ROOT%{_sbindir}
install doc/*.8			$RPM_BUILD_ROOT%{_mandir}/man8
install libbridge/libbridge.a	$RPM_BUILD_ROOT%{_libdir}
install libbridge/libbridge.h	$RPM_BUILD_ROOT%{_includedir}

cd doc && gzip -9nf FAQ FIREWALL HOWTO SMPNOTES WISHLIST

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.gz
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_includedir}/*.h
