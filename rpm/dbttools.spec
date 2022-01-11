%global debug_package %{nil}
%global pkgname dbttools
%{!?pkgrevision: %global pkgrevision 1}
%define installpath /usr/bin

Name:          %{pkgname}
Version:       %{pkgversion}
Release:       %{pkgrevision}%{?dist}
Summary:       TPC-C benchmark kit - tools
License:       The Artistic License
Source:        dbttools-%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:      R-core


%description
TPC-C benchmark kit - tools

%prep
%setup -q -n dbttools-%{version}

%build
cmake -H. -DCMAKE_INSTALL_PREFIX=%{buildroot}/%{installpath}/..

%install
%{__install} -d %{buildroot}/%{installpath}
make install

%files
%{installpath}/dbt-plot-pidstat
%{installpath}/dbt-plot-sar-blockdev
%{installpath}/dbt-plot-sar-cpu
%{installpath}/dbt-plot-sar-mem
%{installpath}/dbt-plot-sar-net
%{installpath}/dbt-plot-sar-swap
%{installpath}/dbt-plot-transaction-distribution
%{installpath}/dbt-process-pidstat
%{installpath}/dbt-pgsql-generate-db-html
%{installpath}/dbt-pgsql-generate-index-html
%{installpath}/dbt-pgsql-generate-table-html
%{installpath}/dbt-pgsql-plot-database-stats
%{installpath}/dbt-pgsql-plot-index-stats
%{installpath}/dbt-pgsql-plot-table-stats

%changelog
* Mon Nov 8 2021 Julien Tachoires <julien.tachoires@enterprisedb.com> - 0.1.0-1
- Initial packaging
