Name: mesaplot
Version: 0.3.4
Release:	1%{?dist}
Summary: A graphical and dynamical interface written in python for plotting MESA data.

Group: Applications/File
License: GPL
URL: http://mesastar.org/tools-utilities/python-based-stuff/mesaplot/mesaplot_v0-3.2-1
Source0: http://www.mleewise.com/mesaplot-%{version}.tgz
BuildArch: noarch

%define _pydir $RPM_BUILD_ROOT/usr/lib/python2.7/site-packages

#BuildRequires:	
Requires: numpy, python-matplotlib, wxPython

%description
MESAplot is an open-source, graphical and dynamical interface written in python for plotting MESA data. It is a replacement for the mathematica-based MESAFace. It uses wxPython, matplotlib, and numpy. One of our major goals in creating this new software was to make something very easy to install and use for both research and educational purposes.

%prep
%setup

%install
mkdir -p %{_pydir}/mesaplot
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
mkdir $RPM_BUILD_ROOT/%{_mandir}/man5

cp *.py %{_pydir}/mesaplot
cp mesaplot.conf $RPM_BUILD_ROOT/%{_sysconfdir}
cp mesaplot.1.gz $RPM_BUILD_ROOT/%{_mandir}/man1
cp mesaplot.conf.5.gz $RPM_BUILD_ROOT/%{_mandir}/man5

chmod 644 $RPM_BUILD_ROOT/%{_mandir}/man1/mesaplot.1.gz
chmod 644 $RPM_BUILD_ROOT/%{_mandir}/man5/mesaplot.conf.5.gz
#chown root:root $RPM_BUILD_ROOT/%{_mandir}/man1/mesaplot.1.gz
#chown root:root $RPM_BUILD_ROOT/%{_mandir}/man5/mesaplot.conf.5.gz
chmod 644 $RPM_BUILD_ROOT/%{_sysconfdir}/mesaplot.conf
#chown root:root $RPM_BUILD_ROOT/%{_sysconfdir}/mesaplot.conf
chmod 644 %{_pydir}/mesaplot/*
#chown root:root %{_pydir}/mesaplot/*


%files
%{_pydir}/mesaplot/*.py
$RPM_BUILD_ROOT/%{_sysconfdir}/mesaplot.conf
$RPM_BUILD_ROOT/%{_mandir}/man1/mesaplot.1.gz
$RPM_BUILD_ROOT/%{_mandir}/man5/mesaplot.conf.5.gz

%doc



%changelog

