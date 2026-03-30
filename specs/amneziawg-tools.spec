Name:           amneziawg-tools
Version: 1.0.20260329
Release: 2%{?dist}
URL:            https://www.wireguard.com/
Summary:        Fast, modern, secure VPN tunnel
License:        GPL-2.0-only

Source0:        https://github.com/YroriXW/amneziawg/releases/download/v1.0.20260329-%{release}/amneziawg-tools.tar.gz

%{?systemd_requires}
BuildRequires: make
BuildRequires: systemd
BuildRequires: gcc

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

This package provides the awg binary and awg-quick script for managing
AmneziaWG interfaces and obfuscation parameters.

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
* Mon Mar 30 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260329-2
- Some fixes

* Mon Mar 30 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260329-1
- All patches now in the upstream

