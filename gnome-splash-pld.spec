Summary:	GNOME splash screen
Summary(pl.UTF-8):   Ekran startowy GNOME
Name:		gnome-splash-pld
Version:	1.99
Release:	2
License:	GPL
Group:		X11/Amusements
Source0:	http://krzak.linux.net.pl/gnome/pld-gnome-splash.png
# Source0-md5:	f1dbeb6a93c0ebf68239f495b23b22f0
URL:		http://www.pld-linux.org/
Requires:	gnome-session >= 2.4.1-6
Provides:	gnome-splash
Obsoletes:	gnome-splash
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Default GNOME splash screen for PLD.

%description -l pl.UTF-8
Standardowy ekran startowy GNOME dla PLD.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}/splash

install %{SOURCE0} $RPM_BUILD_ROOT%{_pixmapsdir}/splash/gnome-splash.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_pixmapsdir}/splash/gnome-splash.png
