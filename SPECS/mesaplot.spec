Name:           mesaplot
Version:        0.3.4
Release:        1%{?dist}
Summary:        A graphical and dynamical interface written in python for plotting MESA data

Group:          Applications/File
License:        GPLv2
URL:            http://mesastar.org/tools-utilities/python-based-stuff/mesaplot/mesaplot_v0-3.2-1
Source0:        http://www.mleewise.com/mesaplot-%{version}.tar.gz
BuildArch:      noarch

patch0: %{name}_to_lower.patch

patch1: mesaoutput1_to_lower.patch

BuildRequires:  python >= 2.6
BuildRequires:  python < 3
Requires:       python >= 2.6
Requires:       python < 3
Requires:       numpy
Requires:       python-matplotlib
Requires:       python-matplotlib-wx
Requires:       wxPython

%description
MESAplot is an open-source, graphical and dynamical interface written in \
python for plotting MESA data. It is a replacement for the mathematica-based \
MESAFace. It uses wxPython, matplotlib, and numpy. One of our major goals in \
creating this new software was to make something very easy to install and \
use for both research and educational purposes.

%prep
%setup -q

# correct refereces to uppercase modules in mesaplot.py
%patch0 -p1

# correct refereces to uppercase modules in mesaoutput1.py
%patch1 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{python_sitelib}/mesaplot
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir $RPM_BUILD_ROOT%{_mandir}/man5
mkdir -p $RPM_BUILD_ROOT%{_bindir}

install -m 644 *.py $RPM_BUILD_ROOT%{python_sitelib}/mesaplot
install -m 666 config.txt $RPM_BUILD_ROOT%{python_sitelib}/mesaplot
install -m 644 mesaplot.conf $RPM_BUILD_ROOT%{_sysconfdir}
install -m 644 mesaplot.1.gz $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 mesaplot.conf.5.gz $RPM_BUILD_ROOT%{_mandir}/man5
install -m 755 mesaplot $RPM_BUILD_ROOT%{_bindir}
ln -s %{_sysconfdir}/mesaplot.conf $RPM_BUILD_ROOT%{python_sitelib}/mesaplot/default_settings.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mesaplot.conf
%{python_sitelib}/mesaplot/default_settings.py
%exclude %{python_sitelib}/mesaplot/default_settings.pyc
%exclude %{python_sitelib}/mesaplot/default_settings.pyo
%{_mandir}/man1/mesaplot.1.gz
%{_mandir}/man5/mesaplot.conf.5.gz
%{python_sitelib}/mesaplot/file_manager.py
%{python_sitelib}/mesaplot/mesaoutput1.py
%{python_sitelib}/mesaplot/plot_manager.py
%{python_sitelib}/mesaplot/mesaplot.py
%{python_sitelib}/mesaplot/config.txt
#bytecode files get created by rpmbuild and need to be included in files list
%{python_sitelib}/mesaplot/file_manager.pyc
%{python_sitelib}/mesaplot/file_manager.pyo
%{python_sitelib}/mesaplot/mesaoutput1.pyc
%{python_sitelib}/mesaplot/mesaoutput1.pyo
%{python_sitelib}/mesaplot/mesaplot.pyc
%{python_sitelib}/mesaplot/mesaplot.pyo
%{python_sitelib}/mesaplot/plot_manager.pyc
%{python_sitelib}/mesaplot/plot_manager.pyo
%{_bindir}/mesaplot

%doc README

%changelog
* Tue Jun 14 2016 Andrew Duty <tisbeok@gmail.com> 0.3.4-1.centos
- first release
