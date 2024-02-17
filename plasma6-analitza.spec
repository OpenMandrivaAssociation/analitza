%define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%ifarch %{arm}
%bcond_with opengl
%else
%bcond_without opengl
%endif

%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Library that will let you add mathematical features to your program
Name:		plasma6-analitza
Version:	24.01.96
Release:	%{?git:0.%{git}.}1
License:	LGPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/education/analitza/-/archive/%{gitbranch}/analitza-%{gitbranchd}.tar.bz2#/analitza-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/analitza-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6OpenGL)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6OpenGLWidgets)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(eigen3)

%description
The analitza library will let you add mathematical features to your program.

#---------------------------------------------

%package plots
Summary:	Plots used by the libanalitzaplot library
Group:		Graphical desktop/KDE
BuildArch:	noarch

%description plots
This package provides plots used by the libanalitzaplot library.

%files plots
%{_datadir}/libanalitza/plots

#---------------------------------------------

%define Analitza_major 8
%define libAnalitza %mklibname Analitza

%package -n %{libAnalitza}
Summary:	Runtime library for %{name}
Group:		System/Libraries

%description -n %{libAnalitza}
The analitza library will let you add mathematical features to your program.
This pakage provide the runtime library for %{name}.

%files -n %{libAnalitza} -f qm.lang
%{_libdir}/libAnalitza.so.%{Analitza_major}*

#---------------------------------------------

%define AnalitzaGui_major %{Analitza_major}
%define libAnalitzaGui %mklibname AnalitzaGui

%package -n %{libAnalitzaGui}
Summary:	Runtime library for %{name}
Group:		System/Libraries

%description -n %{libAnalitzaGui}
The analitza library will let you add mathematical features to your program.
This pakage provide the runtime library for %{name}.

%files -n %{libAnalitzaGui}
%{_libdir}/libAnalitzaGui.so.%{AnalitzaGui_major}*

#---------------------------------------------

%define AnalitzaPlot_major %{Analitza_major}
%define libAnalitzaPlot %mklibname AnalitzaPlot

%package -n %{libAnalitzaPlot}
Summary:	Runtime library for %{name}
Group:		System/Libraries
Requires:	analitza-plots

%description -n %{libAnalitzaPlot}
The analitza library will let you add mathematical features to your program.
This pakage provide the runtime library for %{name}.

%files -n %{libAnalitzaPlot}
%{_libdir}/libAnalitzaPlot.so.%{AnalitzaPlot_major}*

#---------------------------------------------

%define AnalitzaWidgets_major %{Analitza_major}
%define libAnalitzaWidgets %mklibname AnalitzaWidgets

%package -n %{libAnalitzaWidgets}
Summary:	Widget library for %{name}
Group:		System/Libraries

%description -n %{libAnalitzaWidgets}
The analitza library will let you add mathematical features to your program.
This pakage provide the Widgets library for %{name}.

%files -n %{libAnalitzaWidgets}
%{_libdir}/libAnalitzaWidgets.so.%{AnalitzaWidgets_major}*

#---------------------------------------------
%package -n %{_lib}analitza-qml6
Summary:	QML support for Analitza
Group:		System/Libraries

%description -n %{_lib}analitza-qml6
QML support for Analitza

%files -n %{_lib}analitza-qml6
%{_libdir}/qt6/qml/org/kde/analitza

#---------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libAnalitza} = %{EVRD}
Requires:	%{libAnalitzaGui} = %{EVRD}
Requires:	%{libAnalitzaPlot} = %{EVRD}
Requires:	%{libAnalitzaWidgets} = %{EVRD}

%description devel
Files needed to build applications based on %{name}.

%files devel
%{_includedir}/Analitza6
%{_libdir}/libAnalitza.so
%{_libdir}/libAnalitzaGui.so
%{_libdir}/libAnalitzaPlot.so
%{_libdir}/libAnalitzaWidgets.so
%{_libdir}/cmake/Analitza6

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n analitza-%{?git:%{gitbranchd}}%{!?git:%{version}}

%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja \
%if %{with opengl}
	-DSHOULD_BUILD_OPENGL:BOOL=ON
%else
	-DSHOULD_BUILD_OPENGL:BOOL=OFF
%endif

%build
%ninja -C build

%install
%ninja_install -C build
TOP=`pwd`
cd %{buildroot}
find .%{_datadir}/locale -name "*.qm" |while read r; do
	echo "%%lang($(echo $r|cut -d/ -f6)) $(echo $r |cut -b2-)" >>$TOP/qm.lang
done
