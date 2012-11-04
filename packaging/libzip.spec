Name:           libzip
Version:        0.10.1
Release:        0
License:        BSD-3-Clause
Summary:        C library for reading, creating, and modifying zip archives
Url:            http://www.nih.at/libzip
Group:          Development/Libraries/C and C++
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  zlib-devel

%description
libzip is a C library for reading, creating, and modifying zip
archives. Files can be added from data buffers, files, or compressed. This
package contains a set of small utilities built using libzip
 * zipmerge - merge source zip archives into the target one
 * zipcmp - compares the zip archives and check if they contains same files
 * ziptorrent - manipulate with a restricted file format used for using bittorrent on zip files.

%package util
Summary:        C library for reading, creating, and modifying zip archives
Group:          Development/Libraries/C and C++

%description util
This is libzip, a C library for reading, creating, and modifying zip
archives.  Files can be added from data buffers, files, or compressed
data copied directly from other zip archives.  Changes made without
closing the archive can be reverted.  The API is documented by man
pages.

%package devel
Summary:        C library for reading, creating, and modifying zip archives
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libzip = %{version}

%description devel
libzip is a C library for reading, creating, and modifying zip
archives. This package contains devel files.

%prep
%setup -q

%build
autoreconf -fiv
%configure --disable-static --with-pic
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check VERBOSE=1

%install
%make_install
cp lib/zipconf.h %{buildroot}/%{_includedir}/zipconf.h

%post  -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files util
%defattr(-,root,root)
%{_bindir}/ziptorrent
%{_bindir}/zipcmp
%{_bindir}/zipmerge
%{_mandir}/man1/*.1*

%files
%defattr(-,root,root)
%{_libdir}/libzip.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/%{name}.so
%{_includedir}/zip.h
%{_includedir}/zipconf.h
%{_libdir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*.3*

%changelog
