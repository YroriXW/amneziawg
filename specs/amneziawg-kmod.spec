%global debug_package %{nil}
%define buildforkernels akmod

Name:           amneziawg-kmod
Version: 1.0.20260210
Release: 17%{?dist}
URL:            https://github.com/amnezia-vpn/amneziawg-linux-kernel-module
Summary:        Fast, modern, secure VPN tunnel
License:        GPL-2.0-only

Source0:        https://github.com/YroriXW/amneziawg/releases/download/v%{version}-%{release}/amneziawg-kmod.tar.gz

Requires: patch
BuildRequires:  make
BuildRequires:  patch
BuildRequires:  kmodtool

# kmodtool does its magic here
%{expand:%(kmodtool --target %{_target_cpu} --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
AmneziaWG is an obfuscated fork of WireGuard — a high-performance VPN
that runs inside the Linux Kernel and uses state-of-the-art cryptography
(the "Noise" protocol). On top of WireGuard's design goals — fast, simple,
lean, and more practical than IPSec or OpenVPN — AmneziaWG adds
configurable traffic obfuscation via junk packet injection and header
randomization, making it resistant to DPI-based detection and blocking.
It is designed for censorship circumvention in restrictive network
environments while retaining full compatibility with standard WireGuard
peers. Runs over UDP.

%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}

# print kmodtool output for debugging purposes:
kmodtool --target %{_target_cpu} --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%autosetup -c -N

pushd %{name}
kver=%{?kernel_versions}
kbuilddir="${kver##*___}"
kver="${kver%%___*}"
# Patch needed only on 6.19+: that's when blake2s_ctx (new API) was introduced
kver_major=$(echo "$kver" | cut -d. -f1)
kver_minor=$(echo "$kver" | cut -d. -f2)
if [ "$kver_major" -gt 6 ] || { [ "$kver_major" -eq 6 ] && [ "$kver_minor" -ge 19 ]; }; then
    echo "Applying blake2s patch for kernel $kver (>= 6.19, new blake2s API)"
    patch -p1 < ./patches/blake2s.patch
else
    echo "Skipping blake2s patch for kernel $kver (< 6.19, old blake2s API)"
fi
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
* Wed Mar 18 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260210-17
- correct copyright

* Wed Mar 18 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260210-16
- migrated memory leak fix to Arsolitt's PR

* Sun Mar 15 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260210-15
- correct description and docs of systemd units

* Mon Mar 09 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260210-14
- add patch to the dependencies

* Sat Mar 07 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260210-13
- rewrite debseries script

* Sat Mar 07 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260210-12
- fixed changelog and debseries scripts

* Sat Mar 07 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260210-11
- fixed amneziawg-tools env

* Sat Mar 07 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260210-10
- fixed arm builds

* Sat Mar 07 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260210-9
- rename patch, release to 9 and some restructuring

* Sat Mar 07 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260210-8
- More automatizations!

* Sat Mar 07 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260210-7
- Automations

* Sat Mar 07 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260210-6
- Unified changelog for deb based distros

* Fri Mar 06 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260210-5
- Fix links, copyrights, typos
- Simplify logic of applying blake2s patch

* Thu Mar 05 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260210-4
- Introduced smart check for blake2s patching
- Properly building deb

* Wed Mar 04 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260210-3
- Added debian builds
- Patches applying in CI now

* Sun Mar 01 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260210-2
- Added patch for memory leak, blake2s, version string

* Sat Feb 28 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260210-1
- Initial build
