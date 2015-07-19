%ifarch %{arm}
%bcond_with opengl
%else
%bcond_without opengl
%endif

%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Library that will let you add mathematical features to your program
Name:		analitza
Version:	15.04.3
Release:	2
License:	LGPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
# add SHOULD_BUILD_OPENGL option, to be able to disable support
# on arm because plotter3d assumes qreal=double all over the place
Patch0:		analitza-14.12.0-opengl_optional.patch
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

%define analitza_major 6
%define libanalitza %mklibname analitza %{analitza_major}

%package -n %{libanalitza}
Summary:	Runtime library for %{name}
Group:		System/Libraries
# calgebra used to be part of KDE4 analitza, but is gone now
Obsoletes:	calgebra < %{EVRD}

%description -n %{libanalitza}
The analitza library will let you add mathematical features to your program.
This pakage provide the runtime library for %{name}.

%files -n %{libanalitza}
%{_libdir}/libAnalitza.so.%{analitzagui_major}*

#---------------------------------------------

%define analitzagui_major 6
%define libanalitzagui %mklibname analitzagui %{analitzagui_major}

%package -n %{libanalitzagui}
Summary:	Runtime library for %{name}
Group:		System/Libraries

%description -n %{libanalitzagui}
The analitza library will let you add mathematical features to your program.
This pakage provide the runtime library for %{name}.

%files -n %{libanalitzagui}
%{_libdir}/libAnalitzaGui.so.%{analitzagui_major}*

#---------------------------------------------

%define analitzaplot_major 6
%define libanalitzaplot %mklibname analitzaplot %{analitzaplot_major}

%package -n %{libanalitzaplot}
Summary:	Runtime library for %{name}
Group:		System/Libraries
Requires:	analitza-plots

%description -n %{libanalitzaplot}
The analitza library will let you add mathematical features to your program.
This pakage provide the runtime library for %{name}.

%files -n %{libanalitzaplot}
%{_libdir}/libAnalitzaPlot.so.%{analitzaplot_major}*

#---------------------------------------------

%define analitzawidgets_major 6
%define libanalitzawidgets %mklibname analitzawidgets %{analitzawidgets_major}

%package -n %{libanalitzawidgets}
Summary:	Widget library for %{name}
Group:		System/Libraries

%description -n %{libanalitzawidgets}
The analitza library will let you add mathematical features to your program.
This pakage provide the Widgets library for %{name}.

%files -n %{libanalitzawidgets}
%{_libdir}/libAnalitzaWidgets.so.%{analitzawidgets_major}*

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
Requires:	kdelibs4-devel
Requires:	%{libanalitza} = %{EVRD}
Requires:	%{libanalitzagui} = %{EVRD}
Requires:	%{libanalitzaplot} = %{EVRD}
Requires:	%{libanalitzawidgets} = %{EVRD}

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
%patch0 -p1 .opengl_arm_float

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
