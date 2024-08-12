%define libname %mklibname openvr
%define devname %mklibname -d openvr

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

%description
OpenVR is an API and runtime that allows access to VR hardware from multiple vendors
without requiring that applications have specific knowledge of the hardware they are
targeting.

%package -n %{libname}
Summary:        SDK API library
Group:          System/Libraries

%description -n %{libname}
OpenVR is an API and runtime that allows access to VR hardware from multiple vendors
without requiring that applications have specific knowledge of the hardware they are
targeting.

%package -n %{devname}
Summary:        Development files for VR API
Group:          Development/Libraries/C and C++
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
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

%files -n %{devname}
%license LICENSE
%{_includedir}/openvr
%{_libdir}/libopenvr_api.so
%{_datadir}/pkgconfig/openvr.pc

%files -n %{libname}
%{_libdir}/libopenvr_api.so.*
