%global debug_package %{nil}

Name:           amneziawg
Version:        1.0.20260210
Release:        5%{?dist}
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
* Fri Mar 6 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260210-5
- Fix links, copyrights, typos and simplify logic of applying blake2s patch
* Thu Mar 5 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260210-4
- Introduced smart check for blake2s patching, properly building deb
* Wed Mar 4 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260210-3
- Added debian builds, patches applying in the CI now
* Sun Mar 1 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260210-2
- Added patch for memory leak, blake2s, version string
* Sat Feb 28 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260210-1
- Initial build
