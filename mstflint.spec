Name:		mstflint
Summary:	Mellanox firmware burning tool
Version:	1.4
Release:	3%{?dist}
License:	GPLv2+ or BSD
Group:		Applications/System
Source:		http://www.openfabrics.org/downloads/%{name}/%{name}-%{version}-0.1.g899ead3.tar.gz
Url:		http://www.openfabrics.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	libstdc++-devel, zlib-devel
Obsoletes:	openib-mstflint <= 1.4 openib-tvflash <= 0.9.2 tvflash <= 0.9.0
ExcludeArch:	s390 s390x

%description
This package contains a burning tool for Mellanox manufactured HCA cards.
It also provides access to the relevant source code.

%prep
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS"
%configure
make

%install
rm -rf ${RPM_BUILD_ROOT}
install -D -m 0755 mstmread $RPM_BUILD_ROOT%{_bindir}/mstmread
install -D -m 0755 mstmwrite $RPM_BUILD_ROOT%{_bindir}/mstmwrite
install -D -m 0755 mstflint $RPM_BUILD_ROOT%{_bindir}/mstflint
install -D -m 0755 mstregdump $RPM_BUILD_ROOT%{_bindir}/mstregdump
install -D -m 0755 mstvpd $RPM_BUILD_ROOT%{_bindir}/mstvpd
#install -D -m 0644 mtcr.h       $RPM_BUILD_ROOT%{_includedir}/mtcr.h

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-, root, root)
%doc README
%_bindir/*

%changelog
* Fri Feb 19 2010 Doug Ledford <dledford@redhat.com> - 1.4-3.el6
- Don't include mtcr.h as we don't really expect anything to need Mellanox
  card register definitions except this program, and we already have the
  file.
- Change to ExcludeArch instead of ExclusiveArch so we build in all the right
  places.
- Related: bz543948

* Mon Jan 25 2010 Doug Ledford <dledford@redhat.com> - 1.4-2.el6
- Update to tarball from URL instead of from OFED
- Minor tweaks for pkgwrangler import
- Related: bz543948

* Sat Apr 18 2009 Doug Ledford <dledford@redhat.com> - 1.4-1.el5
- Update to ofed 1.4.1-rc3 version
- Related: bz459652

* Tue Apr 01 2008 Doug Ledford <dledford@redhat.com> - 1.3-1
- Update to OFED 1.3 final bits
- Related: bz428197

* Sun Jan 27 2008 Doug Ledford <dledford@redhat.com> - 1.2-2
- Obsolete the old openib-mstflint package

* Fri Jan 25 2008 Doug Ledford <dledford@redhat.com> - 1.2-1
- Initial import into CVS
- Related: bz428197

* Thu Jul 19 2007 - Vladimir Sokolovsky vlad@mellanox.co.il
- Initial Package, Version 1.2
