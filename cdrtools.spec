Summary:	A command line CD/DVD-Recorder
Summary(pl):	Program do nagrywania p³yt CD/DVD
Name:		cdrtools
Version:	1.11a38
Release:	1
Epoch:		2
License:	GPL v2
Group:		Applications/System
#Source0:	ftp://ftp.fokus.gmd.de/pub/unix/cdrecord/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.fokus.gmd.de/pub/unix/cdrecord/alpha/%{name}-%{version}.tar.bz2
Patch0:		%{name}-config.patch
Patch1:		%{name}-smmap.patch
URL:		http://www.fokus.gmd.de/research/cc/glone/employees/joerg.schilling/private/cdrecord.html
BuildRequires:	autoconf
BuildRequires:	automake
Obsoletes:	cdrecord
Provides:	cdrecord
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cdrecord allows you to create CD's on a CD-Recorder (SCSI/ATAPI).
Supports data, audio, mixed, multi-session and CD+ discs etc.

%description -l pl
Cdrecord pozwala tworzyæ CD na nagrywarce CD (SCSI/ATAPI). Obs³uguje
dyski z danymi, d¼wiêkiem, mieszane, wielosesyjne, CD+ i inne.

%package devel
Summary:	The libschily SCSI user level transport library
Summary(pl):	Biblioteka dostêpu do poziomu SCSI przez u¿ytkownika
Group:		Development/Libraries
Obsoletes:	cdrecord-devel

%description devel
The %{name} distribution contains a SCSI user level transport library.
The SCSI library is suitable to talk to any SCSI device without having
a special driver for it. Cdrecord may be easily ported to any system
that has a SCSI device driver similar to the scg driver.

%description devel -l pl
Dystrybucja %{name} zawiera bibliotekê dostêpu do warstwy transportu w
SCSI. Poprzez bibliotekê mo¿na komunikowaæ siê z dowolnym urz±dzeniem
SCSI bez potrzeby posiadania specjalnego sterownika do tego
urz±dzenia.

%package cdda2wav
Summary:	Get WAV files from digital audio cd's
Summary(pl):	Uzyskaj pliki WAV z cyfrowego kompaktu audio
Summary(fr):	convertisseur CD-Audio->.wav
Group:		Applications/Sound
Provides:	cdda2wav
Obsoletes:	cdda2wav
Obsoletes:	cdrecord-cdda2wav

%description cdda2wav
A sampling utility for cdrom drives that are capable of sending audio
cd data in digital form to your host. Data can be dumped into wav or
sun format sound files. Options control the recording format
(stereo/mono; 8,12,16 bits; different rates).

%description cdda2wav -l pl
Narzêdzie do zczytywania danych z napêdów cdrom, które s± w stanie
wysy³aæ strumieñ audio. Dane mog± zostaæ zapisane w formacie plików
wav lub suna.

%package readcd
Summary:	Read/Write data Compact Discs
Summary(pl):	Odczytuje/Zapisuje dane z P³yt Kompaktowych
Group:		Applications/System
Obsoletes:	cdrecord-readcd

%description readcd
Read/Write data Compact Discs

%description readcd -l pl
Odczytuje/Zapisuje dane z P³yt Kompaktowych

%package utils
Summary:	Dumping and verifying iso9660 images.
Summary(pl):	Zrzucanie i weryfikacja obrazów iso9660.
Group:		Applications/System

%description utils
Utility programs for dumping and verifying iso9660 images.

%description utils -l pl
Narzêdzia do zrzucania i weryfikacji obrazów iso9660.

%package mkisofs
Summary:	Creates an ISO9660 filesystem image
Summary(de):	Erstellt ein Dateisystem-Abbild nach ISO9660
Summary(fr):	Crée un image système de fichiers ISO9660
Summary(pl):	Tworzy obraz systemu plikow ISO9660
Summary(tr):	ISO9660 dosya sistemi kopyasý oluþturur
Group:		Applications/System
Provides:	mkisofs
Obsoletes:	mkisofs

%description mkisofs
This is the mkisofs package. It is used to create ISO 9660 file system
images for creating CD-ROMs.

%description mkisofs -l pl
To jest pakiet mkisofs. Jest on u¿ywany do tworzenia obrazów systemów
plików ISO9660 potrzebnych do tworzenia p³yt CD-ROM.

