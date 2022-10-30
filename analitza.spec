%ifarch %{arm}
%bcond_with opengl
%else
%bcond_without opengl
%endif

%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Library that will let you add mathematical features to your program
Name:		analitza
Version:	22.08.2
Release:	2
License:	LGPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(eigen3)
BuildRequires:	cmake(Qt5PrintSupport)

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
%define libAnalitza %mklibname Analitza %{Analitza_major}

%package -n %{libAnalitza}
Summary:	Runtime library for %{name}
Group:		System/Libraries
# calgebra used to be part of KDE4 analitza, but is gone now
Obsoletes:	calgebra < %{EVRD}
Obsoletes:	%{mklibname analitza 6} < 15012.0

%description -n %{libAnalitza}
The analitza library will let you add mathematical features to your program.
This pakage provide the runtime library for %{name}.

%files -n %{libAnalitza} -f qm.lang
%{_libdir}/libAnalitza.so.%{Analitza_major}*

#---------------------------------------------

%define AnalitzaGui_major %{Analitza_major}
%define libAnalitzaGui %mklibname AnalitzaGui %{AnalitzaGui_major}

%package -n %{libAnalitzaGui}
Summary:	Runtime library for %{name}
Group:		System/Libraries
Obsoletes:	%{mklibname analitzagui 6} < 15012.0

%description -n %{libAnalitzaGui}
The analitza library will let you add mathematical features to your program.
This pakage provide the runtime library for %{name}.

%files -n %{libAnalitzaGui}
%{_libdir}/libAnalitzaGui.so.%{AnalitzaGui_major}*

#---------------------------------------------

%define AnalitzaPlot_major %{Analitza_major}
%define libAnalitzaPlot %mklibname AnalitzaPlot %{AnalitzaPlot_major}

%package -n %{libAnalitzaPlot}
Summary:	Runtime library for %{name}
Group:		System/Libraries
Requires:	analitza-plots
Obsoletes:	%{mklibname analitzaplot 6} < 15012.0

%description -n %{libAnalitzaPlot}
The analitza library will let you add mathematical features to your program.
This pakage provide the runtime library for %{name}.

%files -n %{libAnalitzaPlot}
%{_libdir}/libAnalitzaPlot.so.%{AnalitzaPlot_major}*

#---------------------------------------------

%define AnalitzaWidgets_major %{Analitza_major}
%define libAnalitzaWidgets %mklibname AnalitzaWidgets %{AnalitzaWidgets_major}

%package -n %{libAnalitzaWidgets}
Summary:	Widget library for %{name}
Group:		System/Libraries
Obsoletes:	%{mklibname analitzawidgets 6} < 15012.0

%description -n %{libAnalitzaWidgets}
The analitza library will let you add mathematical features to your program.
This pakage provide the Widgets library for %{name}.

%files -n %{libAnalitzaWidgets}
%{_libdir}/libAnalitzaWidgets.so.%{AnalitzaWidgets_major}*

#---------------------------------------------
%package -n %{_lib}analitza-qml
Summary:	QML support for Analitza
Group:		System/Libraries

%description -n %{_lib}analitza-qml
QML support for Analitza

%files -n %{_lib}analitza-qml
%{_libdir}/qt5/qml/org/kde/analitza

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
%{_includedir}/Analitza5
%{_libdir}/libAnalitza.so
%{_libdir}/libAnalitzaGui.so
%{_libdir}/libAnalitzaPlot.so
%{_libdir}/libAnalitzaWidgets.so
%{_libdir}/cmake/Analitza5

#----------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%cmake_kde5 \
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
	echo "%%lang($(echo $r|cut -d/ -f5)) $(echo $r |cut -b2-)" >>$TOP/qm.lang
done
