Name:           amneziawg-tools
Version:        1.0.20260223
Release:        3%{?dist}
URL:            https://www.wireguard.com/
Summary:        Fast, modern, secure VPN tunnel
License:        GPL-2.0-only

Source0:        https://github.com/amnezia-vpn/amneziawg-tools/archive/refs/tags/v%{version}.tar.gz

Patch0:			https://github.com/YroriXW/amneziawg/raw/refs/heads/main/fixversiontools.patch

%{?systemd_requires}
BuildRequires: make
BuildRequires: systemd
BuildRequires: gcc

%description
WireGuard is a novel VPN that runs inside the Linux Kernel and uses
state-of-the-art cryptography (the "Noise" protocol). It aims to be
faster, simpler, leaner, and more useful than IPSec, while avoiding
the massive headache. It intends to be considerably more performant
than OpenVPN. WireGuard is designed as a general purpose VPN for
running on embedded interfaces and super computers alike, fit for
many different circumstances. It runs over UDP.

This package provides the wg binary for controlling WireGuard.

%prep
%autosetup -p1

%build
%set_build_flags
%make_build RUNSTATEDIR=%{_rundir} -C src

%install
%make_install BINDIR=%{_bindir} MANDIR=%{_mandir} RUNSTATEDIR=%{_rundir} \
WITH_BASHCOMPLETION=yes WITH_WGQUICK=yes WITH_SYSTEMDUNITS=yes -C src

%files
%doc README.md contrib
%license COPYING
%{_bindir}/awg
%{_bindir}/awg-quick
%{_sysconfdir}/amnezia/amneziawg/
%{_datadir}/bash-completion/completions/awg
%{_datadir}/bash-completion/completions/awg-quick
%{_unitdir}/awg-quick@.service
%{_unitdir}/awg-quick.target
%{_mandir}/man8/awg.8*
%{_mandir}/man8/awg-quick.8*

%changelog
* Wed Mar 4 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260210-3
- Added debian builds, patches applying in the CI now
* Sun Mar 1 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260210-2
- Added patch for memory leak, blake2s, version string
* Sat Feb 28 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260223-1
- Initial build
