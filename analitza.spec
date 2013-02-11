Name:		analitza
Summary:	Library that will let you add mathematical features to your program
Version:	4.10.0
Release:	1
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

%package plots
Summary:	Plots used by the libanalitzaplot library
Group:		Graphical desktop/KDE
BuildArch:	noarch

%description plots
This package provides plots used by the libanalitzaplot library.

%files plots
%{_kde_appsdir}/libanalitza/plots/basic_curves.plots

#---------------------------------------------

%define analitza_major 4
%define libanalitza %mklibname analitza %{analitza_major}

%package -n %{libanalitza}
Summary:	Runtime library for %{name}
Group:		System/Libraries

%description -n %{libanalitza}
The analitza library will let you add mathematical features to your program.
This pakage provide the runtime library for %{name}.

%files -n %{libanalitza}
%{_kde_libdir}/libanalitza.so.%{analitzagui_major}*

#---------------------------------------------

%define analitzagui_major 4
%define libanalitzagui %mklibname analitzagui %{analitzagui_major}

%package -n %{libanalitzagui}
Summary:	Runtime library for %{name}
Group:		System/Libraries

%description -n %{libanalitzagui}
The analitza library will let you add mathematical features to your program.
This pakage provide the runtime library for %{name}.

%files -n %{libanalitzagui}
%{_kde_libdir}/libanalitzagui.so.%{analitzagui_major}*

#---------------------------------------------

%define analitzaplot_major 4
%define libanalitzaplot %mklibname analitzaplot %{analitzaplot_major}

%package -n %{libanalitzaplot}
Summary:	Runtime library for %{name}
Group:		System/Libraries
Requires:	analitza-plots

%description -n %{libanalitzaplot}
The analitza library will let you add mathematical features to your program.
This pakage provide the runtime library for %{name}.

%files -n %{libanalitzaplot}
%{_kde_libdir}/libanalitzaplot.so.%{analitzaplot_major}*

#---------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	kdelibs4-devel
Requires:	%{libanalitza} = %{EVRD}
Requires:	%{libanalitzagui} = %{EVRD}
Requires:	%{libanalitzaplot} = %{EVRD}

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

%changelog
* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.0-1
- New version 4.10.0
- New subpackage libanalitzaplot
- New subpackage plots
- Fix some summaries and descriptions

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.1-1
- New version 4.9.1

* Mon Aug 13 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.0-1
- New version 4.9.0

* Thu Jul 19 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.97-1
- New version 4.8.97

* Mon Jul 02 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.95-1
- New version 4.8.95

* Sat Jun 09 2012 Crispin Boylan <crisb@mandriva.org> 4.8.4-1
+ Revision: 803730
- New release

* Fri May 04 2012 Crispin Boylan <crisb@mandriva.org> 4.8.3-1
+ Revision: 796277
- New release

* Thu Apr 19 2012 Crispin Boylan <crisb@mandriva.org> 4.8.2-1
+ Revision: 792020
- New release

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New upstream tarball

* Sun Feb 26 2012 Andrey Bondrov <abondrov@mandriva.org> 4.8.0-2
+ Revision: 780796
- Add BuildRequires libreadline-devel and calgebra subpackage

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.8.0-1
+ Revision: 762439
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.97-1
+ Revision: 758030
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.95-1
+ Revision: 744506
- New upstream tarball

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.90-1
+ Revision: 739342
- New upstream tarball

* Wed Nov 23 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.80-1
+ Revision: 732995
- Import analitza
- create analitza repo

