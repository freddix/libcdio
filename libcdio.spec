Summary:	GNU Compact Disc Input and Control Library
Name:		libcdio
Version:	0.83
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	ftp://ftp.gnu.org/gnu/libcdio/%{name}-%{version}.tar.gz
# Source0-md5:	b9e0f1bccb142e697cd834fe56b6e6fb
URL:		http://www.gnu.org/software/libcdio/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	help2man
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	sed
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library is to encapsulate CD-ROM reading and control.
Applications wishing to be oblivious of the OS- and device-dependent
properties of a CD-ROM can use this library.

%package devel
Summary:	Header files for libcdio libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libcdio libraries.

%package c++
Summary:	C++ libcdio libraries
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description c++
C++ libcdio libraries.

%package c++-devel
Summary:	Header files for C++ libcdio libraries
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description c++-devel
Header files for C++ libcdio libraries.

%package utils
Summary:	libcdio utilities: cd-info, cd-read
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description utils
libcdio utilities: cd-info, cd-read.

%prep
%setup -q

sed -i 's| example$||' Makefile.am
sed -i 's|libudf\.pc$|libudf.pc \\|' Makefile.am
sed -i 's|ENABLE_CPP|ENABLE_CXX_BINDINGS|' Makefile.am

%build
cp /usr/share/gettext/config.rpath .
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static	\
	--disable-vcd-info
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	mansubdir=/ja/man1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%post	devel -p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	c++ -p /usr/sbin/ldconfig
%postun	c++ -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %ghost %{_libdir}/libcdio.so.??
%attr(755,root,root) %ghost %{_libdir}/libcdio_cdda.so.?
%attr(755,root,root) %ghost %{_libdir}/libcdio_paranoia.so.?
%attr(755,root,root) %ghost %{_libdir}/libiso9660.so.?
%attr(755,root,root) %ghost %{_libdir}/libudf.so.?
%attr(755,root,root) %{_libdir}/libcdio.so.*.*.*
%attr(755,root,root) %{_libdir}/libcdio_cdda.so.*.*.*
%attr(755,root,root) %{_libdir}/libcdio_paranoia.so.*.*.*
%attr(755,root,root) %{_libdir}/libiso9660.so.*.*.*
%attr(755,root,root) %{_libdir}/libudf.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcdio.so
%attr(755,root,root) %{_libdir}/libcdio_cdda.so
%attr(755,root,root) %{_libdir}/libcdio_paranoia.so
%attr(755,root,root) %{_libdir}/libiso9660.so
%attr(755,root,root) %{_libdir}/libudf.so
%{_libdir}/libcdio.la
%{_libdir}/libcdio_cdda.la
%{_libdir}/libcdio_paranoia.la
%{_libdir}/libiso9660.la
%{_libdir}/libudf.la
%{_includedir}/cdio
%{_pkgconfigdir}/libcdio.pc
%{_pkgconfigdir}/libcdio_cdda.pc
%{_pkgconfigdir}/libcdio_paranoia.pc
%{_pkgconfigdir}/libiso9660.pc
%{_pkgconfigdir}/libudf.pc
%{_infodir}/libcdio.info*

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libcdio++.so.?
%attr(755,root,root) %ghost %{_libdir}/libiso9660++.so.?
%attr(755,root,root) %{_libdir}/libcdio++.so.*.*.*
%attr(755,root,root) %{_libdir}/libiso9660++.so.*.*.*

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcdio++.so
%attr(755,root,root) %{_libdir}/libiso9660++.so
%{_libdir}/libcdio++.la
%{_libdir}/libiso9660++.la
%{_includedir}/cdio++
%{_pkgconfigdir}/libcdio++.pc
%{_pkgconfigdir}/libiso9660++.pc

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
%lang(ja) %{_mandir}/ja/man1/*.1*