%prep
%setup -q -n %{name}-1.11
chmod +w -R *
%patch0 -p1
%patch1 -p1

%build
cd conf
cp xconfig.h.in xconfig.h.in.org
sed -e 's#/\*.*\*/##g' xconfig.h.in.org > xconfig.h.in
rm -f acgeneral.m4 acspecific.m4 autoheader.m4 acoldnames.m4 autoconf.m4
%{__aclocal}
%{__autoconf}
cd ..
CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" ./Gmake.linux

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_includedir}/schily/scg}

./Gmake.linux install \
	MANDIR=share/man \
	INS_BASE=$RPM_BUILD_ROOT%{_prefix}

# Installing Header files for use with devel package
rm -f include/scg

install include/*		$RPM_BUILD_ROOT%{_includedir}/schily
install incs/*/xconfig.h	$RPM_BUILD_ROOT%{_includedir}/schily
install libscg/scg/*		$RPM_BUILD_ROOT%{_includedir}/schily/scg

install cdrecord/cdrecord.dfl	$RPM_BUILD_ROOT%{_sysconfdir}/cdrecord.conf

# fix manual pages
echo ".so man8/isoinfo.8" >	$RPM_BUILD_ROOT%{_mandir}/man8/devdump.8
echo ".so man8/isoinfo.8" >     $RPM_BUILD_ROOT%{_mandir}/man8/isovfy.8
echo ".so man8/isoinfo.8" >     $RPM_BUILD_ROOT%{_mandir}/man8/isodump.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AN-%{version} doc/cdrecord.ps Changelog README README.ATAPI README.WORM
%doc README.audio README.cdplus README.cdtext README.cdrw README.copy
%doc README.linux README.mkisofs README.multi README.parallel README.raw
%doc README.rscsi README.sony README.verify
%doc cdrecord/cdrecord.dfl
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/cdrecord.conf
%attr(755,root,root) %{_bindir}/cdrecord
%attr(755,root,root) %{_sbindir}/rscsi
%{_mandir}/man1/cdrecord.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_includedir}/schily
%{_includedir}/*.h
#%attr(755,root,root) %{_bindir}/scgcheck
#%{_mandir}/man1/scgcheck.1*

%files cdda2wav
%defattr(644,root,root,755)
%doc cdda2wav/Frontends cdda2wav/HOWTOUSE cdda2wav/OtherProgs
%doc cdda2wav/README cdda2wav/THANKS cdda2wav/TODO cdda2wav/cdda2mp3
%doc cdda2wav/cdda2mp3.new cdda2wav/cdda_links cdda2wav/pitchplay
%doc cdda2wav/readmult cdda2wav/tracknames.pl cdda2wav/tracknames.txt
%doc cdda2wav/FAQ cdda2wav/cdda2ogg
%attr(755,root,root) %{_bindir}/cdda2wav
%{_mandir}/man1/cdda2wav.1*

%files readcd
%defattr(644,root,root,755)
%{_mandir}/man1/readcd.1*
%attr(755,root,root) %{_bindir}/readcd

%files utils
%defattr(644,root,root,755)
%{_mandir}/man8/isoinfo.8*
%{_mandir}/man8/devdump.8*
%{_mandir}/man8/isovfy.8*
%{_mandir}/man8/isodump.8*
%attr(755,root,root) %{_bindir}/devdump
%attr(755,root,root) %{_bindir}/isodebug
%attr(755,root,root) %{_bindir}/isoinfo
%attr(755,root,root) %{_bindir}/isovfy
%attr(755,root,root) %{_bindir}/isodump

%files mkisofs
%defattr(644,root,root,755)
%{_mandir}/man8/mkisofs.8*
%{_mandir}/man8/mkhybrid.8*
%attr(755,root,root) %{_bindir}/mkisofs
%attr(755,root,root) %{_bindir}/mkhybrid
%doc mkisofs/README.compression mkisofs/README.eltorito mkisofs/README
%doc mkisofs/README.graft_dirs mkisofs/README.hfs_boot mkisofs/README.hfs_magic
%doc mkisofs/README.hide mkisofs/README.joliet mkisofs/README.mkhybrid
%doc mkisofs/README.prep_boot mkisofs/README.rootinfo mkisofs/README.session
%doc mkisofs/README.sort mkisofs/README.sparcboot
