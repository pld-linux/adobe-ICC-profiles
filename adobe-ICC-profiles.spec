#######
# TODO:
# - what is the real license? If not distributable - make license_agreement bcond
#   http://www.adobe.com/support/downloads/license.html
# - check _iccdir ?
Summary:	Adobe ICC profiles
Summary(pl.UTF-8):	Profile ICC firmy Adobe
Name:		adobe-ICC-profiles
Version:	20070807
Release:	0.1
License:	Free to use, distribution restricted
Group:		Applications/Graphics
#Source0:	http://download.adobe.com/pub/adobe/iccprofiles/win/AdobeICCProfilesWin_end-user.zip
Source0:	http://download.adobe.com/pub/adobe/iccprofiles/win/AdobeICCProfilesWin_bundler.zip
# NoSource0-md5:	296d093d5171a8cc333ff7a360441fed
URL:		http://www.adobe.com/support/downloads/product.jsp?product=62&platform=Windows
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_iccdir		%{_datadir}/color/icc

%description
Adobe wants to enable consistent, high-quality color workflows. For
color workflows to succeed, color information must be shared by many
people, from original creator to final publisher. For this reason,
Adobe is supplying its ICC profiles as a free download for graphics
professionals to use across their workflows.

3 RGB profiles:
- Adobe RGB (1998)
- Apple RGB
- ColorMatch RGB

12 CMYK profiles:
- US Web Coated (SWOP) v2
- US Web Uncoated v2
- US Sheetfed Coated v2
- US Sheetfed Uncoated v2
- Coated FOGRA27 (ISO 12647-2:2004)
- Web Coated FOGRA28 (ISO 12647-2:2004)
- Uncoated FOGRA29 (ISO 12647-2:2004)
- Coated FOGRA39 (ISO 12647-2:2004)
- Japan Web Coated (Ad)
- Japan Color 2001 Coated
- Japan Color 2001 Uncoated
- Japan Color 2002 Newspaper 

%description -l pl.UTF-8
Adobe chce umożliwoć spójne przepływy kolorów wysokiej jakości. Aby
przepływy kolorów były możliwe, informacje o kolorach muszą być
współdzielone przez wiele osób, od początkowego twórcy do ostatecznego
wydawcy. W tym celu Adobe udostępnia profile ICC do darmowego pobrania
przez profesjonalnych grafików do używania w ciągu całej pracy.

3 profile RGB:
- Adobe RGB (1998)
- Apple RGB
- ColorMatch RGB

12 profili CMYK:
- US Web Coated (SWOP) v2
- US Web Uncoated v2
- US Sheetfed Coated v2
- US Sheetfed Uncoated v2
- Coated FOGRA27 (ISO 12647-2:2004)
- Web Coated FOGRA28 (ISO 12647-2:2004)
- Uncoated FOGRA29 (ISO 12647-2:2004)
- Coated FOGRA39 (ISO 12647-2:2004)
- Japan Web Coated (Ad)
- Japan Color 2001 Coated
- Japan Color 2001 Uncoated
- Japan Color 2002 Newspaper 

%prep
%setup -q -n 'Adobe\ ICC\ Profiles\ \(bundler\)'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iccdir}
install */*.icc $RPM_BUILD_ROOT%{_iccdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.pdf
%dir %{_iccdir}
%{_iccdir}/*.icc
