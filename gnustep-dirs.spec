Summary:	Common dirs for GNUstep enviroment
Summary(pl):	Katalogi wspólne dla ¶rodowiska GNUstep
Name:		gnustep-dirs
Version:	1.0
Release:	1
License:	free
Group:		Base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Common dirs for GNUstep enviroment.

%description -l pl
Katalogi wspólne dla ¶rodowiska GNUstep.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/GNUstep

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/GNUstep*
