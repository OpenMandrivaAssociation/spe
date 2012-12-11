Summary:	A Python-based IDE 
Name:		spe
Version:	0.8.4.h
Release:	%{mkrel 3}
Source0:	http://download.berlios.de/python/%{name}-%{version}-wx2.6.1.0.tar.gz
License:	GPLv2+
Group:		Development/Python
URL:		http://pythonide.stani.be 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-devel
BuildRequires:	imagemagick
Requires:	wxPython >= 2.6.1.0
Requires:	pychecker

%description
Spe is a free Python IDE with auto indentation & completion, call tips, 
syntax coloring & highlighting, UML diagrams, class explorer, source index, 
auto todo list, sticky notes, pycrust shell, file browsers, drag&drop, 
context help and Blender support.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --compile --optimize=2

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{48x48,32x32,16x16}/apps
convert build/lib/_spe/images/spe.png -scale 48x48 %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert build/lib/_spe/images/spe.png -scale 32x32 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert build/lib/_spe/images/spe.png -scale 16x16 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=SPE
Comment=Python IDE
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Development;IDE;
EOF

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%{py_puresitedir}/_%{name}
%{py_puresitedir}/*.egg-info
%{_bindir}/%{name}*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png



%changelog
* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.8.4.h-3mdv2010.0
+ Revision: 445202
- rebuild

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 0.8.4.h-2mdv2009.1
+ Revision: 319721
- rebuild with python 2.6

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Wed Aug 20 2008 Adam Williamson <awilliamson@mandriva.org> 0.8.4.h-1mdv2009.0
+ Revision: 274406
- correct group
- clean file list
- correct .desktop file name, summary, icon name, categories
- fd.o icons
- use --optimize=2 to get .pyo files
- use %%{buildroot} not $RPM_BUILD_ROOT
- requires pychecker
- new license policy
- wx2.6.1.0 is not part of the version just indicates requires wx version
- upstream stopped using SPE in tarball name so no need for that define
- new release 0.8.4.h

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.8.2.a_wx2.6.1.0-2mdv2008.1
+ Revision: 140850
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Tue Dec 05 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 0.8.2.a_wx2.6.1.0-2mdv2007.0
+ Revision: 91333
- Rebuild against new python
- import spe-0.8.2.a_wx2.6.1.0-1mdv2007.0

* Sat Aug 26 2006 Stew Benedict <sbenedict@mandriva.com> 0.8.2.a_wx2.6.1.0-1mdv2007.0
- 0.8.2.a-wx2.6.1.0, xdg menu

* Tue Dec 20 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.8.1.b_wx2.6.1.0_bl2.35-2mdk
- Fix BuildRequires

* Fri Dec 16 2005 Stew Benedict <sbenedict@mandriva.com> 0.8.1.b_wx2.6.1.0_bl2.35-1mdk
- 0.8.1.b-wx2.6.1.0.-bl2.35

* Fri Oct 21 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.7.5.c_wx2.6.1.0_bl2.35-2mdk
- Fix BuildRequires
- %%{1}mdv2007.1

* Thu Sep 29 2005 Stew Benedict <sbenedict@mandriva.com> 0.7.5.c_wx2.6.1.0_bl2.35-1mdk
- first Mandriva release

