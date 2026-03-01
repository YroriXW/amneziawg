%global debug_package %{nil}
%define buildforkernels akmod

Name:           amneziawg-kmod
Version:        1.0.20260210
Release:        2%{?dist}
URL:            https://github.com/amnezia-vpn/amneziawg-linux-kernel-module
Summary:        Fast, modern, secure VPN tunnel
License:        GPL-2.0-only

Source0:        https://github.com/YroriXW/amneziawg/releases/download/v%{version}-%{release}/amneziawg-kmod.tar.gz

Patch0:			https://github.com/babiulep/my-kernel-patches/raw/refs/heads/main/AMNEZIAWG/blake2s.patch
Patch1:			https://github.com/YroriXW/amneziawg/raw/refs/heads/main/fixmemleakinjpspecsetup.patch

BuildRequires:  make
BuildRequires:  kmodtool

# kmodtool does its magic here
%{expand:%(kmodtool --target %{_target_cpu} --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
WireGuard is a novel VPN that runs inside the Linux Kernel and uses
state-of-the-art cryptography (the "Noise" protocol). It aims to be
faster, simpler, leaner, and more useful than IPSec, while avoiding
the massive headache. It intends to be considerably more performant
than OpenVPN. WireGuard is designed as a general purpose VPN for
running on embedded interfaces and super computers alike, fit for
many different circumstances. It runs over UDP.

%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}

# print kmodtool output for debugging purposes:
kmodtool --target %{_target_cpu} --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%autosetup -c -N

pushd %{name}

kver=%{?kernel_versions}
kver=${kver%%___*}
kmaj=$(echo $kver | cut -d. -f1)
kmin=$(echo $kver | cut -d. -f2)
if [ -n "$kver" ] && { [ "$kmaj" -gt 6 ] || { [ "$kmaj" -eq 6 ] && [ "$kmin" -ge 18 ]; }; }; then
    echo "Applying blake2s patch for kernel $kver"
    patch -p1 < %{PATCH0}
fi

echo "Applying memory leak fix for jp_spec_setup"
patch -p1 < %{PATCH1}

popd

for kernel_version in %{?kernel_versions} ; do
    cp -a %{name} _kmod_build_${kernel_version%%___*}
done

%build
for kernel_version in %{?kernel_versions}; do
    make %{?_smp_mflags} -C "${kernel_version##*___}" M=${PWD}/_kmod_build_${kernel_version%%___*} modules
done

%install
for kernel_version in %{?kernel_versions}; do
    mkdir -p %{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}
    install -D -m 755 _kmod_build_${kernel_version%%___*}/*.ko %{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
done

#fix for obs
if [ -e %{_sourcedir}/%{name}.spec ]
then
  cp %{_sourcedir}/%{name}.spec %{_specdir}
fi

%{?akmod_install}

%changelog
* Sun Mar 1 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260210-2
- Added patch for memory leak, blake2s
* Sat Feb 28 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260210-1
- Initial build
