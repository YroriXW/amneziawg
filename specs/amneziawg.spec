%global debug_package %{nil}

Name:           amneziawg
Version: 1.0.20260329
Release: 2%{?dist}
Summary:        Fast, modern, secure VPN tunnel
License:        GPL-2.0-only
URL:            https://github.com/YroriXW/amneziawg
Requires:       (akmod-amneziawg >= %{version} or kmod-amneziawg >= %{version})
Requires:       amneziawg-tools >= %{version}
Provides:       amneziawg-kmod-common = %{version}

BuildArch:      noarch

%description
Common package for AmneziaWG

%files

%changelog
* Mon Mar 30 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260329-2
- Some fixes

* Mon Mar 30 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260329-1
- All patches now in the upstream

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
