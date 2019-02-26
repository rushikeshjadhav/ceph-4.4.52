%define uname  %{kernel_version}
%define module_dir updates
%define release 176

Summary: Driver for CephFS
Name: ceph
Version: 4.4.52
Release: %{?release}%{!?release:1}
License: GPL
#Source taken from kernel.org
#wget "https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.4.52.tar.xz"
#tar xf linux-4.4.52.tar.xz
#mv linux-4.4.52 ceph-4.4.52
#tar czf ceph-4.4.52.tar.gz ceph-4.4.52/fs/ceph
Source: %{name}-%{version}.tar.gz

BuildRequires: kernel-devel
Provides: vendor-driver
Requires: kernel-uname-r = %{kernel_version}
Requires(post): /usr/sbin/depmod
Requires(postun): /usr/sbin/depmod

#** Upstream patches to XCP-NG **
Patch1000: Makefile.patch
Patch1001: 05a9143edb47e7799f191f1015f56eb2dacfee0d.patch
Patch1002: bb7031c7e50f1b6564bf529036d9089e3c10120f.patch
Patch1003: 04f522476a267e5d2d15d4b0c9e1500027e69879.patch
#Not yet applied
#Patch1004: 044470266a5040585093e863f163f49024c3e459.patch
Patch1005: ba790013b514da37e85e52b00cbc04ea2e1d2167.patch
Patch1006: 857d0b3dd7566ebb70686a009c7100322ddf3bbe.patch
Patch1007: c7a20ed2951f303aba4b697afb41a220f72a3f05.patch
Patch1008: da0345d723f00b0544fe2b7aff3a4858ef5c38fa.patch
Patch1009: 8c7c3d5b785f539da3f45920c7c1ab5de5727ba7.patch
Patch1010: 5f6ce5ea8393c0826c0c0b85278ff1d49b94da69.patch

%description
Ceph Linux Device Driver source.

%prep
#%setup -q -n %{name}-%{version}
%autosetup -p1


%build
%{__make} -C /lib/modules/%{uname}/build M=$(pwd)/fs/ceph modules 

%install
%{__make} -C /lib/modules/%{uname}/build M=$(pwd)/fs/ceph INSTALL_MOD_PATH=%{buildroot} INSTALL_MOD_DIR=%{module_dir} DEPMOD=/bin/true modules_install

# remove extra files modules_install copies in
rm -f %{buildroot}/lib/modules/%{uname}/modules.*

# mark modules executable so that strip-to-file can strip them
find %{buildroot}/lib/modules/%{uname} -name "*.ko" -type f | xargs chmod u+x

%post
/sbin/depmod %{kernel_version}
%{regenerate_initrd_post}

%postun
/sbin/depmod %{kernel_version}
%{regenerate_initrd_postun}

%posttrans
%{regenerate_initrd_posttrans}

%files
%defattr(-,root,root,-)
/lib/modules/%{uname}/*/*.ko
%doc

%changelog
* Wed Feb 27 2019 Rushikesh Jadhav <rushikesh7@gmail.com> - 4.4.176
- Added upstream url as Source
- Update Ceph code from upstream patches
- Corrected spec file for date and version

* Sun Feb 24 2019 Rushikesh Jadhav <rushikesh7@gmail.com> - 4.4.52
- Added driver for CephFS
