%global debug_package %{nil}

Name:           amneziawg
Version: 1.0.20260210
Release: 8%{?dist}
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
