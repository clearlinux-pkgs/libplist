#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v4
# autospec commit: 1ab68caa3dd3
#
Name     : libplist
Version  : 2.4.0
Release  : 1
URL      : https://github.com/libimobiledevice/libplist/releases/download/2.4.0/libplist-2.4.0.tar.bz2
Source0  : https://github.com/libimobiledevice/libplist/releases/download/2.4.0/libplist-2.4.0.tar.bz2
Summary  : C++ binding for @PACKAGE_NAME@
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: libplist-bin = %{version}-%{release}
Requires: libplist-lib = %{version}-%{release}
Requires: libplist-license = %{version}-%{release}
Requires: libplist-man = %{version}-%{release}
Requires: libplist-python = %{version}-%{release}
Requires: libplist-python3 = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : pypi-cython
BuildRequires : python3-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Project Name:
libcnary
Project Description:
A small N-ary (Tree) library written in C.

%package bin
Summary: bin components for the libplist package.
Group: Binaries
Requires: libplist-license = %{version}-%{release}

%description bin
bin components for the libplist package.


%package dev
Summary: dev components for the libplist package.
Group: Development
Requires: libplist-lib = %{version}-%{release}
Requires: libplist-bin = %{version}-%{release}
Provides: libplist-devel = %{version}-%{release}
Requires: libplist = %{version}-%{release}

%description dev
dev components for the libplist package.


%package lib
Summary: lib components for the libplist package.
Group: Libraries
Requires: libplist-license = %{version}-%{release}

%description lib
lib components for the libplist package.


%package license
Summary: license components for the libplist package.
Group: Default

%description license
license components for the libplist package.


%package man
Summary: man components for the libplist package.
Group: Default

%description man
man components for the libplist package.


%package python
Summary: python components for the libplist package.
Group: Default
Requires: libplist-python3 = %{version}-%{release}

%description python
python components for the libplist package.


%package python3
Summary: python3 components for the libplist package.
Group: Default
Requires: python3-core

%description python3
python3 components for the libplist package.


%prep
%setup -q -n libplist-2.4.0
cd %{_builddir}/libplist-2.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1709922603
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1709922603
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libplist
cp %{_builddir}/libplist-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libplist/881b050efe0ca3ad845b81debc6c1b4a1afa5a3e || :
cp %{_builddir}/libplist-%{version}/COPYING.LESSER %{buildroot}/usr/share/package-licenses/libplist/a64734e065eb3fcf8b3eea74e695bf274048be81 || :
cp %{_builddir}/libplist-%{version}/libcnary/COPYING %{buildroot}/usr/share/package-licenses/libplist/a64734e065eb3fcf8b3eea74e695bf274048be81 || :
export GOAMD64=v2
GOAMD64=v2
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/plistutil

%files dev
%defattr(-,root,root,-)
/usr/include/plist/Array.h
/usr/include/plist/Boolean.h
/usr/include/plist/Data.h
/usr/include/plist/Date.h
/usr/include/plist/Dictionary.h
/usr/include/plist/Integer.h
/usr/include/plist/Key.h
/usr/include/plist/Node.h
/usr/include/plist/Real.h
/usr/include/plist/String.h
/usr/include/plist/Structure.h
/usr/include/plist/Uid.h
/usr/include/plist/cython/plist.pxd
/usr/include/plist/plist++.h
/usr/include/plist/plist.h
/usr/lib64/libplist++-2.0.so
/usr/lib64/libplist-2.0.so
/usr/lib64/pkgconfig/libplist++-2.0.pc
/usr/lib64/pkgconfig/libplist-2.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libplist++-2.0.so.4
/usr/lib64/libplist++-2.0.so.4.4.0
/usr/lib64/libplist-2.0.so.4
/usr/lib64/libplist-2.0.so.4.4.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libplist/881b050efe0ca3ad845b81debc6c1b4a1afa5a3e
/usr/share/package-licenses/libplist/a64734e065eb3fcf8b3eea74e695bf274048be81

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/plistutil.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
