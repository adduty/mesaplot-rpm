Name: mesaplot
Version: 0.3.4
Release:	1%{?dist}
Summary: A graphical and dynamical interface written in python for plotting MESA data.

Group: Applications/File
License: GPL
URL: http://mesastar.org/tools-utilities/python-based-stuff/mesaplot/mesaplot_v0-3.2-1
Source0: http://www.mleewise.com/mesaplotDL.php

%define_pydir%{_libdir}/python2.7/site-packages

BuildRequires:	
Requires: numpy, python-matplotlib, wxPython

%description
MESAplot is an open-source, graphical and dynamical interface written in python for plotting MESA data. It is a replacement for the mathematica-based MESAFace. It uses wxPython, matplotlib, and numpy. One of our major goals in creating this new software was to make something very easy to install and use for both research and educational purposes.

%prep
%setup -q


%build
%configure
#make %{?_smp_mflags}


%install
#make install DESTDIR=%{buildroot}
cp *.py %{_pydir}i/mesaplot
cp mesaplot.conf %{_sysconfdir}
cp mesaplot.1.gz %{_mandir}/man1
cp mesaplot.conf.5.gz %{_mandir}/man5


%files
%{_pydir}i/mesaplot/*.py
%{_sysconfdir}/mesaplot.conf
%{_mandir}/man1/mesaplot.1.gz
%{_mandir}/man5/mesaplot.conf.5.gz

%doc



%changelog

