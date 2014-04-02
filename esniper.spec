Name:           esniper
Version:        2.29.0
Release:        1%{?dist}
Summary:        A lightweight console application for sniping eBay auctions 

Group:          Applications/Internet
License:        BSD
URL:            http://esniper.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-2-29-0.tgz

BuildRequires:  curl-devel

%description
Esniper is a lightweight console application for sniping eBay auctions.


%prep
%setup -q -n %{name}-2-29-0

# Encode manpage to utf-8
iconv -f iso8859-1 -t utf-8 esniper.1 > esniper.1.conv \
    && touch -r esniper.1 esniper.1.conv \
    && mv esniper.1.conv esniper.1


%build
%configure
make %{?_smp_mflags}


%install
make install INSTALL="install -p" DESTDIR=%{buildroot}

# Install frontend script
install -p -m 755 frontends/snipe %{buildroot}/%{_bindir}


%files
%doc frontends/README COPYING ChangeLog AUTHORS sample_config.txt sample_auction.txt
%{_bindir}/%{name}
%{_bindir}/snipe
%{_mandir}/man1/%{name}.1.*


%changelog
* Wed Apr 02 2014 Volker Fröhlich <volker27@gmx.at> - 2.29.0-1
- New upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 25 2012 Volker Fröhlich <volker27@gmx.at> - 2.28.0-1
- New upstream release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 06 2012 Volker Fröhlich <volker27@gmx.at> - 2.27.0-1
- New upstream release
- Remove curl fix from previous release (included upstream)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 09 2011 Volker Fröhlich <volker27@gmx.at> - 2.26.0-2
- Don't include curl's types.h

* Tue Aug 09 2011 Volker Fröhlich <volker27@gmx.at> - 2.26.0-1
- Update for 2.26.0
- Drop defattr

* Sun Jun 05 2011 Volker Fröhlich <volker27@gmx.at> - 2.25.0-1
- Updated for 2.25.0

* Fri Feb 25 2011 Volker Fröhlich <volker27@gmx.at> - 2.24.0-6
- Added the INSTALL definition, that should have been there in the last release

* Fri Feb 25 2011 Volker Fröhlich <volker27@gmx.at> - 2.24.0-5
- Preserve timestamp on man page
- Defined INSTALL for make

* Thu Feb 24 2011 Volker Fröhlich <volker27@gmx.at> - 2.24.0-4
- Added sample aution file
- More specific files section

* Fri Dec 03 2010 Volker Fröhlich <volker27@gmx.at> - 2.24.0-3
- Added sample configuration to docs
- Install frontend script
- Shortened file list syntax

* Thu Dec 02 2010 Volker Fröhlich <volker27@gmx.at> - 2.24.0-2
- Dropped clean section and rm command from install section,
  as it's no longer necessary
- Replaced .gz with * for man-file
- Adapted source link

* Sun Nov 28 2010 Volker Fröhlich <volker27@gmx.at> - 2.24.0-1
- Inital packaging
