Name:           mesaplot
Version:        0.3.4
Release:        1%{?dist}
Summary:        A graphical and dynamical interface written in python for plotting MESA data.

Group:          Applications/File
License:        GPL
URL:            http://mesastar.org/tools-utilities/python-based-stuff/mesaplot/mesaplot_v0-3.2-1
Source0:        http://www.mleewise.com/mesaplot-%{version}.tgz
BuildArch:      noarch

BuildRequires:  python
Requires:       python >= 2.6, numpy, python-matplotlib, wxPython

%description
MESAplot is an open-source, graphical and dynamical interface written in python for plotting MESA data. It is a replacement for the mathematica-based MESAFace. It uses wxPython, matplotlib, and numpy. One of our major goals in creating this new software was to make something very easy to install and use for both research and educational purposes.

%prep
%setup

%install
mkdir -p $RPM_BUILD_ROOT%{python_sitelib}/mesaplot
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir $RPM_BUILD_ROOT%{_mandir}/man5
mkdir -p $RPM_BUILD_ROOT%{_bindir}

install -m 644 *.py $RPM_BUILD_ROOT%{python_sitelib}/mesaplot
install -m 644 mesaplot.conf $RPM_BUILD_ROOT%{_sysconfdir}
install -m 644 mesaplot.1.gz $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 mesaplot.conf.5.gz $RPM_BUILD_ROOT%{_mandir}/man5
install -m 755 mesaplot $RPM_BUILD_ROOT%{_bindir}

%files
%defattr(-,root,root)
%config(noreplace) %verify(not md5 mtime size) /etc/mesaplot.conf
/usr/share/man/man1/mesaplot.1.gz
/usr/share/man/man5/mesaplot.conf.5.gz
/usr/lib/python2.7/site-packages/mesaplot/file_manager.py
/usr/lib/python2.7/site-packages/mesaplot/mesaoutput1.py
/usr/lib/python2.7/site-packages/mesaplot/plot_manager.py
/usr/lib/python2.7/site-packages/mesaplot/mesaplot.py
#bytecode files get created by rpmbuild and need to be included in files list
/usr/lib/python2.7/site-packages/mesaplot/file_manager.pyc
/usr/lib/python2.7/site-packages/mesaplot/file_manager.pyo
/usr/lib/python2.7/site-packages/mesaplot/mesaoutput1.pyc
/usr/lib/python2.7/site-packages/mesaplot/mesaoutput1.pyo
/usr/lib/python2.7/site-packages/mesaplot/mesaplot.pyc
/usr/lib/python2.7/site-packages/mesaplot/mesaplot.pyo
/usr/lib/python2.7/site-packages/mesaplot/plot_manager.pyc
/usr/lib/python2.7/site-packages/mesaplot/plot_manager.pyo
/usr/bin/mesaplot

%doc README

%changelog
* Tue Jun 14 2016 Andrew Duty <tisbeok@gmail.com> - 0.3.4
- first release
