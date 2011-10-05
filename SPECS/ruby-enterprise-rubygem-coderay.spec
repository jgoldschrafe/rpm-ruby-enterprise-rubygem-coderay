%define ruby_dist ruby-enterprise
%define ruby_dist_dash %{ruby_dist}-
%define _prefix /opt/ruby-enterprise
%define _gem %{_prefix}/bin/gem
%define _ruby %{_prefix}/bin/ruby

# Generated from coderay-0.9.7.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(%{_ruby} -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(%{_ruby} -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname coderay
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Fast syntax highlighting for selected languages
Name: %{?ruby_dist_dash}rubygem-%{gemname}
Version: 0.9.7
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://coderay.rubychan.de
Source0: http://gemcutter.orggems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?ruby_dist_dash}rubygems
BuildRequires: %{?ruby_dist_dash}rubygems
BuildArch: noarch
Provides: %{?ruby_dist_dash}rubygem(%{gemname}) = %{version}

%description
Fast and easy syntax highlighting for selected languages, written in Ruby.
Comes with RedCloth integration and LOC counter.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
%{_gem} install --local --install-dir %{buildroot}%{gemdir} \
                --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/coderay
%{_bindir}/coderay_stylesheet
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/lib/README
%doc %{geminstdir}/FOLDERS
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Mon Oct  3 2011 Jeff Goldschrafe <jeff@holyhandgrenade.org> - 0.9.7-1.hhg
- Rebuild for Ruby Enterprise Edition

* Thu Apr 28 2011 Sergio Rubio <rubiojr@frameos.org> - 0.9.7-1
- Initial package
