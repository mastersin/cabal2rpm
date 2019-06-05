%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name cabal2info
%define f_pkg_name cabal2info
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %f_pkg_name
Version: 0.1.0.0
Release: alt1
License: BSD-3-Clause
Packager: Evgeny Sinelnikov <sin@altlinux.org>
Group: Development/Haskell
Url: http://hackage.haskell.org/package/cabal2info
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: cabal2info

BuildPreReq: haskell(abi) = %ghc_version


%description
cabal2info

%prep
%setup
%patch -p1

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all

%changelog
* Wed Jun 05 2019 Evgeny Sinelnikov <sin@altlinux.org> 0.1.0.0-alt1
- Spec created by cabal2rpm 0.20_11
