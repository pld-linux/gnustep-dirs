Summary:	Common dirs for GNUstep environment
Summary(pl.UTF-8):	Katalogi wspólne dla środowiska GNUstep
Name:		gnustep-dirs
Version:	1.0
Release:	4
License:	free
Group:		Base
Requires:	FHS
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Common dirs for GNUstep environment.

%description -l pl.UTF-8
Katalogi wspólne dla środowiska GNUstep.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/GNUstep

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/GNUstep*
