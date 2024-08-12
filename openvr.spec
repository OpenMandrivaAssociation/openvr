%define so_ver 2_5_1
Name:           openvr
Version:        2.5.1
Release:        1
Summary:        Virtual reality SDK
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/ValveSoftware/openvr
Source:         https://github.com/ValveSoftware/openvr/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE install-library.patch -- Install library in suffixed directory
Patch0:         install-library.patch
BuildRequires:  cmake
BuildRequires:  pkgconfig

%package devel
Summary:        Development files for VR API
Group:          Development/Libraries/C and C++
Requires:       libopenvr_api%{so_ver}

%package -n libopenvr_api%{so_ver}
Summary:        SDK API library
Group:          System/Libraries

%description
OpenVR is an API and runtime that allows access to VR hardware from multiple vendors
without requiring that applications have specific knowledge of the hardware they are
targeting.

%description devel
OpenVR is an API and runtime that allows access to VR hardware from multiple vendors
without requiring that applications have specific knowledge of the hardware they are
targeting.

%description -n libopenvr_api%{so_ver}
OpenVR is an API and runtime that allows access to VR hardware from multiple vendors
without requiring that applications have specific knowledge of the hardware they are
targeting.

%prep
%autosetup -p1

rm -rfv ./lib ./bin

%build
%cmake -DBUILD_SHARED=ON -DBUILD_UNIVERSAL=OFF -DUSE_LIBCXX=OFF
%make_build

%install
%make_install -C build

%post -n libopenvr_api%{so_ver} -p /sbin/ldconfig
%postun -n libopenvr_api%{so_ver} -p /sbin/ldconfig

%files devel
%license LICENSE
%{_includedir}/openvr
%{_libdir}/libopenvr_api.so
%{_datadir}/pkgconfig/openvr.pc

%files -n libopenvr_api%{so_ver}
%{_libdir}/libopenvr_api.so.*
