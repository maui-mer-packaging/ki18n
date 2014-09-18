# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       ki18n

# >> macros
# << macros

# >> bcond_with
# << bcond_with

# >> bcond_without
# << bcond_without

Summary:    KDE Frameworks 5 Tier 1 addon for localization
Version:    5.2.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  ki18n.yaml
Source101:  ki18n-rpmlintrc
Requires:   kf5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext-devel
BuildRequires:  python3-devel

%description
KDE Frameworks 5 Tier 1 addon for localization.


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   gettext
Requires:   python3

%description devel
The %{name}-devel package contains the files necessary to develop applications |
that use %{name}.


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%doc COPYING.LIB README.md
%{_kf5_libdir}/libKF5I18n.so.*
%{_kf5_plugindir}/*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kf5_includedir}/ki18n_version.h
%{_kf5_includedir}/KI18n
%{_kf5_libdir}/libKF5I18n.so
%{_kf5_cmakedir}/KF5I18n
%{_kf5_mkspecsdir}/qt_KI18n.pri
# >> files devel
# << files devel
