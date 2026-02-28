Name:           amneziawg
Version:        1.0.20260210
Release:        1%{?dist}
Epoch:			1
Summary:        Fast, modern, secure VPN tunnel
License:        GPL-2.0
URL:            https://github.com/YroriXW/amneziawg-linux-kernel-module
Requires:       (akmod-amneziawg >= %{epoch}:%{version} or kmod-amneziawg >= %{epoch}:%{version})
Requires:       amneziawg-tools >= %{epoch}:%{version}
Provides:       amneziawg-kmod-common = %{epoch}:%{version}

BuildArch:      noarch

%description
Common package for AmneziaWG

%files

%changelog
* Sat Feb 28 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260210-1
- Initial build
