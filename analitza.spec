Name:		analitza
Summary:	Library that will let you add mathematical features to your program
Version: 4.9.2
Release: 1
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://edu.kde.org
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	readline-devel

%description
The analitza library will let you add mathematical features to your program.

#---------------------------------------------

%package -n calgebra
Summary:	Console mathematical calculator
Group:		Graphical desktop/KDE
Conflicts:	kalgebra < 4.7.90

%description -n calgebra
Console interface for a mathematical calculator based content markup MathML
language.

%files -n calgebra
%{_kde_bindir}/calgebra

#---------------------------------------------

%define analitza_major 4
%define libanalitza %mklibname analitza %{analitza_major}

%package -n %{libanalitza}
Summary:	Runtime library for marble
Group:		System/Libraries

%description -n %{libanalitza}
Runtime library for marble

%files -n %{libanalitza}
%{_kde_libdir}/libanalitza.so.%{analitzagui_major}*

#---------------------------------------------

%define analitzagui_major 4
%define libanalitzagui %mklibname analitzagui %{analitzagui_major}

%package -n %{libanalitzagui}
Summary:	Runtime library for marble
Group:		System/Libraries

%description -n %{libanalitzagui}
Runtime library for marble

%files -n %{libanalitzagui}
%{_kde_libdir}/libanalitzagui.so.%{analitzagui_major}*

#---------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	kdelibs4-devel
Requires:	%{libanalitza} = %{EVRD}
Requires:	%{libanalitzagui} = %{EVRD}

%description devel
Files needed to build applications based on %{name}.

%files devel
%{_kde_includedir}/analitza
%{_kde_includedir}/analitzagui
%{_kde_libdir}/libanalitza.so
%{_kde_libdir}/libanalitzagui.so
%{_kde_libdir}/cmake/analitza

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

