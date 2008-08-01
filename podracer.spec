%define name	podracer
%define version	1.4
%define release %mkrel 4

Name: 	 	%{name}
Summary: 	A versatile podcast fetcher
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/podracer/%{name}-%{version}.tar.bz2
URL:		http://podracer.sourceforge.net/
License:	BSD
Group:		Networking/News
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	curl bittorrent screen

%description
Podracer is a podcast aggregator that gets the enclosures from your list of
podcast subscriptions and stores them in the location you specify. It
supports BitTorrent, HTTP, and FTP downloads, and runs best as a cron job to
automatically retrieve podcasts throughout the day.

%prep
%setup -q

%build
gcc $RPM_BUILD_OPTS timeout.c -o timeout
chmod 755 timeout
			
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%_bindir
cp timeout %buildroot/%_bindir
mkdir -p %buildroot/%_mandir/man1
cp timeout.1.gz %buildroot/%_mandir/man1
cp %name %buildroot/%_bindir
mkdir -p %buildroot/%_sysconfdir
cp %name.conf %buildroot/%_sysconfdir
cp podracer.1.gz %buildroot/%_mandir/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CREDITS LICENSE README ChangeLog sample.subscriptions
%{_bindir}/%name
%{_bindir}/timeout
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/%name.conf

