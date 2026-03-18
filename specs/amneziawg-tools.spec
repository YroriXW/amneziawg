Name:           amneziawg-tools
Version: 1.0.20260223
Release: 17%{?dist}
URL:            https://www.wireguard.com/
Summary:        Fast, modern, secure VPN tunnel
License:        GPL-2.0-only

Source0:        https://github.com/YroriXW/amneziawg/releases/download/v1.0.20260210-%{release}/amneziawg-tools.tar.gz

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
* Wed Mar 18 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260223-17
- correct copyright

* Wed Mar 18 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260223-16
- migrated memory leak fix to Arsolitt's PR

* Sun Mar 15 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260223-15
- correct description and docs of systemd units

* Mon Mar 09 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260223-14
- add patch to the dependencies

* Sat Mar 07 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260223-13
- rewrite debseries script

* Sat Mar 07 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260223-12
- fixed changelog and debseries scripts

* Sat Mar 07 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260223-11
- fixed amneziawg-tools env

* Sat Mar 07 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260223-10
- fixed arm builds

* Sat Mar 07 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260223-9
- rename patch, release to 9 and some restructuring

* Sat Mar 07 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260223-8
- More automatizations!

* Sat Mar 07 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260223-7
- Automations

* Sat Mar 07 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260223-6
- Unified changelog for deb based distros

* Fri Mar 06 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260223-5
- Fix links, copyrights, typos
- Simplify logic of applying blake2s patch

* Thu Mar 05 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260223-4
- Introduced smart check for blake2s patching
- Properly building deb

* Wed Mar 04 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260223-3
- Added debian builds
- Patches applying in CI now

* Sun Mar 01 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260223-2
- Added patch for memory leak, blake2s, version string

* Sat Feb 28 2026 Oleg YroriXW <olegyrori@gmail.com> - 1.0.20260223-1
- Initial build
